from gpiozero import DistanceSensor, PWMLED

led = PWMLED(18, frequency = 500)
distancesensor = DistanceSensor(24, 23, max_distance = 1)

try:
    while True:
        duty_cycle = round((1-distancesensor.distance), 10)
        print(duty_cycle)
        led.value = duty_cycle
except KeyboardInterrupt:
    distancesensor.close()S
    led.close()
