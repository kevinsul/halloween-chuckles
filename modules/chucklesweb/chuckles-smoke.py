import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

fire_gpio = 21
smoke_gpio = 26

GPIO.setup(smoke_gpio, GPIO.OUT)
GPIO.output(smoke_gpio, GPIO.LOW)

GPIO.output(smoke_gpio, GPIO.HIGH)
time.sleep(4)
GPIO.output(smoke_gpio, GPIO.LOW)