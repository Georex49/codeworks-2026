from gpiozero import Button, TonalBuzzer
from gpiozero.tones import Tone
from time import sleep

button = Button(2)
buzzer = TonalBuzzer(17)

tempo = 180
whole_note = (6000*4) / tempo

#Notes
E5 = 659
D5 = 587
FS4 = 370
GS4 = 415
CS5 = 554
B4 = 494
D4 = 294
E4 = 330
A4 = 440
CS4 = 277

melody = [
  (E5, 8),

  
]


button.wait_for_press()
print('You Pressed Me')
