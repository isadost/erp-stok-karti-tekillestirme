# GitHub'a Eklenecek Dosyalar

Aşağıdaki dosyaları repo içine ekleyin:

```text
src/api.py
docs/API_KATMANI.md
requirements.txt
```

Commit mesajı:

```text
add API warning service
```

README dosyasına eklenecek bölüm:

```markdown
## API Katmanı ve Uyarı Sistemi

Projeye FastAPI tabanlı bir servis katmanı eklenmiştir. Bu servis, ERP sisteminden gelen stok adı bilgisini alarak mevcut stok kartlarıyla benzerlik kontrolü yapmakta ve duplicate stok kartı riski varsa uyarı üretmektedir.

### Çalıştırma

```bash
pip install -r requirements.txt
uvicorn src.api:app --reload
```

### Örnek Endpoint

```text
POST /stok/benzerlik-kontrol
```
```

