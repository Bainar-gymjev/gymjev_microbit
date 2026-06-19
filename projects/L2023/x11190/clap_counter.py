# Imports go at the top
from microbit import *

from microbit import*
import music

clap_count = 0
last_clap_count = running_time()

while True:
    display.show("Clap!")
    display.clear()
    clap_count = 0
    last_clap_count = running_time()
    while running_time() - last_clap_count < 2000:
        if microphone.was_event(SoundEvent.LOUD):
            clap_count = clap_count + 1
    display.show(clap_count)

    
    if clap_count == 1:
        display.show (Image.ANGRY)
    if clap_count == 2:
        display.show (Image.HAPPY)
    sleep(1000)
        
        

    
        
        
            
    
