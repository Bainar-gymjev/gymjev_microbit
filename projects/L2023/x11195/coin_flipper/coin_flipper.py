from microbit import *
import random


score = 0
high_score = 0
game_active = False

while True:
    
    if button_a.is_pressed() and not game_active:
        game_active = True
        display.clear()
        
        
        wait_time = random.randint(1000, 3000)
        sleep(wait_time)
        
        
        target_is_skull = random.getrandbits(1)
        
        if target_is_skull:
            display.show(Image.SKULL)
        else:
            display.show(Image.SQUARE)
            
        start_time = running_time()
        success = False
        
        
        while running_time() - start_time < 1500:
            if accelerometer.was_gesture('shake'):
                if target_is_skull:
                    success = True
                break
            sleep(20)
            
        if not target_is_skull and not accelerometer.was_gesture('shake'):
            success = True

        
        if success:
            score += 1
            if score > high_score:
                high_score = score
            display.scroll("+" + str(score))
        else:
            display.show(Image.SAD)
            sleep(1000)
            display.scroll("HS:" + str(high_score))
            score = 0 # Vynulování skóre
            
        game_active = False
    sleep(10)
