# HEIC → JPEG Converter (Fast & Multi-Core)

Bu proje, HEIC formatındaki fotoğrafları **çok çekirdekli** şekilde hızlıca **JPEG** formatına dönüştürmek için yazılmış basit bir Python scriptidir.

Amaç:
- Apple’dan çıkan HEIC fotoğrafları
- Android, WhatsApp, Instagram gibi ortamlarda
- Sorunsuz ve hızlı şekilde kullanılabilir hale getirmek.

---

## Özellikler

- Çok çekirdekli işlem (tüm CPU gücünü kullanır)
- Toplu dönüştürme (yüzlerce foto için uygun)
- JPEG kalite: **95**
- Android ve sosyal medya uyumlu çıktı
- Hatalı dosyalarda durmaz, devam eder
- Girdi / çıktı klasörleri ayrı

---

## Gereksinimler

- Python **3.10+**
- Pillow
- pillow-heif

Kurulum:
```bash
py -m pip install pillow pillow-heif
```

---

## Klasör Yapısı

```text
heic-converter/
│
├─ main.py
├─ heic_fotolar/      # HEIC dosyalarını buraya at
├─ jpeg_fotolar/     # Çıktılar buraya yazılır
```

---

## Kullanım

1. Proje dizininde `heic_fotolar` adlı bir klasör oluştur
2. Dönüştürmek istediğin `.heic` dosyalarını içine koy
3. Scripti çalıştır:

```bash
python main.py
```

İşlem tamamlandığında dönüştürülen dosyalar `jpeg_fotolar` klasöründe olur.

---

## Neden JPEG?

- Android cihazlarda %100 uyum
- WhatsApp / Instagram / Telegram sorunsuz
- PNG’ye göre çok daha küçük dosya boyutu
- Fotoğraflar için kalite kaybı pratikte fark edilmez

---

## Notlar

- Script, mevcut CPU çekirdek sayısını otomatik algılar
- HEIC dosyaları RGB’ye çevrilerek kaydedilir
- Girdi ve çıktı klasörleri bilerek repo dışı bırakılmalıdır

---

## Lisans

Bu proje kişisel kullanım ve öğrenme amaçlıdır.
İstediğin gibi kullanabilir, düzenleyebilirsin.
