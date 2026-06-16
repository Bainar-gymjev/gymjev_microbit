from microbit import *
result = 0
x = 0
y = 0

def neznamax(x):
    while True:
        display.show(x)
        if button_a.was_pressed():
            x += 1
            if x == 10:
                x=0
            display.show(x)

        if button_b.was_pressed():
            display.show(Image('00000:'
                                '00900:'
                                '09990:'
                                '00900:'
                                '00000',))
            sleep(1000)
            return x

def neznamay(x, y):
    while True:
        display.show(y)
        if button_a.was_pressed():
            y += 1
            if y == 10:
                y=0
            display.show(y)
        if button_b.was_pressed():
            result = x+y
            display.show(result)
            break

while True:
    display.scroll("? A")  
    if button_a.was_pressed():
            x = neznamax(x)          
            neznamay(x, y)
            sleep(1000)
            display.scroll("? A")
            x = 0
            y = 0