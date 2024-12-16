import RPi.GPIO as GPIO
import time

# Configura i pin GPIO
LED_PIN = 17
GPIO.setmode(GPIO.BCM)
GPIO.setup(LED_PIN, GPIO.OUT)

try:
    print("LED Blinker in esecuzione. Premi Ctrl+C per uscire.")
    while True:
        GPIO.output(LED_PIN, GPIO.HIGH)  # Accendi il LED
        print("LED acceso")
        time.sleep(1)  # Aspetta 1 secondo
        GPIO.output(LED_PIN, GPIO.LOW)   # Spegni il LED
        print("LED spento")
        time.sleep(1)  # Aspetta 1 secondo
except KeyboardInterrupt:
    print("\nProgramma interrotto manualmente.")
finally:
    GPIO.cleanup()  # Pulisce la configurazione GPIO
