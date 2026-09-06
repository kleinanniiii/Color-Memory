import serial
import time

arduino = serial.Serial(
    port="COM3",
    baudrate=115200,
    timeout=0.2
)

# Verhindern, dass DTR/RTS den ESP32 dauerhaft beeinflussen
arduino.dtr = False
arduino.rts = False

print("Mit Makey verbunden...")
time.sleep(2)

# Start-/Bootmeldungen wegwerfen
arduino.reset_input_buffer()

# Die vier auswählbaren Farben
colors = ["RED", "GREEN", "BLUE", "YELLOW"]

# Start bei RED
color_index = 0

print("Jetzt Encoder drehen oder drücken!")

while True:
    if arduino.in_waiting > 0:
        line = arduino.readline().decode("utf-8", errors="ignore").strip()

        if line:
            print("Vom Makey:", line)

            # Nach rechts -> nächste Farbe
            if line == "RIGHT":
                color_index = (color_index + 1) % len(colors)
                print("Ausgewählt:", colors[color_index])

            # Nach links -> vorherige Farbe
            elif line == "LEFT":
                color_index = (color_index - 1) % len(colors)
                print("Ausgewählt:", colors[color_index])

            # Drücken -> Farbe bestätigen
            elif line == "PRESS":
                print("Bestätigt:", colors[color_index])