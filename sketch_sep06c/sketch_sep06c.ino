#include <Adafruit_NeoPixel.h>

// =========================
// Encoder
// =========================
#define ENC_A   32
#define ENC_B   35
#define ENC_BTN 15

int lastA;
bool lastButton = HIGH;

// =========================
// LEDs
// =========================
#define LED_PIN 13
#define LED_COUNT 2

Adafruit_NeoPixel leds(
  LED_COUNT,
  LED_PIN,
  NEO_GRBW + NEO_KHZ800
);

// =========================
// LEDs ausschalten
// =========================
void ledsOff() {
  leds.clear();
  leds.show();
}

// =========================
// Farbe anzeigen
// =========================

void setBothLeds(uint32_t color) {
  leds.setPixelColor(0, color);
  leds.setPixelColor(1, color);
  leds.show();
}

void showColor(String color) {

  leds.clear();

  if (color == "RED") {
   setBothLeds(leds.Color(50, 0, 0, 0));
  }

  else if (color == "GREEN") {
    setBothLeds(leds.Color(0, 50, 0, 0));
  }

  else if (color == "BLUE") {
    setBothLeds(leds.Color(0, 0, 50, 0));
  }

  else if (color == "YELLOW") {
    setBothLeds(leds.Color(50, 50, 0, 0));
  }

  else if (color == "OFF") {
    ledsOff();
    return;
  }

  leds.show();
}

// =========================
// Setup
// =========================
void setup() {

  Serial.begin(115200);

  // Encoder
  pinMode(ENC_A, INPUT_PULLUP);

  // GPIO35 hat beim ESP32 keinen internen Pullup
  pinMode(ENC_B, INPUT);

  pinMode(ENC_BTN, INPUT_PULLUP);

  lastA = digitalRead(ENC_A);

  // LEDs
  leds.begin();
  leds.clear();
  leds.show();

  Serial.println("READY");
}

// =========================
// Loop
// =========================
void loop() {

  // -------------------------
  // Encoder drehen
  // -------------------------
  int currentA = digitalRead(ENC_A);

  if (currentA != lastA) {

    if (currentA == LOW) {

      if (digitalRead(ENC_B) != currentA) {
        Serial.println("RIGHT");
      }
      else {
        Serial.println("LEFT");
      }
    }
  }

  lastA = currentA;

  // -------------------------
  // Encoder drücken
  // -------------------------
  bool button = digitalRead(ENC_BTN);

  if (button == LOW && lastButton == HIGH) {
    Serial.println("PRESS");
    delay(30);
  }

  lastButton = button;

  // -------------------------
  // Befehle von Python empfangen
  // -------------------------
  if (Serial.available()) {

    String command = Serial.readStringUntil('\n');

    command.trim();

    if (
      command == "RED" ||
      command == "GREEN" ||
      command == "BLUE" ||
      command == "YELLOW" ||
      command == "OFF"
    ) {
      showColor(command);
    }
  }
}
