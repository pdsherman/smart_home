
import time
import RPi.GPIO as GPIO

PWR_PIN    = 4
HIGH_PIN   = 3
LOW_PIN    = 27
LOWLOW_PIN = 22
MEDIUM_PIN = 2

def setup():
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)
    pins = [PWR_PIN, HIGH_PIN, LOW_PIN, LOWLOW_PIN, MEDIUM_PIN]
    for p in pins:
        GPIO.setup(p, GPIO.OUT)
        GPIO.output(p, GPIO.HIGH)

def pulse(pin):
    GPIO.output(pin, GPIO.LOW)
    time.sleep(0.5)
    GPIO.output(pin, GPIO.HIGH)

def pwr():
    pulse(PWR_PIN)

def lowlow():
    pulse(LOWLOW_PIN)

def low():
    pulse(LOW_PIN)

def medium():
    pulse(MEDIUM_PIN)

def high():
    pulse(HIGH_PIN)

if __name__ == "__main__":
    setup()
    time.sleep(1.0)
    pwr()
    time.sleep(2.0)
    lowlow()
    time.sleep(3.0)
    pwr()
