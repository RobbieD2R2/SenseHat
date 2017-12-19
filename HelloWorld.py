# Basic "Hello world" program to scroll text on the LED matrix

from sense_hat import SenseHat
sense = SenseHat()


# Scroll the message 20 times

for i in range(20):
    sense.show_message("Hello World!")
