'''

Adapted excerpt from Getting Started with Raspberry Pi by Matt Richardson

Modified by Rui Santos
Complete project details: https://randomnerdtutorials.com

'''

import RPi.GPIO as GPIO
import time
from flask import Flask, render_template, request
import os

app = Flask(__name__)

GPIO.setmode(GPIO.BCM)

fire_gpio = 21
strobe_gpio = 20
smoke_gpio = 26

sequences = ["Fireball", "LGB", "RandomSound", "Strobe-On", "Strobe-Off", "Smoke"]

# Set each pin as an output and make it low:
GPIO.setup(fire_gpio, GPIO.OUT)
GPIO.output(fire_gpio, GPIO.LOW)

GPIO.setup(strobe_gpio, GPIO.OUT)
GPIO.output(strobe_gpio, GPIO.LOW)

GPIO.setup(smoke_gpio, GPIO.OUT)
GPIO.output(smoke_gpio, GPIO.LOW)


@app.route("/")
def main():
   # For each pin, read the pin state and store it in the pins dictionary:
   #for pin in pins:
   #   pins[pin]['state'] = GPIO.input(pin)
   # Put the pin dictionary into the template data dictionary:
   templateData = {
      'sequences' : sequences
      }
   # Pass the template data into the template main.html and return it to the user
   return render_template('main.html', **templateData)

# The function below is executed when someone requests a URL with the pin number and action in it:
@app.route("/<chosensequence>")
def action(chosensequence):
   # Convert the pin from the URL into an integer:
   #changePin = int(changePin)
   # Get the device name for the pin being changed:
   #deviceName = chosensequence
   # If the action part of the URL is "on," execute the code indented below:
   if chosensequence == 'Fireball':
      # Set the pin high:
      # Save the status message to be passed into the template:
      # message = "Turned " + deviceName + " on."
      GPIO.output(fire_gpio, GPIO.HIGH)
      time.sleep(.10)
      GPIO.output(fire_gpio, GPIO.LOW)
   if chosensequence == 'LGB':
      # Set the pin high:
      # Save the status message to be passed into the template:
      # message = "Turned " + deviceName + " on."
      GPIO.output(fire_gpio, GPIO.HIGH)
      time.sleep(.10)
      GPIO.output(fire_gpio, GPIO.LOW)
      time.sleep(.25)
      GPIO.output(fire_gpio, GPIO.HIGH)
      time.sleep(.10)
      GPIO.output(fire_gpio, GPIO.LOW)
      time.sleep(.25)
      GPIO.output(fire_gpio, GPIO.HIGH)
      time.sleep(.75)
      GPIO.output(fire_gpio, GPIO.LOW)
   if chosensequence == 'RandomSound':
      os.system("python3 chuckles-sounds.py &")
   if chosensequence == 'Strobe-On':
      GPIO.output(strobe_gpio, GPIO.HIGH)      
   if chosensequence == 'Strobe-Off':      
      GPIO.output(strobe_gpio, GPIO.LOW)      
   if chosensequence == 'Smoke':      
      os.system("python3 chuckles-smoke.py &")
      
   # For each pin, read the pin state and store it in the pins dictionary:
   #for pin in pins:
   #   pins[pin]['state'] = GPIO.input(pin)

   # Along with the pin dictionary, put the message into the template data dictionary:
   templateData = {
      'sequences' : sequences
   }

   return render_template('main.html', **templateData)

if __name__ == "__main__":
   app.run(host='0.0.0.0', port=8000, debug=True)
