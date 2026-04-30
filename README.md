# ERP Stok Kartı Tekilleştirme

## Proje Amacı
ERP sistemlerinde duplicate stok kartlarının tespit edilmesi.

## Kullanılan Teknolojiler
- Python
- Pandas
- Scikit-learn
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
