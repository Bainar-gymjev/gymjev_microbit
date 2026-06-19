from microbit import *
import random
def hra():
    raketa_x = 2
    meteory = []
    skore = 0
    rychlost = 500
    while True:
        if button_a.was_pressed() and raketa_x > 0:
            raketa_x -= 1
        if button_b.was_pressed() and raketa_x < 4:
            raketa_x += 1
        if random.randint(0, 100) < 40:
            meteory.append([random.randint(0, 4), 0])
        nove_meteory = []
        for meteor in meteory:
            meteor[1] += 1
            if meteor[1] == 4 and meteor[0] == raketa_x:
                display.show(Image.SAD)
                sleep(1000)
                display.scroll("Skore: " + str(skore))
                display.scroll("A+B")
                while True:
                    if button_a.is_pressed() and button_b.is_pressed():
                        sleep(500)
                        return
            elif meteor[1] > 4:
                skore += 1
                if rychlost > 150:
                    rychlost -= 5
            else:
                nove_meteory.append(meteor)
        meteory = nove_meteory
        display.clear()
        display.set_pixel(raketa_x, 4, 9)
        for meteor in meteory:
            display.set_pixel(meteor[0], meteor[1], 5)
        sleep(rychlost)
display.scroll("START")
hra()
