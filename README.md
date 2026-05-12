# ERP Stok Kartı Tekilleştirme

## Proje Amacı
ERP sistemlerinde duplicate stok kartlarının tespit edilmesi.

## Kullanılan Teknolojiler
- Python
- Pandas
- Scikit-learn
- Notebook
- TF-IDF
- Cosine Similarity

## UML Diyagramları
Sistem tasarım diyagramları docs/uml klasörü içerisinde bulunmaktadır.

- Use Case Diagram
- Activity Diagram
- Class Diagram
- Component Diagram
- Sequence Diagram
## Performans Metrikleri

- Precision
- Recall
- F1-Score
- Accuracy
## Çalıştırma
pip install -r requirements.txt
## Metrik Sonuçları

Proje kapsamında sistemin ürettiği benzer stok kartı adayları `manuel_dogrulama_seti.csv` dosyası üzerinden manuel olarak doğrulanmıştır. Toplam 50 kayıt değerlendirilmiş ve sistem tahminleri ile manuel doğrulama etiketleri karşılaştırılmıştır.

| Metrik | Değer |
|---|---:|
| Değerlendirilen Kayıt Sayısı | 50 |
| Precision | 1.0 |
| Recall | 1.0 |
| F1-score | 1.0 |
| Accuracy | 1.0 |

Bu sonuçlar, seçilen 50 kayıt üzerinde yapılan pilot doğrulama değerlendirmesini göstermektedir. Daha geniş veri setleriyle ek doğrulama yapılması önerilmektedir.
## API Katmanı ve Uyarı Sistemi

Projeye FastAPI tabanlı bir servis katmanı eklenmiştir.

### Çalıştırma

```bash
py -m uvicorn src.api:app --reload
```

### Swagger Test Ekranı

```text
http://127.0.0.1:8000/docs
```
