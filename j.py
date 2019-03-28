from gpiozero import LED
from time import sleep

led = LED(17)
i = 1

led.on()
sleep(1)
led.off()
while i <= 3
	sleep(1)
	led.on()
	sleep(3)
	led.off()
	i+=1
sleep(3)
