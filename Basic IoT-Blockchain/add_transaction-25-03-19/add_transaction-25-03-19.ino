#include <ESP8266HTTPClient.h>
#include <ESP8266WiFi.h>
#include <ArduinoJson.h>
#include <NTPClient.h>
#include <WiFiUdp.h>




WiFiUDP ntpUDP;
NTPClient timeClient(ntpUDP, "time.nist.gov", 0, 1000);



void setup() {

  Serial.begin(115200);
  Serial.println("Waiting for connection");
  WiFi.begin("Prakhar PC", "12345611");

  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.println("Waiting for connection");

  }
  timeClient.begin();
}

void loop() {
  timeClient.update();
  if (WiFi.status() == WL_CONNECTED) {
    if (long(timeClient.getEpochTime()) > 1553447876) {
      timeClient.update();

      StaticJsonBuffer<250> jsonBuffer;
      JsonObject& root = jsonBuffer.createObject();
      JsonArray& sensors = root.createNestedArray("sensors");
      JsonObject& sensor_one = jsonBuffer.createObject();
      JsonObject& sensor_two = jsonBuffer.createObject();

      root["factoryID"] = "1234";
      root["factoryName"] = "ABCD";
      root["timestamp"] = timeClient.getEpochTime();
      sensor_one["type"] = "Gas";
      sensor_one["name"] = "CO2";
      sensor_one["value"] = random(1, 15);
      sensors.add(sensor_one);
      sensor_two["type"] = "Light";
      sensor_two["name"] = "Lux";
      sensor_two["value"] = random(30, 50);
      sensors.add(sensor_two);

      char JSONmessageBuffer[300];
      root.prettyPrintTo(JSONmessageBuffer, sizeof(JSONmessageBuffer));
      Serial.println(JSONmessageBuffer);
      root.prettyPrintTo(Serial);
      Serial.println();
      HTTPClient http;
      http.begin("http://192.168.137.1:5001/add_transaction");
      http.addHeader("Content-Type", "application/json");
      int httpCode = http.POST(JSONmessageBuffer);
      String payload = http.getString();
      Serial.println(httpCode);
      Serial.println(payload);
      http.end();
    }
    else
    {
      Serial.print("Unix Time : ");
      Serial.println(timeClient.getEpochTime());
    }
  } else
  {
    Serial.println("Error in WiFi connection");
  }
  delay(2000);
}
