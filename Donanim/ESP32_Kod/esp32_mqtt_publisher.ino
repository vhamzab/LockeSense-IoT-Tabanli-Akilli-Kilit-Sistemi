#include <WiFi.h>
#include <PubSubClient.h>

// --- AYARLARINIZI BURADAN GİRİN ---
// Wi-Fi Bilgileri
const char* ssid = "deneme";
const char* password = "tavadahamsi";

// MQTT Broker (Sunucu) Bilgileri
const char* mqtt_server = "broker.hivemq.com"; // Örnek genel broker
const int mqtt_port = 1883;

// MQTT Konusu (Topic) - Bu isim hem ESP32 hem de PC'de aynı OLMALIDIR
const char* mqtt_topic = "/pc_kilit/status"; 
// ------------------------------------

WiFiClient espClient;
PubSubClient client(espClient);
long lastMsg = 0; // Son mesaj gönderme zamanı

void setup_wifi() {
  delay(10);
  Serial.println();
  Serial.print("Wi-Fi Ağına Bağlanılıyor: ");
  Serial.println(ssid);

  WiFi.begin(ssid, password);

  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.print(".");
  }

  Serial.println("\nWi-Fi Bağlantısı Başarılı!");
  Serial.print("IP Adresi: ");
  Serial.println(WiFi.localIP());
}

void reconnect() {
  // Bağlantı koparsa yeniden bağlanmayı dene
  while (!client.connected()) {
    Serial.print("MQTT Broker'a bağlanılıyor...");
    
    // Rastgele bir Client ID kullanın
    String clientId = "ESP32_PC_KILIT-";
    clientId += String(random(0xffff), HEX);
    
    // Bağlanmayı dene
    if (client.connect(clientId.c_str())) {
      Serial.println("Bağlandı.");
    } else {
      Serial.print("Bağlanma Başarısız, rc=");
      Serial.print(client.state());
      Serial.println(". 5 saniye bekle.");
      delay(5000);
    }
  }
}

void setup() {
  Serial.begin(115200);
  setup_wifi();
  client.setServer(mqtt_server, mqtt_port);
}

void loop() {
  if (!client.connected()) {
    reconnect();
  }
  client.loop(); // MQTT mesajlaşma trafiğini yönetir

  long now = millis();
  // Her 3 saniyede bir mesaj yayınla
  if (now - lastMsg > 3000) { 
    lastMsg = now;
    
    // Gönderilecek mesaj: PC'ye kartın aktif olduğunu bildirir
    const char* payload = "MEVCUT"; 
    
    // Mesajı yayınla
    client.publish(mqtt_topic, payload);
    Serial.print("MQTT Mesajı Yayınlandı: ");
    Serial.println(payload);
  }
}