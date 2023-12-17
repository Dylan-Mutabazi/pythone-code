# Imports go at the top
from microbit import *

hungryness = 0

# Code in a 'while True:' loop repeats forever
while True:
    if button_a.was_pressed():
        hungryness = hungryness + 1
        display.show(hungryness)
    
    if button_b.was_pressed():
        hungryness = 0
        display.show(hungryness)