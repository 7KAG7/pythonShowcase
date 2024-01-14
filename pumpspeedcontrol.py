import rpi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
pump_pin = 18

GPIO.setup(pump_pin, GPIO.OUT)
pwm = GPIO.PWM(pump_pin, 100)


try: 
    while True:
        speed = float(input("Enter pump speed (0-100): "))
        if 0 <= speed <= 100:
            duty_cycle = speed / 10.0
            pwm.ChangeDutyCycle(duty_cycle)
            print(f"Pump speed set to {speed}%")
        else:
            print("Invalid speed. Enter a value between 0 and 100.")
except KeyboardInterrupt:
    pass
finally:
    pwm.stop()
    GPIO.cleanup()
