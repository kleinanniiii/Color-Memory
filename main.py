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

# Aufgabe 1)
# Erstelle eine Liste mit den vier auswählbaren Farben.


# Aufgabe 2)
# Erstelle eine Variable für die aktuell ausgewählte Farbe.
# Zu Beginn soll RED ausgewählt sein.

# Aufgabe 3)
# Erstelle eine leere Liste namens sequenz.
# Wähle zwei zufällige Farben aus und speichere sie in sequenz.


print(sequenz)

#Random Farben anzeigen
for farbe in sequenz:
    arduino.write((farbe + "\n").encode())
    time.sleep(1)
    arduino.write(("OFF" + "\n").encode())
    time.sleep(0.5)

print("Jetzt Encoder drehen oder drücken!")

# Aufgabe 4)
# Erstelle eine leere Liste für die Spielereingaben


while True:
    if arduino.in_waiting > 0:
        befehl = arduino.readline().decode("utf-8", errors="ignore").strip()

        if befehl:
            print("Vom Makey:", befehl)

            # Aufgabe 5)
            # Prüfe, ob der Encoder nach rechts gedreht wurde und wähle die nächste Farbe
            

            # Aufgabe 6)
            # Prüfe, ob der Encoder nach links gedreht wurde und wähle die vorherige Farbe
            

            # Drücken -> Farbe bestätigen
            elif befehl == "PRESS":
                print("Bestätigt:", colors[color_index])
                spielereingabe = spielereingabe + [colors[color_index]]
                if spielereingabe[-1] != sequenz[len(spielereingabe) - 1]:
                    print("Game Over")
                    break
                print(spielereingabe)

                # Aufgabe 7)
                # Prüfe, ob die komplette Runde richtig war
                
                    # Aufgabe 8)
                    # Füge der Sequenz eine neue zufällige Farbe hinzu
                    
                    # Aufgabe 9)
                    # Leere die Spielereingaben für die nächste Runde
                    

                    #neue laengere Sequenz anzeigen
                    for farbe in sequenz:
                        arduino.write((farbe+ "\n").encode())
                        time.sleep(1)
                        arduino.write(("OFF" + "\n").encode())
                        time.sleep(0.5)

