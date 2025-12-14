# Donanım Dokümantasyonu

## 📋 Genel Bakış

Bu klasör, LockeSense sisteminin donanım bileşenlerini içermektedir. ESP32 mikrodenetleyicisi, Wi-Fi üzerinden MQTT protokolü ile PC ile iletişim kurar.

---

## 🔧 Gereksinimler

### Donanım
- **ESP32 DevKit V1** (veya uyumlu model)
  - ESP32-WROOM-32 veya ESP32-WROOM-32D
  - Micro-USB kablosu (programlama ve güç için)
- **Wi-Fi Erişimi**: ESP32'nin bağlanabileceği bir Wi-Fi ağı

### Yazılım
- **Arduino IDE** (2.0 veya üzeri önerilir)
- **ESP32 Board Desteği** (Arduino IDE'ye eklenecek)

---

## 📦 Arduino IDE Kurulumu

### Adım 1: Arduino IDE İndirme ve Kurulum

1. [Arduino IDE](https://www.arduino.cc/en/software) adresinden Arduino IDE'yi indirin
2. Kurulumu tamamlayın

### Adım 2: ESP32 Board Desteğini Ekleme

1. Arduino IDE'yi açın
2. **File → Preferences** (veya `Ctrl + ,`) menüsüne gidin
3. **Additional Board Manager URLs** alanına şu URL'yi ekleyin:
   ```
   https://raw.githubusercontent.com/espressif/arduino-esp32/gh-pages/package_esp32_index.json
   ```
   Eğer birden fazla URL varsa, virgülle ayırın.

4. **Tools → Board → Boards Manager** menüsüne gidin
5. Arama kutusuna `esp32` yazın
6. **"esp32 by Espressif Systems"** paketini bulun ve **Install** butonuna tıklayın
7. Kurulum tamamlanana kadar bekleyin (birkaç dakika sürebilir)

### Adım 3: Gerekli Kütüphaneleri Yükleme

1. **Tools → Manage Libraries** menüsüne gidin
2. Aşağıdaki kütüphaneleri arayıp yükleyin:
   - **PubSubClient** (Nick O'Leary tarafından)
     - MQTT protokolü için gerekli
     - Versiyon: 2.8.0 veya üzeri

### Adım 4: Board ve Port Ayarları

1. **Tools → Board** menüsünden **"ESP32 Arduino"** altından **"DOIT ESP32 DEVKIT V1"** seçin
   - Veya kullandığınız ESP32 modeline uygun board'u seçin

2. **Tools → Port** menüsünden ESP32'nin bağlı olduğu COM portunu seçin
   - Windows'ta: `COM3`, `COM4` gibi
   - Port görünmüyorsa: **Device Manager**'da **Ports (COM & LPT)** altında kontrol edin

3. Diğer önemli ayarlar:
   - **Upload Speed**: `115200` (veya `921600` daha hızlı yükleme için)
   - **CPU Frequency**: `240MHz (WiFi/BT)`
   - **Flash Frequency**: `80MHz`
   - **Flash Size**: `4MB (32Mb)`
   - **Partition Scheme**: `Default 4MB with spiffs`
   - **Core Debug Level**: `None` (veya `Info` debug için)

---

## 🔌 Pin Kullanımı

### Bu Projede Kullanılan Pinler

**Harici Pin Kullanımı Yok**: Bu proje sadece ESP32'nin dahili Wi-Fi modülünü kullanır. Harici sensör veya aktüatör bağlantısı gerektirmez.

### ESP32 DevKit V1 Pin Yapısı

ESP32 DevKit V1'de önemli pinler:
- **3.3V**: Güç kaynağı (3.3V)
- **GND**: Toprak (Ground)
- **5V**: USB'den gelen 5V (sadece USB bağlantısı varsa)
- **EN**: Enable pin (Reset butonu)
- **GPIO Pins**: Genel amaçlı giriş/çıkış pinleri (bu projede kullanılmıyor)

### Gelecek Geliştirmeler İçin Pin Önerileri

Eğer gelecekte ek özellikler eklemek isterseniz:
- **GPIO 2**: LED göstergesi için
- **GPIO 4**: Buton girişi için
- **GPIO 5**: Buzzer için
- **GPIO 12-19**: SPI/I2C sensörler için

---

## 💻 Kod Yükleme

### Adım 1: Kodu Açma

1. Arduino IDE'yi açın
2. **File → Open** menüsünden `ESP32_Kod/esp32_mqtt_publisher.ino` dosyasını açın

### Adım 2: Hassas Bilgileri Yapılandırma (GÜVENLİK)

⚠️ **ÖNEMLİ**: Hassas bilgiler (Wi-Fi şifresi, MQTT ayarları) artık `secrets.h` dosyasında saklanmaktadır.

1. `secrets.h.example` dosyasını kopyalayın
2. `secrets.h` olarak kaydedin (aynı klasörde)
3. Kendi bilgilerinizi girin:

```cpp
// Wi-Fi Bilgileri
const char* ssid = "WIFI_AG_ADINIZ";        // Wi-Fi ağ adınız
const char* password = "WIFI_SIFRENIZ";     // Wi-Fi şifreniz

// MQTT Broker (Sunucu) Bilgileri
const char* mqtt_server = "broker.hivemq.com";  // Broker adresi
const int mqtt_port = 1883;                      // Port numarası
const char* mqtt_topic = "/pc_kilit/status";      // Topic (Python ile aynı olmalı)
```

**Güvenlik Notu**: `secrets.h` dosyası `.gitignore` ile korunur ve GitHub'a yüklenmez. Sadece yerel olarak kullanılır.

### Adım 3: MQTT Broker Ayarlarını Kontrol Etme

MQTT broker bilgilerinin Python scripti ile aynı olduğundan emin olun (her ikisi de `secrets.h` ve `.env` dosyalarında tanımlı olmalıdır).

### Adım 4: Kodu Yükleme

1. ESP32'yi bilgisayarınıza USB kablosu ile bağlayın
2. Doğru board ve port seçildiğinden emin olun
3. **Sketch → Upload** (veya `Ctrl + U`) ile kodu yükleyin
4. Yükleme sırasında ESP32'deki **BOOT** butonuna basmanız gerekebilir
5. Yükleme tamamlandığında "Done uploading" mesajını göreceksiniz

---

## 🔍 Serial Monitor ile Test

### Serial Monitor'ü Açma

1. **Tools → Serial Monitor** (veya `Ctrl + Shift + M`)
2. **Baud Rate**'i **115200** olarak ayarlayın (sağ alt köşede)

### Beklenen Çıktı

Başarılı bir bağlantıda şu mesajları görmelisiniz:

```
Wi-Fi Ağına Bağlanılıyor: WIFI_AG_ADINIZ
.....
Wi-Fi Bağlantısı Başarılı!
IP Adresi: 192.168.1.XXX
MQTT Broker'a bağlanılıyor...Bağlandı.
MQTT Mesajı Yayınlandı: MEVCUT
MQTT Mesajı Yayınlandı: MEVCUT
MQTT Mesajı Yayınlandı: MEVCUT
...
```

Her 3 saniyede bir "MEVCUT" mesajı gönderilmelidir.

---

## ⚙️ Yapılandırma Seçenekleri

### Mesaj Gönderme Sıklığı

Kod içinde mesaj gönderme aralığını değiştirebilirsiniz:

```cpp
// Her 3 saniyede bir mesaj yayınla
if (now - lastMsg > 3000) {  // 3000 = 3 saniye (milisaniye cinsinden)
```

- **Daha sık mesaj**: `2000` (2 saniye) - Daha hızlı tepki, daha fazla güç tüketimi
- **Varsayılan**: `3000` (3 saniye) - Dengeli
- **Daha seyrek mesaj**: `5000` (5 saniye) - Daha az güç tüketimi, daha yavaş tepki

⚠️ **Not**: Python scriptindeki `LOCK_TIMEOUT_SECONDS` değerini de buna göre ayarlayın.

### Client ID Özelleştirme

MQTT client ID'yi özelleştirebilirsiniz:

```cpp
String clientId = "ESP32_PC_KILIT-";  // Özel bir isim ekleyebilirsiniz
clientId += String(random(0xffff), HEX);
```

---

## 🔋 Güç Yönetimi

### USB Güç

- ESP32, USB kablosu üzerinden güç alır
- Çoğu USB portu yeterli gücü sağlar (500mA)
- Taşınabilir kullanım için power bank kullanılabilir

### Batarya ile Çalıştırma (İleri Seviye)

ESP32'yi batarya ile çalıştırmak için:
- 3.7V Li-Po batarya kullanın
- Batarya yönetim modülü (BMS) ekleyin
- Deep sleep modu ekleyerek güç tüketimini azaltın

---

## 🔍 Sorun Giderme

### "Board not found" Hatası

**Çözüm**: ESP32 board desteğini yüklediğinizden emin olun (yukarıdaki Adım 2).

### "Failed to connect to ESP32" Hatası

**Çözümler**:
1. USB kablosunu değiştirin (veri aktarımı yapabilen bir kablo olmalı)
2. USB portunu değiştirin
3. ESP32'deki **BOOT** butonuna basılı tutarak yükleme yapmayı deneyin
4. **Tools → Erase Flash** ile flash'ı temizleyin

### Wi-Fi Bağlantı Sorunu

**Kontrol Listesi**:
- ✅ SSID ve şifre doğru mu?
- ✅ Wi-Fi ağı 2.4GHz mi? (ESP32 5GHz desteklemez)
- ✅ Wi-Fi sinyal gücü yeterli mi?
- ✅ WPA2/WPA3 şifreleme kullanılıyor mu? (WEP desteklenmez)

### MQTT Bağlantı Sorunu

**Kontrol Listesi**:
- ✅ İnternet bağlantısı var mı?
- ✅ Broker adresi doğru mu?
- ✅ Port numarası doğru mu? (1883 genellikle varsayılandır)
- ✅ Firewall MQTT trafiğini engelliyor mu?

### Serial Monitor'de Hiçbir Şey Görünmüyor

**Çözümler**:
1. Baud rate'in 115200 olduğundan emin olun
2. Doğru COM portunu seçtiğinizden emin olun
3. ESP32'yi resetleyin (RST butonuna basın)
4. Serial Monitor'ü kapatıp tekrar açın

---

## 📁 Dosya Yapısı

```
Donanim/
├── ESP32_Kod/
│   └── esp32_mqtt_publisher.ino    # Ana Arduino kodu
└── README_DONANIM.md               # Bu dosya
```

**Not**: Bu projede ESP32 sadece USB kablosu ile bağlanır, harici devre şeması gerektirmez.

---

## 🔐 Güvenlik Notları

1. **Wi-Fi Şifreleri**: Kod içinde Wi-Fi şifreleri düz metin olarak saklanır. Üretim ortamlarında güvenli saklama yöntemleri kullanın.

2. **MQTT Broker**: Genel broker'lar (HiveMQ) test amaçlıdır. Üretim için kendi broker'ınızı kullanın.

3. **Topic İsimleri**: Özel ve benzersiz topic isimleri kullanın.

---

## 📝 Lisans

Bu donanım dokümantasyonu, ana proje lisansı (MIT) altında lisanslanmıştır.

---

## 💡 İpuçları

- **İlk Kurulum**: İlk kez yüklerken ESP32'deki **BOOT** butonuna basmanız gerekebilir
- **Hızlı Yükleme**: Upload speed'i `921600` yaparak yükleme süresini kısaltabilirsiniz
- **Debug**: Serial Monitor'ü açık tutarak sistem durumunu izleyebilirsiniz
- **Reset**: ESP32'yi resetlemek için **RST** butonuna basın veya USB'yi çıkarıp takın

---

## 🚀 Gelecek Geliştirmeler

- [ ] Deep sleep modu ile güç tüketimini azaltma
- [ ] LED göstergesi ekleme (bağlantı durumu için)
- [ ] Buton ile manuel reset
- [ ] OTA (Over-The-Air) güncelleme desteği
- [ ] Bluetooth Low Energy (BLE) desteği
