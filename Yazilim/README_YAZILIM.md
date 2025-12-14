# Yazılım Dokümantasyonu

## 📋 Genel Bakış

Bu klasör, LockeSense sisteminin PC tarafı yazılımını içermektedir. Python scripti, ESP32 cihazından gelen MQTT mesajlarını dinleyerek bilgisayarın otomatik olarak kilitlenmesini sağlar.

---

## 🔧 Gereksinimler

### İşletim Sistemi
- **Windows 10/11** (PC kilitleme özelliği Windows API kullanır)
- Python 3.7 veya üzeri

### Python Kütüphaneleri
- `paho-mqtt` - MQTT protokolü için
- `pywin32` - Windows API erişimi için

---

## 📦 Kurulum

### Adım 1: Python Kurulumu

1. Python'un yüklü olduğunu kontrol edin:
   ```bash
   python --version
   ```
   veya
   ```bash
   python3 --version
   ```

2. Eğer Python yüklü değilse, [python.org](https://www.python.org/downloads/) adresinden indirin.
   - ⚠️ **Önemli**: Kurulum sırasında "Add Python to PATH" seçeneğini işaretleyin.

### Adım 2: Bağımlılıkları Yükleme

1. Terminal/Command Prompt'u açın
2. Proje klasörüne gidin:
   ```bash
   cd "LockeSense\Yazilim"
   ```
3. Bağımlılıkları yükleyin:
   ```bash
   pip install -r Bagimliliklar/requirements.txt
   ```
   
   Veya manuel olarak:
   ```bash
   pip install paho-mqtt pywin32
   ```

### Adım 3: Yapılandırma

`Python_Script/mqtt_lock_manager.py` dosyasını bir metin editörü ile açın ve aşağıdaki ayarları yapın:

```python
# MQTT Broker Bilgileri (ESP32 koduyla aynı olmalı)
MQTT_SERVER = "broker.hivemq.com"  # Varsayılan genel broker
MQTT_PORT = 1883
MQTT_TOPIC = "/pc_kilit/status"    # ESP32 ile aynı topic olmalı

# Kilit Zaman Aşımı (saniye)
LOCK_TIMEOUT_SECONDS = 7  # ESP32 3 saniyede bir mesaj gönderir
```

#### MQTT Broker Seçenekleri

**Seçenek 1: Genel Broker (HiveMQ) - Varsayılan**
- Ücretsiz ve hızlı kurulum
- İnternet bağlantısı gerekir
- `broker.hivemq.com` kullanılır

**Seçenek 2: Kendi Broker'ınız**
- Daha güvenli ve özel
- Mosquitto, EMQX gibi broker'lar kullanılabilir
- Yerel ağda çalışabilir
- Örnek: `192.168.1.100` (yerel IP)

**Seçenek 3: Bulut Broker (AWS IoT, Azure IoT Hub)**
- Üretim ortamları için
- Daha fazla yapılandırma gerekir

---

## 🚀 Çalıştırma

### Normal Çalıştırma

1. Terminal/Command Prompt'u açın
2. Script klasörüne gidin:
   ```bash
   cd "LockeSense\Yazilim\Python_Script"
   ```
3. Scripti çalıştırın:
   ```bash
   python mqtt_lock_manager.py
   ```

### Arka Planda Çalıştırma (Windows)

Scripti arka planda çalıştırmak için:

1. `.bat` dosyası oluşturun (`start_lock_manager.bat`):
   ```batch
   @echo off
   cd /d "%~dp0"
   python mqtt_lock_manager.py
   pause
   ```

2. Veya Windows Task Scheduler ile otomatik başlatma yapabilirsiniz.

### Windows Başlangıçta Otomatik Çalıştırma

1. `Win + R` tuşlarına basın
2. `shell:startup` yazın ve Enter'a basın
3. Script'in kısayolunu bu klasöre kopyalayın

---

## 📊 Çıktı ve Loglar

Script çalışırken konsolda şu mesajları göreceksiniz:

### Başarılı Bağlantı
```
--- Akıllı PC Kilidi Yöneticisi Başlatıldı ---
Hedef Broker: broker.hivemq.com
İzleme Konusu: /pc_kilit/status
Kilit Zaman Aşımı: 7 saniye
------------------------------------------
MQTT Broker'a Bağlandı. Sonuç kodu: 0
'/pc_kilit/status' konusuna abone olundu.
```

### Normal Çalışma
```
-> Gelen Mesaj: MEVCUT | Durum: UNLOCKED
```

### Kilitleme
```
!!! ZAMAN AŞIMI: Cihaz yok. Bilgisayar Kilitleniyor...
```

### Kilit Açma Bölgesine Giriş
```
*** CİHAZ GÖRÜNDÜ: Kilit Açma Alanına Girildi. ***
```

---

## ⚙️ Ayarlar ve Özelleştirme

### Kilit Zaman Aşımını Değiştirme

`LOCK_TIMEOUT_SECONDS` değerini değiştirin:
- **Daha hızlı kilit**: 5 saniye (daha hassas)
- **Varsayılan**: 7 saniye (önerilen)
- **Daha yavaş kilit**: 10 saniye (daha toleranslı)

⚠️ **Not**: ESP32 3 saniyede bir mesaj gönderir. Zaman aşımı 3 saniyenin altında olmamalıdır.

### MQTT Topic Değiştirme

Topic'i değiştirmek için hem Python scriptinde hem de ESP32 kodunda aynı değeri kullanın:
```python
MQTT_TOPIC = "/pc_kilit/status"  # Özel topic kullanabilirsiniz
```

---

## 🔍 Sorun Giderme

### "ModuleNotFoundError: No module named 'paho'"

**Çözüm**: Bağımlılıkları yükleyin:
```bash
pip install -r Bagimliliklar/requirements.txt
```

### "ModuleNotFoundError: No module named 'win32api'"

**Çözüm**: pywin32'yi yükleyin:
```bash
pip install pywin32
```

### "MQTT Bağlantı Hatası"

**Olası Nedenler**:
1. İnternet bağlantısı yok
2. Broker adresi yanlış
3. Firewall engelliyor

**Çözümler**:
- İnternet bağlantınızı kontrol edin
- Broker adresini doğrulayın
- Windows Firewall'da Python'a izin verin

### "PC Kilitlenmiyor"

**Kontrol Listesi**:
- ✅ Script çalışıyor mu?
- ✅ MQTT mesajları geliyor mu? (konsol çıktısını kontrol edin)
- ✅ Windows kullanıcı hesabınız var mı? (Guest hesabı kilitleyemez)
- ✅ Windows kilitleme özelliği aktif mi?

### "Sürekli Kilitleniyor"

**Neden**: ESP32'den mesaj gelmiyor veya yanlış topic kullanılıyor.

**Çözüm**:
- ESP32'nin çalıştığını kontrol edin
- Topic'lerin aynı olduğundan emin olun
- Wi-Fi bağlantısını kontrol edin

---

## 📁 Dosya Yapısı

```
Yazilim/
├── Python_Script/
│   └── mqtt_lock_manager.py    # Ana Python scripti
├── Bagimliliklar/
│   └── requirements.txt        # Python bağımlılıkları
└── README_YAZILIM.md          # Bu dosya
```

---

## 🔐 Güvenlik Notları

1. **MQTT Broker**: Genel broker'lar (HiveMQ) üretim ortamları için uygun değildir. Hassas veriler için kendi broker'ınızı kullanın.

2. **Topic İsimleri**: Özel ve benzersiz topic isimleri kullanın (örn: `/kullanici_adi/pc_kilit/status`).

3. **Şifreleme**: Üretim ortamlarında MQTT over TLS (port 8883) kullanın.

4. **Windows Kilitleme**: Sistem seviyesi bir işlemdir. Script yönetici yetkisi gerektirmez.

---

## 📝 Lisans

Bu yazılım, ana proje lisansı (MIT) altında lisanslanmıştır.

---

## 💡 İpuçları

- Script'i test etmek için ESP32'yi kapatıp açarak kilitleme mekanizmasını test edebilirsiniz
- Konsol çıktısını bir dosyaya kaydetmek için: `python mqtt_lock_manager.py > log.txt`
- Windows'ta script'i durdurmak için `Ctrl + C` kullanın
