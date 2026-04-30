from fastapi import FastAPI
from pydantic import BaseModel
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

app = FastAPI(
    title="ERP Stok Kartı Tekilleştirme API",
    description="ERP stok kartları için benzerlik kontrolü ve duplicate uyarı servisi",
    version="1.0.0"
)

DATA_PATH = "data.xlsx"
THRESHOLD = 0.90

class StokRequest(BaseModel):
    stok_adi: str

def load_data():
    df = pd.read_excel(DATA_PATH)
    df["STOK ADI"] = df["STOK ADI"].astype(str).str.strip().str.upper()
    df["YALIN HALİ"] = df["YALIN HALİ"].astype(str).str.strip().str.upper()
    df["STOK KODU"] = df["STOK KODU"].astype(str).str.strip().str.upper()
    return df

df = load_data()

vectorizer = TfidfVectorizer(analyzer="char_wb", ngram_range=(3, 5))
tfidf_matrix = vectorizer.fit_transform(df["YALIN HALİ"].fillna("").astype(str))

@app.get("/")
def home():
    return {
        "message": "ERP Stok Kartı Tekilleştirme API çalışıyor",
        "kayit_sayisi": len(df),
        "threshold": THRESHOLD
    }

@app.get("/health")
def health_check():
    return {
        "status": "ok",
        "data_loaded": True,
        "kayit_sayisi": len(df)
    }

@app.post("/stok/benzerlik-kontrol")
def benzerlik_kontrol(request: StokRequest):
    stok_adi = request.stok_adi.strip().upper()

    query_vector = vectorizer.transform([stok_adi])
    scores = cosine_similarity(query_vector, tfidf_matrix)[0]

    results = []

    for index, score in enumerate(scores):
        if score >= THRESHOLD:
            results.append({
                "stok_kodu": df.iloc[index]["STOK KODU"],
                "stok_adi": df.iloc[index]["STOK ADI"],
                "yalin_hali": df.iloc[index]["YALIN HALİ"],
                "benzerlik_skoru": round(float(score), 4),
                "uyari": "Benzer stok kartı mevcut olabilir"
            })

    results = sorted(results, key=lambda x: x["benzerlik_skoru"], reverse=True)

    return {
        "aranan_stok": stok_adi,
        "threshold": THRESHOLD,
        "benzer_kayit_sayisi": len(results),
        "uyari_durumu": len(results) > 0,
        "benzer_kayitlar": results[:10]
    }

@app.get("/stok/uyari-raporu")
def uyari_raporu():
    similarity_matrix = cosine_similarity(tfidf_matrix)
    warnings = []

    for i in range(len(df)):
        for j in range(i + 1, len(df)):
            score = similarity_matrix[i, j]

            if score >= THRESHOLD:
                warnings.append({
                    "stok_kodu_1": df.iloc[i]["STOK KODU"],
                    "stok_adi_1": df.iloc[i]["STOK ADI"],
                    "stok_kodu_2": df.iloc[j]["STOK KODU"],
                    "stok_adi_2": df.iloc[j]["STOK ADI"],
                    "benzerlik_skoru": round(float(score), 4),
                    "uyari": "Duplicate stok kartı riski"
                })

    return {
        "threshold": THRESHOLD,
        "uyari_sayisi": len(warnings),
        "uyarilar": warnings[:100]
    }
