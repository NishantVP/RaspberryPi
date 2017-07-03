# Import Lib
import RPi.GPIO as GPIO
import time

# Set GPIO Mode
GPIO.setmode(GPIO.BCM)

# Set Pins
GPIO.setup(17,GPIO.IN)

# Set Previous Inputs for buttons
prev_input = 0

while True:
  #take a reading
  input = GPIO.input(17)
  #if the last reading was low and this one high, print
  if ((not prev_input) and input):
    print("Button pressed")
  #update previous input
  prev_input = input
  #slight pause to debounce
  time.sleep(0.05)


