import os
from pathlib import Path
from concurrent.futures import ProcessPoolExecutor, as_completed

def convert_one(src_path: str, out_dir: str, quality: int = 95):
    try:
        # Windows + multiprocessing için importları burada tutuyorum
        from PIL import Image
        import pillow_heif

        pillow_heif.register_heif_opener()

        src = Path(src_path)
        out = Path(out_dir)
        out.mkdir(exist_ok=True)

        dst = out / (src.stem + ".jpg")

        with Image.open(src) as img:
            # JPEG RGB ister, garantiye alıyoruz
            if img.mode != "RGB":
                img = img.convert("RGB")

            img.save(
                dst,
                format="JPEG",
                quality=quality,
                optimize=True,
                progressive=True
            )

        return True, src.name

    except Exception as e:
        return False, f"{Path(src_path).name} -> {e}"

def main():
    INPUT_DIR = Path("heic_fotolar")
    OUTPUT_DIR = Path("jpeg_fotolar")
    QUALITY = 95

    if not INPUT_DIR.exists():
        print("heic_fotolar klasörü yok, önce onu oluştur.")
        return

    heics = [p for p in INPUT_DIR.iterdir() if p.suffix.lower() == ".heic"]

    if not heics:
        print("Klasörde HEIC dosyası yok.")
        return

    cpu_count = os.cpu_count() or 4
    print(f"{len(heics)} foto bulundu | {cpu_count} çekirdek kullanılıyor")

    ok = 0
    fail = 0

    with ProcessPoolExecutor(max_workers=cpu_count) as executor:
        jobs = [
            executor.submit(convert_one, str(p), str(OUTPUT_DIR), QUALITY)
            for p in heics
        ]

        for job in as_completed(jobs):
            success, msg = job.result()
            if success:
                ok += 1
            else:
                fail += 1
                print("Hata:", msg)

    print(f"Bitti → Başarılı: {ok}, Hatalı: {fail}")

if __name__ == "__main__":
    main()
