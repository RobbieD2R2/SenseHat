# Program to display the current humidity and temperature

from sense_hat import SenseHat
import math
sense = SenseHat()

# Display the humidity
sense.show_message("Humidity:")
sense.show_message(str(math.floor(sense.get_humidity())))
sense.show_message("%")

# Get the temperature (in celsius) and convert to farenheit
celsius = sense.get_temperature()
farenheit = (celsius * 1.8) + 32

# Display both temperatures
sense.show_message("Temp:")
sense.show_message(str(math.floor(farenheit)))
sense.show_message("F")
sense.show_message(str(math.floor(celsius)))
sense.show_message("C")
