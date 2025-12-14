import paho.mqtt.client as mqtt
import time
import ctypes
import win32api
import os
from dotenv import load_dotenv

# .env dosyasından ortam değişkenlerini yükle
load_dotenv()

# --- AYARLARINIZI .env DOSYASINDAN YÜKLEYİN ---
# MQTT Broker Bilgileri (ESP32 koduyla aynı olmalı)
MQTT_SERVER = os.getenv("MQTT_SERVER", "broker.hivemq.com")
MQTT_PORT = int(os.getenv("MQTT_PORT", "1883"))
MQTT_TOPIC = os.getenv("MQTT_TOPIC", "/pc_kilit/status")

# KİLİTLEME MANTIĞI EŞİKLERİ
# Son mesajın üzerinden kaç saniye geçerse kilitlenecek.
# (ESP32 3 saniyede bir mesaj gönderdiği için 5-7 saniye güvenilir bir aralıktır.)
LOCK_TIMEOUT_SECONDS = int(os.getenv("LOCK_TIMEOUT_SECONDS", "7")) 

# Sistem Durum Takibi
last_message_time = time.time()
is_pc_locked = False
# ------------------------------------

def lock_pc():
    """Windows kilit komutu (ctypes kullanarak alternatif çözüm)."""
    global is_pc_locked
    if not is_pc_locked:
        print("\n!!! ZAMAN AŞIMI: Cihaz yok. Bilgisayar Kilitleniyor... (Alternatif Komut)")
        
        # Windows API fonksiyonunu doğrudan çağırır
        ctypes.windll.user32.LockWorkStation()
        
        is_pc_locked = True

def unlock_pc():
    """Kilit Açma Bölgesine Girildi (Manuel Açma Gerekir)."""
    global is_pc_locked
    if is_pc_locked:
        # Not: Güvenlik nedeniyle Python otomatik olarak şifre/parola yazamaz.
        # Bu, sadece kilit ekranından çıktıktan sonra konsola bilgi mesajıdır.
        print("\n*** CİHAZ GÖRÜNDÜ: Kilit Açma Alanına Girildi. ***")
        is_pc_locked = False

# MQTT Geri Çağrı Fonksiyonları
def on_connect(client, userdata, flags, rc):
    """Broker'a başarılı bağlantı kurulduğunda çağrılır."""
    print(f"MQTT Broker'a Bağlandı. Sonuç kodu: {rc}")
    # Bağlantı kurulur kurulmaz konuya abone ol
    client.subscribe(MQTT_TOPIC)
    print(f"'{MQTT_TOPIC}' konusuna abone olundu.")

def on_message(client, userdata, msg):
    """Abone olunan konuya mesaj geldiğinde çağrılır."""
    global last_message_time, is_pc_locked
    
    payload = msg.payload.decode()
    
    if payload == "MEVCUT":
        # Yeni mesaj geldi, zamanı güncelle
        last_message_time = time.time()
        
        # Eğer kilitliysek ve mesaj geldiyse, kilit açma bölgesine girdik
        if is_pc_locked:
            unlock_pc()

        # Konsolda durumu göster
        print(f"-> Gelen Mesaj: {payload} | Durum: UNLOCKED", end='\r')


def main():
    global is_pc_locked, last_message_time
    
    client = mqtt.Client()
    client.on_connect = on_connect
    client.on_message = on_message
    
    # Broker'a bağlan
    try:
        client.connect(MQTT_SERVER, MQTT_PORT, 60)
    except Exception as e:
        print(f"MQTT Bağlantı Hatası: {e}")
        return

    # MQTT dinleme döngüsünü arka planda başlat
    client.loop_start()

    print("\n--- Akıllı PC Kilidi Yöneticisi Başlatıldı ---")
    print(f"Hedef Broker: {MQTT_SERVER}")
    print(f"İzleme Konusu: {MQTT_TOPIC}")
    print(f"Kilit Zaman Aşımı: {LOCK_TIMEOUT_SECONDS} saniye")
    print("------------------------------------------")

    # Ana kilit kontrol döngüsü
    while True:
        time_since_last_message = time.time() - last_message_time
        
        if time_since_last_message > LOCK_TIMEOUT_SECONDS:
            # Zaman aşımı gerçekleşti, kilit komutunu gönder
            lock_pc()
        
        time.sleep(1) # Her saniye kontrol et

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nProgram kullanıcı tarafından sonlandırıldı.")
    except Exception as e:
        print(f"Kritik Hata: {e}")