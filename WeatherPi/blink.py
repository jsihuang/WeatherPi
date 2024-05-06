import RPi.GPIO as GPIO # Import Raspberry Pi GPIO library
from time import sleep # Import the sleep function from the time module

GPIO.setwarnings(False) # Ignore warning for now
GPIO.setmode(GPIO.BOARD) # Use physical pin numbering
GPIO.setup(8, GPIO.OUT, initial=GPIO.LOW) # Set pin 8 to be an output pin and set initial value to low (off)
GPIO.setup(10, GPIO.OUT, initial=GPIO.LOW)


# Create a PWM object with a frequency of 100 Hz
# pwm = GPIO.PWM(8, 100)
# pwm = GPIO.PWM(10, 100)
# pwm.start(0) # Start PWM with 0% duty cycle (off)

def forever(): # Testing - Run forever
	GPIO.output(8, GPIO.HIGH) # Turn on
	GPIO.output(10, GPIO.HIGH) # Turn on
	sleep(1) # Sleep for 1 second
	GPIO.output(8, GPIO.LOW) # Turn off
	GPIO.output(10, GPIO.LOW) # Turn on
	sleep(1) # Sleep for 1 second
	
def rain():
	GPIO.output(8, GPIO.HIGH) # Turn on
	sleep(0.2) # Sleep for 1 second
	GPIO.output(10, GPIO.HIGH) # Turn on
	GPIO.output(8, GPIO.LOW) # Turn on
	sleep(0.2) # Sleep for 1 second
	GPIO.output(10, GPIO.LOW) # Turn on


def drizzle():
	GPIO.output(8, GPIO.HIGH) # Turn on
	sleep(2) # Sleep for 1 second
	GPIO.output(10, GPIO.HIGH) # Turn on
	GPIO.output(8, GPIO.LOW) # Turn off
	sleep(2) # Sleep for 1 second
	GPIO.output(10, GPIO.LOW) # Turn on
	

	
def clear():
		for dc in range(0, 101, 5): # Increase duty cycle forom 0 to 100 in steps of 5
			pwm.ChangeDutyCycle(dc) # Set duty cycle
			sleep(0.2) # Wait for a short duration for gradual increase
		sleep(3) # Wait for a longer duration at maximum intensity
		# GPIO.output(8, GPIO.LOW) # Turn on
		# sleep(1) # Sleep for 1 second
		
		pwm.stop() # Stop PWM
		GPIO.cleanup() # Clean up GPIO settings
	

while True: 
	drizzle()

