""" EE 250L Lab 02: GrovePi Sensors

List team members here.
Insert Github repository link here.
"""
#github.com/jaylenvictoria/GrovePi-EE250
"""python3 interpreters in Ubuntu (and other linux distros) will look in a 
default set of directories for modules when a program tries to `import` one. 
Examples of some default directories are (but not limited to):
  /usr/lib/python3.5
  /usr/local/lib/python3.5/dist-packages

The `sys` module, however, is a builtin that is written in and compiled in C for
performance. Because of this, you will not find this in the default directories.
"""
import sys
import time
# By appending the folder of all the GrovePi libraries to the system path here,
# we are successfully `import grovepi`
sys.path.append('../../Software/Python/')
# This append is to support importing the LCD library.
sys.path.append('../../Software/Python/grove_rgb_lcd')

import grovepi
from grove_rgb_lcd import *

"""This if-statement checks if you are running this python file directly. That 
is, if you run `python3 grovepi_sensors.py` in terminal, this if-statement will 
be true"""

#connect grove rotary angle senssor to analog port A1
potentiometer = 1

grovepi.pinMode(potentiometer,"INPUT")
time.sleep(1)

#adc refrence voltage
adc_ref = 5

#vcc of grove interface
grove_vcc = 5

#the full angle of the rotary angle is 300 degrees
full_angle = 300

#range of ultrasonic 
ultrasonic_range = 518

#connect ultrasonic ranger to D7
ultrasonic_ranger = 7


if __name__ == '__main__':
#background color
	setRGB(0, 128, 0)
	while True:
		try:
			#read sensor value from potentiometer
			sensor_value = grovepi.analogRead(potentiometer)
			
			#calculate voltage
			voltage = round((float)(sensor_value) * adc_ref / 1023, 2)
			
			#calculate rotation in degrees
			degrees = round((voltage * full_angle) / grove_vcc, 2)

			#convert to range from degrees
			target = int(degrees / full_angle * ultrasonic_range)

			#distance from ranger
			distance = grovepi.ultrasonicRead(ultrasonic_ranger)

			if distance < target:
				setRGB( 128, 0, 0)
				display = '%3dcm OBJ PRES %3dcm' % (target, distance)
			else:
				setRGB( 0, 128, 0)
				display = '%3dcm           %3dcm' % (target, distance)

			setText_norefresh(display)

		except KeyboardInerrupt:
			#turn it off
			setRGB(0,0,0)
			setText('')
			break

		except I0Error:
			print("Error")
			setText('')

