# Program to display random colors on the LED display

from sense_hat import SenseHat
from time import sleep
import random

sense = SenseHat()

# Create colors for Red, Green, Blue, and White
R = [255, 0, 0]
G = [0, 255, 0]
B = [0, 0, 255]
W = [255, 255, 255]

# Create counter variables to act as coordinates in the loop below
x=0
y=0

# Run the randomized display 10 times
for k in range(10):

  # Set all 64 pixels to a random color
	for i in range(8):
		for j in range(8):
			random_color = random.choice([R, G, B, W])
			sense.set_pixel(i, j, random_color)
			y = y+1
		x = x+1
    
	sleep(1)	
	sense.clear()
