# Görsel Dosyaları Listesi

Bu dosya, projede kullanılması gereken görsellerin listesini ve durumlarını içerir.

---

## ✅ Görsel Dosyaları ve Durumları

### MVP Fotoğrafları

| # | Dosya Adı | Açıklama | Durum | Öncelik |
|---|-----------|----------|-------|---------|
| 01 | `01_mvp_sistem_calisma_hali.jpg` | ESP32 ve laptop birlikte çalışırken | ✅ Tamamlandı | 🔴 Yüksek |
| 02 | `02_esp32_laptop_yakindan.jpg` | ESP32 yakın çekim görüntüsü | ⏳ Bekleniyor | 🟡 Orta |

### Ekran Görüntüleri

| # | Dosya Adı | Açıklama | Durum | Öncelik |
|---|-----------|----------|-------|---------|
| 03 | `03_python_script_cikti.jpg` | Python script konsol çıktısı | ✅ Tamamlandı | 🔴 Yüksek |
| 04 | `04_python_script_kilit_islemi.jpg` | PC kilitleme işlemi çıktısı | ✅ Tamamlandı | 🟡 Orta |
| 05 | `05_arduino_ide_serial_monitor.jpg` | Arduino Serial Monitor çıktısı | ✅ Tamamlandı | 🔴 Yüksek |
| 06 | `06_arduino_ide_kod_ekrani.png` | Arduino IDE kod ekranı | ⏳ Bekleniyor | 🟢 Düşük |

### Diyagramlar ve Şemalar

| # | Dosya Adı | Açıklama | Durum | Öncelik |
|---|-----------|----------|-------|---------|
| 07 | `07_sistem_akis_semasi.jpg` | Sistem akış şeması | ✅ Tamamlandı | 🔴 Yüksek |
| 07 | `07_sistem_akis_semasi.svg` | Sistem akış şeması (SVG) | ⏳ Bekleniyor | 🟡 Orta |
| 08 | `08_sistem_mantigi_diyagrami.png` | Sistem mantığı diyagramı | ⏳ Bekleniyor | 🟡 Orta |

### Donanım Şemaları

| # | Dosya Adı | Açıklama | Durum | Öncelik |
|---|-----------|----------|-------|---------|
| 09 | `09_esp32_baglantı_semasi.png` | ESP32 bağlantı şeması | ⏳ Bekleniyor | 🟢 Düşük |
| 09 | `09_esp32_baglantı_semasi.fzz` | Fritzing dosyası | ⏳ Bekleniyor | 🟢 Düşük |

---

## 📊 Durum Göstergeleri

- ✅ **Tamamlandı**: Görsel eklendi ve kullanıma hazır
- ⏳ **Bekleniyor**: Görsel henüz eklenmedi
- 🔄 **Güncelleniyor**: Görsel üzerinde çalışılıyor
- ❌ **İptal Edildi**: Görsel eklenmeyecek

## 🎯 Öncelik Seviyeleri

- 🔴 **Yüksek**: Ana README.md'de kullanılacak, zorunlu görseller
- 🟡 **Orta**: Dokümantasyonda kullanılacak, önerilen görseller
- 🟢 **Düşük**: İsteğe bağlı, ek bilgi için görseller

---

## 📝 Görsel İçerik Detayları

### 01_mvp_sistem_calisma_hali.jpg
**Görülecekler**:
- ESP32 DevKit V1 cihazı laptop klavyesi üzerinde
- Yeşil LED'ler yanık
- USB kablosu bağlı
- Laptop ekranında Arduino IDE ve Python script çıktısı
- Sistem aktif ve çalışır durumda

**Çekim İpuçları**:
- İyi aydınlatma kullanın
- LED'lerin görünür olduğundan emin olun
- Ekran görüntüsü net olmalı
- Yüksek çözünürlükte çekin (1920x1080+)

### 03_python_script_cikti.png
**Görülecekler**:
```
--- Akıllı PC Kilidi Yöneticisi Başlatıldı ---
Hedef Broker: broker.hivemq.com
İzleme Konusu: /pc_kilit/status
Kilit Zaman Aşımı: 7 saniye
------------------------------------------
MQTT Broker'a Bağlandı. Sonuç kodu: 0
'/pc_kilit/status' konusuna abone olundu.
-> Gelen Mesaj: MEVCUT | Durum: UNLOCKED
```

**Ekran Görüntüsü Alma**:
- Windows: `Win + Shift + S`
- Terminal penceresini tam ekran gösterin
- Temiz bir arka plan kullanın

### 05_arduino_ide_serial_monitor.png
**Görülecekler**:
```
Wi-Fi Bağlantısı Başarılı!
IP Adresi: 192.168.1.XXX
MQTT Broker'a bağlanılıyor...Bağlandı.
MQTT Mesajı Yayınlandı: MEVCUT
MQTT Mesajı Yayınlandı: MEVCUT
...
```

**Ekran Görüntüsü Alma**:
- Arduino IDE Serial Monitor sekmesi açık
- Baud rate: 115200 görünür olmalı
- Mesajlar tekrarlanıyor olmalı

### 07_sistem_akis_semasi.png/svg
**Görülecekler**:
- ESP32 Mikrodenetleyici (sol)
- HiveMQ MQTT Broker (orta, bulut şeklinde)
- Python Script (sağ)
- Akış okları ve etiketler
- Karar mekanizması (Sinyal Var/Yok)
- Windows Lock çıktısı

**Oluşturma**:
- Draw.io veya benzeri araç kullanın
- Vektör formatında (SVG) kaydedin
- PNG olarak da export edin
- Renkli ve anlaşılır olmalı

---

## 🔄 Güncelleme Notları

- **2025-12-14**: Görsel listesi oluşturuldu
- Görseller eklendikçe bu dosya güncellenecek

---

## 📌 Notlar

- Tüm görseller `Dokumantasyon/Gorseller/` klasöründe olmalıdır
- Dosya isimlendirme şablonuna uyulmalıdır
- Görseller eklendikten sonra ana README.md güncellenmelidir
- Kişisel bilgi veya hassas veri içermemelidir

