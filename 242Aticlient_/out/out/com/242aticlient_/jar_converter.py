# ============================================
# EVRENSEL JAR DÖNÜŞTÜRÜCÜ
# Bu script, ELİNDEKİ HERHANGİ BİR DOSYAYI (java, json, txt, vs.)
# .jar DOSYASINA DÖNÜŞTÜRÜR.
# Hiçbir şeye bağımlı değildir. Java derlemesi bile GEREKTİRMEZ.
# ============================================

import os
import zipfile
import sys
import shutil
from pathlib import Path
from datetime import datetime

# ============================================
# KONFİGÜRASYON
# ============================================
JAR_ADI = "output.jar"  # Çıktı jar dosyasının adı
MANIFEST = True         # MANIFEST.MF eklemek istiyor musun?
COMPRESS = True         # Sıkıştırma (ZIP_DEFLATED) veya depolama

# ============================================
# YARDIMCI FONKSİYONLAR
# ============================================
def log(mesaj, durum="INFO"):
    """Terminale renkli log yazdırır."""
    renkler = {
        "INFO": "\033[94m[INFO]\033[0m",
        "OK": "\033[92m[OK]\033[0m",
        "HATA": "\033[91m[HATA]\033[0m",
        "UYARI": "\033[93m[UYARI]\033[0m",
        "YILDIZ": "\033[95m[✦]\033[0m"
    }
    print(f"{renkler.get(durum, renkler['INFO'])} {mesaj}")

def dosya_ve_klasorleri_listele(kok_dizin):
    """Belirtilen dizindeki TÜM dosya ve klasörleri listeler."""
    sonuclar = []
    for root, dirs, files in os.walk(kok_dizin):
        for dosya in files:
            sonuclar.append(os.path.join(root, dosya))
    return sonuclar

def klasor_kopyala(kaynak, hedef):
    """Bir klasörü ve içindekileri hedefe kopyalar."""
    if os.path.exists(hedef):
        shutil.rmtree(hedef)
    shutil.copytree(kaynak, hedef)
    log(f"Klasör kopyalandı: {kaynak} → {hedef}", "OK")

# ============================================
# ANA JAR OLUŞTURMA FONKSİYONU
# ============================================
def jar_olustur(girdi_yolu, cikti_yolu):
    """
    Herhangi bir dosya/klasörü .jar dosyasına dönüştürür.
    
    Parametreler:
    girdi_yolu (str): Kaynak dosya veya klasör yolu
    cikti_yolu (str): Hedef .jar dosya yolu
    """
    
    # 1. Girdi kontrolü
    if not os.path.exists(girdi_yolu):
        log(f"HATA: '{girdi_yolu}' bulunamadı!", "HATA")
        return False
    
    # 2. Hedef dizin kontrolü
    cikti_dizini = os.path.dirname(os.path.abspath(cikti_yolu))
    if not os.path.exists(cikti_dizini):
        os.makedirs(cikti_dizini, exist_ok=True)
        log(f"Hedef dizin oluşturuldu: {cikti_dizini}", "OK")
    
    # 3. Geçici dizin oluştur
    gecici_dizin = f"temp_jar_{datetime.now().strftime('%Y%m%d_%H%M%S')}"
    os.makedirs(gecici_dizin, exist_ok=True)
    
    try:
        # 4. Girdiyi geçici dizine kopyala
        if os.path.isfile(girdi_yolu):
            # Tek dosya ise
            shutil.copy2(girdi_yolu, os.path.join(gecici_dizin, os.path.basename(girdi_yolu)))
            log(f"Dosya kopyalandı: {os.path.basename(girdi_yolu)}", "OK")
        elif os.path.isdir(girdi_yolu):
            # Klasör ise
            klasor_kopyala(girdi_yolu, gecici_dizin)
        
        # 5. MANIFEST.MF ekle (isteğe bağlı)
        if MANIFEST:
            manifest_icerik = """Manifest-Version: 1.0
Created-By: Universal Jar Converter
Build-Jdk: 17
Main-Class: com._242aticlient.Main
"""
            manifest_yolu = os.path.join(gecici_dizin, "META-INF", "MANIFEST.MF")
            os.makedirs(os.path.dirname(manifest_yolu), exist_ok=True)
            with open(manifest_yolu, "w", encoding="utf-8") as f:
                f.write(manifest_icerik)
            log("MANIFEST.MF eklendi", "OK")
        
        # 6. Jar dosyasını oluştur
        compression = zipfile.ZIP_DEFLATED if COMPRESS else zipfile.ZIP_STORED
        with zipfile.ZipFile(cikti_yolu, "w", compression) as jar:
            for root, dirs, files in os.walk(gecici_dizin):
                for dosya in files:
                    tam_yol = os.path.join(root, dosya)
                    arcname = os.path.relpath(tam_yol, gecici_dizin)
                    jar.write(tam_yol, arcname)
        
        log(f"✅ Jar oluşturuldu: {os.path.abspath(cikti_yolu)}", "OK")
        return True
        
    except Exception as e:
        log(f"HATA: {str(e)}", "HATA")
        return False
    finally:
        # 7. Geçici dizini temizle
        if os.path.exists(gecici_dizin):
            shutil.rmtree(gecici_dizin)
            log("Geçici dizin temizlendi", "OK")

# ============================================
# KULLANICI ARAYÜZÜ
# ============================================
def main():
    print("=" * 60)
    print("        EVRENSEL JAR DÖNÜŞTÜRÜCÜ v1.0")
    print("   Elindeki her şeyi .jar yap — Hiçbir şeye bağlı değil!")
    print("=" * 60)
    print()
    
    # 1. Kullanıcıdan girdi al
    print("📂 Elindeki dosya veya klasörün YOLUNU yaz:")
    print("   (Örnek: C:\\Users\\Sen\\Desktop\\242Aticlient)")
    girdi = input("> ").strip()
    
    if not girdi:
        log("Girdi boş olamaz!", "HATA")
        sys.exit(1)
    
    # 2. Çıktı dosyasını sor
    print()
    print("📦 Çıktı jar dosyasının adını yaz (varsayılan: output.jar):")
    cikti_adi = input("> ").strip() or "output.jar"
    
    if not cikti_adi.endswith(".jar"):
        cikti_adi += ".jar"
    
    # 3. Yolu genişlet (kullanıcı adını çöz)
    girdi_yolu = os.path.abspath(os.path.expanduser(girdi))
    cikti_yolu = os.path.abspath(os.path.expanduser(cikti_adi))
    
    # 4. Jar oluştur
    print()
    log("Jar dönüştürme işlemi başlatılıyor...", "YILDIZ")
    print()
    
    basarili = jar_olustur(girdi_yolu, cikti_yolu)
    
    if basarili:
        print()
        print("=" * 60)
        print("🎉 TAMAMLANDI!")
        print(f"📦 Jar dosyan hazır: {cikti_yolu}")
        print("=" * 60)
        print()
        print("Not: Bu jar herhangi bir mod değildir. Sadece dosyalarını paketler.")
        print("Minecraft'ta çalışması için Fabric mod yapısına uygun olması gerekir.")
        print()
    else:
        print()
        print("❌ İşlem başarısız oldu. Kontrol et ve tekrar dene.")

# ============================================
# PROGRAMI BAŞLAT
# ============================================
if __name__ == "__main__":
    main()