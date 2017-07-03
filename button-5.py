# Import Lib
import RPi.GPIO as GPIO
import time

# Set GPIO Mode
GPIO.setmode(GPIO.BCM)

# Set Pins
GPIO.setup(21,GPIO.IN)
GPIO.setup(20,GPIO.IN)
GPIO.setup(16,GPIO.IN)
GPIO.setup(12,GPIO.IN)
GPIO.setup(24,GPIO.IN)

# Set Previous Inputs for buttons
prev_input_1 = 0
prev_input_2 = 0
prev_input_3 = 0
prev_input_4 = 0
prev_input_5 = 0

while True:
  #take a reading

  #if the last reading was low and this one high, print
  input_1 = GPIO.input(21)
  if ((not prev_input_1) and input_1):
    print("Button 1 pressed")
    #update previous input 
    #slight pause to debounce
    #time.sleep(0.05)
  prev_input_1 = input_1
   

  input_2 = GPIO.input(20)
  if ((not prev_input_2) and input_2):
    print("Button 2 pressed")
    #update previous input  
    #slight pause to debounce
    #time.sleep(0.05)
  prev_input_2 = input_2
  
  input_3 = GPIO.input(16)
  if ((not prev_input_3) and input_3):
    print("Button 3 pressed")
    #update previous input
    #slight pause to debounce
    #time.sleep(0.05)
  prev_input_3 = input_3
   
  input_4 = GPIO.input(12)
  if ((not prev_input_4) and input_4):
    print("Button 4 pressed")
    #update previous input
    #slight pause to debounce
    #time.sleep(0.05)
  prev_input_4 = input_4
 
  input_5 = GPIO.input(24)
  if ((not prev_input_5) and input_5):
    print("Button 5 pressed")
    #update previous input
    #slight pause to debounce
    #time.sleep(0.05)
  prev_input_5 = input_5

  time.sleep(0.05)

