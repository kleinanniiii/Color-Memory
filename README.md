# Color-Memory
Color Memory is a small interactive memory game built with Python and a Makey:Lab ESP32 board.

At the beginning of the game, the Makey:Lab LEDs display a sequence of two randomly selected colors. The player has to remember the sequence and reproduce it using the rotary encoder. Turning the encoder allows the player to choose between red, green, blue, and yellow, and pressing the encoder confirms the selected color.

If the player enters the complete sequence correctly, a new random color is added. The full sequence is displayed again and becomes one color longer after every successful round. If the player selects a wrong color, the game ends with Game Over.



What will we learn?

The main goal of this project is to learn basic Python programming through a simple interactive game. We will learn how to:

-create and use variables and lists
-work with if conditions
-use for and while loops
-select random values using random
-add new elements to a sequence
-compare the player's input with the correct sequence
-react to user input from a rotary encoder
-communicate between Python and an ESP32
-control LEDs based on the program logic

The technical communication with the Makey:Lab is mostly provided, so beginners can focus on understanding and programming the game logic step by step.