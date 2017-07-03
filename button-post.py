# Import Lib
import RPi.GPIO as GPIO
import time
import requests


# Set GPIO Mode
GPIO.setmode(GPIO.BCM)

def initGPIO():
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

url = 'http://10.0.0.107:8080/IOTStanfordAttendanceSystem/stanford/feedback/ratings/'
headers = {'Content-Type': 'application/json'}

def sendPOSTRequest(buttonPressed):
  print("Button %s pressed"%buttonPressed)
  data = '''{"rfid":"d","sessionId":"sd","rate":2}'''
  response = requests.post(url, headers = headers ,data=data)
  print response

initGPIO()

while True:
  #take a reading

  #if the last reading was low and this one high, print
  input_1 = GPIO.input(21)
  if ((not prev_input_1) and input_1):
    #print("Button 1 pressed")
    sendPOSTRequest(1)
    #update previous input
    #slight pause to debounce
    #time.sleep(0.05)
  prev_input_1 = input_1


  input_2 = GPIO.input(20)
  if ((not prev_input_2) and input_2):
    sendPOSTRequest(2)
    #update previous input
    #slight pause to debounce
    #time.sleep(0.05)
  prev_input_2 = input_2

  input_3 = GPIO.input(16)
  if ((not prev_input_3) and input_3):
    sendPOSTRequest(3)
    #update previous input
    #slight pause to debounce
    #time.sleep(0.05)
  prev_input_3 = input_3

  input_4 = GPIO.input(12)
  if ((not prev_input_4) and input_4):
    sendPOSTRequest(4)
    #update previous input
    #slight pause to debounce
    #time.sleep(0.05)
  prev_input_4 = input_4

  input_5 = GPIO.input(24)
  if ((not prev_input_5) and input_5):
    sendPOSTRequest(5)
    #update previous input
    #slight pause to debounce
    #time.sleep(0.05)
  prev_input_5 = input_5

  time.sleep(0.05)


