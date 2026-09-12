import serial
import time
import random

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

#random Farbe erzeugen
sequenz = []
for i in range(2):
    pick_color = random.choice(colors)
    sequenz = sequenz + [pick_color] 

print(sequenz)

#Random Farben anzeigen
for farbe in sequenz:
    arduino.write((farbe+ "\n").encode())
    time.sleep(1)
    arduino.write(("OFF" + "\n").encode())

print("Jetzt Encoder drehen oder drücken!")

while True:
    if arduino.in_waiting > 0:
        befehl = arduino.readline().decode("utf-8", errors="ignore").strip()

        if befehl:
            print("Vom Makey:", befehl)

            # Nach rechts -> nächste Farbe
            if befehl == "RIGHT":
                color_index = (color_index + 1) % len(colors)
                print("Ausgewählt:", colors[color_index])
                arduino.write((colors[color_index] + "\n").encode())

            # Nach links -> vorherige Farbe
            elif befehl == "LEFT":
                color_index = (color_index - 1) % len(colors)
                print("Ausgewählt:", colors[color_index])
                arduino.write((colors[color_index] + "\n").encode())

            # Drücken -> Farbe bestätigen
            elif befehl == "PRESS":
                print("Bestätigt:", colors[color_index])

