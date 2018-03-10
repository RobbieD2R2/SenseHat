# Program to make the Pi act as a compass and tell direction

from sense_hat import SenseHat
sense = SenseHat()
sense.clear()
sense.set_rotation(90)

while True:

    degrees = sense.get_compass()
    print("Degrees: %s" % degrees)
    
    if degrees >= 135 and degrees < 225:
        print("SOUTH")
        sense.show_letter('S')
    elif degrees >=45 and degrees < 135:
        print("EAST")
        sense.show_letter('E')
    elif degrees >= 225 and degrees < 315:
        print("WEST")
        sense.show_letter('W')
    else:
        print("NORTH")
        sense.show_letter('N')



