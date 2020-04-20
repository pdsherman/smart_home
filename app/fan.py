
import time
import RPi.GPIO as GPIO

def setup():
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)
    pins = [17, 22, 27, 23, 24]
    for p in pins:
        GPIO.setup(p, GPIO.OUT)
        GPIO.output(p, GPIO.HIGH)

def pulse(pin):
    GPIO.output(pin, GPIO.LOW)
    time.sleep(0.5)
    GPIO.output(pin, GPIO.HIGH)

def pwr():
    pulse(17)

def lowlow():
    pulse(27)

def low():
    pulse(23)

def medium():
    pulse(24)

def high():
    pulse(22)

if __name__ == "__main__":
    setup()
    time.sleep(1.0)
    pwr()
    time.sleep(2.0)
    lowlow()
    time.sleep(3.0)
    pwr()
