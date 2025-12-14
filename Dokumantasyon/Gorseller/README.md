# Görseller ve Medya Dosyaları

Bu klasör, LockeSense projesinin görsel dokümantasyonunu içermektedir.

---

## 📸 Görsel Dosyaları

### 1. MVP (Minimum Viable Product) Fotoğrafları

#### `01_mvp_sistem_calisma_hali.jpg` / `01_mvp_sistem_calisma_hali.png`
**Açıklama**: Sistemin çalışır halini gösteren ana MVP fotoğrafı
- ESP32 DevKit V1 cihazının laptop üzerinde çalışır durumda görüntüsü
- Arduino IDE ve Python script'inin aynı anda çalıştığı ekran görüntüsü
- Yeşil LED'lerin yanık olduğu, sistemin aktif olduğunu gösteren görsel
- **Kullanım**: Ana README.md'de demo bölümünde kullanılır
- **Boyut Önerisi**: 1920x1080 veya daha yüksek çözünürlük
- **Format**: JPG (küçük dosya) veya PNG (yüksek kalite)

#### `02_esp32_laptop_yakindan.jpg` / `02_esp32_laptop_yakindan.png`
**Açıklama**: ESP32 cihazının laptop klavyesi üzerindeki yakın çekim görüntüsü
- Cihazın fiziksel yerleşimi
- USB kablosu bağlantısı
- LED durumları
- **Kullanım**: Donanım dokümantasyonunda kullanılır

---

### 2. Ekran Görüntüleri (Screenshots)

#### `03_python_script_cikti.png`
**Açıklama**: Python script'inin çalışırken konsol çıktısı
- "Akıllı PC Kilidi Yöneticisi Başlatıldı" mesajı
- MQTT broker bağlantı durumu
- Mesaj alma ve kilitleme işlemleri
- **İçerik**:
  ```
  --- Akıllı PC Kilidi Yöneticisi Başlatıldı ---
  Hedef Broker: broker.hivemq.com
  İzleme Konusu: /pc_kilit/status
  Kilit Zaman Aşımı: 7 saniye
  MQTT Broker'a Bağlandı. Sonuç kodu: 0
  '/pc_kilit/status' konusuna abone olundu.
  -> Gelen Mesaj: MEVCUT | Durum: UNLOCKED
  ```
- **Kullanım**: Yazılım dokümantasyonunda örnek çıktı olarak

#### `04_python_script_kilit_islemi.png`
**Açıklama**: PC kilitleme işleminin gerçekleştiği anın ekran görüntüsü
- Zaman aşımı mesajı
- Kilitleme komutu çıktısı
- Cihaz tekrar algılandığında kilit açma mesajı
- **İçerik**:
  ```
  !!! ZAMAN AŞIMI: Cihaz yok. Bilgisayar Kilitleniyor...
  *** CİHAZ GÖRÜNDÜ: Kilit Açma Alanına Girildi. ***
  ```
- **Kullanım**: Sistem davranışını göstermek için

#### `05_arduino_ide_serial_monitor.png`
**Açıklama**: Arduino IDE Serial Monitor çıktısı
- ESP32'nin Wi-Fi bağlantı durumu
- IP adresi bilgisi
- MQTT broker bağlantı durumu
- "MQTT Mesajı Yayınlandı: MEVCUT" mesajlarının tekrarı
- **İçerik**:
  ```
  Wi-Fi Bağlantısı Başarılı!
  IP Adresi: 192.168.33.167
  MQTT Broker'a bağlanılıyor...Bağlandı.
  MQTT Mesajı Yayınlandı: MEVCUT
  ```
- **Kullanım**: Donanım dokümantasyonunda ESP32 çıktısı örneği

#### `06_arduino_ide_kod_ekrani.png`
**Açıklama**: Arduino IDE'de açık kod dosyası ve Serial Monitor
- `esp32_mqtt_publisher.ino` dosyasının kod görünümü
- Serial Monitor sekmesi aktif
- Board bilgisi: "DOIT ESP32 DEVKIT V1"
- **Kullanım**: Kurulum dokümantasyonunda IDE görünümü

---

### 3. Diyagramlar ve Şemalar

#### `07_sistem_akis_semasi.png` / `07_sistem_akis_semasi.svg`
**Açıklama**: Sistemin teknik mimarisini gösteren akış şeması
- ESP32 → MQTT Broker → Python Script akışı
- Karar mekanizması (Sinyal Var/Yok)
- Kilitleme mantığı
- **İçerik Bileşenleri**:
  - Giriş: ESP32 Mikrodenetleyici
  - İletişim: HiveMQ MQTT Broker
  - İşleme: Python Script
  - Çıktı: Windows Lock/Unlock
- **Kullanım**: Ana README.md'de teknik mimari bölümünde
- **Format**: PNG (bitmap) veya SVG (vektör, önerilen)

#### `08_sistem_mantigi_diyagrami.png`
**Açıklama**: Sistem mantığını gösteren basitleştirilmiş diyagram
- Sinyal algılama durumu
- 7 saniye zaman aşımı mantığı
- Kilitleme karar akışı
- **Kullanım**: Sunumlarda ve hızlı açıklamalarda

---

### 4. Devre Şemaları (Donanım)

#### `09_esp32_baglantı_semasi.png` / `09_esp32_baglantı_semasi.fzz`
**Açıklama**: ESP32'nin bağlantı şeması
- USB bağlantısı
- Güç bağlantıları
- Harici bileşen bağlantıları (varsa)
- **Format**: PNG (görsel) ve FZZ (Fritzing dosyası)
- **Kullanım**: Donanım dokümantasyonunda

---

## 📋 Dosya İsimlendirme Şablonu

Görselleri yüklerken aşağıdaki isimlendirme şablonunu kullanın:

```
[numara]_[kategori]_[açıklama].[uzantı]
```

**Örnekler**:
- `01_mvp_sistem_calisma_hali.jpg`
- `03_python_script_cikti.png`
- `07_sistem_akis_semasi.svg`

**Kategoriler**:
- `mvp` - MVP fotoğrafları
- `screenshot` - Ekran görüntüleri
- `diagram` - Diyagramlar ve şemalar
- `hardware` - Donanım görselleri
- `demo` - Demo görselleri

---

## 🎨 Görsel Gereksinimleri

### Çözünürlük
- **MVP Fotoğrafları**: Minimum 1920x1080 (Full HD)
- **Ekran Görüntüleri**: Orijinal ekran çözünürlüğü
- **Diyagramlar**: Minimum 1200x800 (vektör formatı önerilir)

### Format
- **Fotoğraflar**: JPG (küçük dosya) veya PNG (yüksek kalite)
- **Ekran Görüntüleri**: PNG (kayıpsız)
- **Diyagramlar**: SVG (vektör, önerilen) veya PNG (yüksek çözünürlük)
- **Fritzing Dosyaları**: FZZ

### Dosya Boyutu
- **JPG**: Maksimum 2 MB
- **PNG**: Maksimum 5 MB
- **SVG**: Maksimum 1 MB

---

## 📝 Görselleri README.md'ye Ekleme

Ana README.md dosyasında görselleri şu şekilde ekleyin:

```markdown
## 📸 Demo

![Sistem Çalışma Hali](Dokumantasyon/Gorseller/01_mvp_sistem_calisma_hali.jpg)

*ESP32 cihazı ve Python script'inin birlikte çalıştığı görüntü*

### Python Script Çıktısı
![Python Script](Dokumantasyon/Gorseller/03_python_script_cikti.png)

### Arduino Serial Monitor
![Arduino Serial Monitor](Dokumantasyon/Gorseller/05_arduino_ide_serial_monitor.png)
```

---

## 🔄 Görsel Güncelleme Kontrol Listesi

Yeni görsel eklerken:

- [ ] Dosya adı şablona uygun mu?
- [ ] Çözünürlük yeterli mi?
- [ ] Format uygun mu?
- [ ] Dosya boyutu makul mü?
- [ ] README.md'ye link eklendi mi?
- [ ] Alt yazı/açıklama eklendi mi?

---

## 📚 Kullanım Senaryoları

### 1. GitHub README
- MVP fotoğrafı ana sayfada
- Ekran görüntüleri ilgili bölümlerde
- Diyagramlar teknik mimari bölümünde

### 2. Sunumlar
- MVP fotoğrafı giriş slaydında
- Sistem akış şeması mimari slaydında
- Ekran görüntüleri demo slaydında

### 3. Dokümantasyon
- Donanım görselleri → `Donanim/README_DONANIM.md`
- Yazılım görselleri → `Yazilim/README_YAZILIM.md`
- Genel görseller → Ana `README.md`

---

## 🛠️ Görsel Düzenleme Araçları Önerileri

- **Fotoğraf Düzenleme**: GIMP, Photoshop, Paint.NET
- **Ekran Görüntüsü**: Windows Snipping Tool, ShareX, Greenshot
- **Diyagram**: Draw.io, Lucidchart, Mermaid (kod tabanlı)
- **Fritzing**: Fritzing (devre şemaları için)

---

## 📌 Notlar

- Tüm görseller projenin açık kaynak lisansı (MIT) altındadır
- Görsellerde kişisel bilgi veya hassas veri bulunmamalıdır
- Ekran görüntülerinde Wi-Fi şifreleri veya API anahtarları görünmemelidir
- Görselleri eklerken `.gitignore` dosyasını kontrol edin (büyük dosyalar için Git LFS kullanılabilir)

---

## 🔗 İlgili Dosyalar

- [Ana README.md](../../README.md)
- [Donanım README](../../Donanim/README_DONANIM.md)
- [Yazılım README](../../Yazilim/README_YAZILIM.md)

