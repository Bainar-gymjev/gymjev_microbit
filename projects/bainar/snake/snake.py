# Imports go at the top
from microbit import *
from random import randint

cup = Image('09990:'
        '90909:'
        '09990:'
        '00900:'
        '09990:'
    )

arrow_up = Image('00900:'
    '09990:'
    '99999:'
    '03930:'
    '03930:'
    )

def game_snake(speed = 512, level = 1):
    def move_snake(x, y, dir):
        if dir == 0:
            return (x + 1) % 5, y
        elif dir == 1:
            return x, (y + 4) % 5
        elif dir == 2:
            return (x + 4) % 5, y
        elif dir == 3:
            return x, (y + 1) % 5
        return 0, 0
        
    def gen_apple(snake):
        apple_x, apple_y = snake[0]
        while display.get_pixel(apple_x, apple_y) != 0:
            apple_x, apple_y = randint(0,4), randint(0,4)
        display.set_pixel(apple_x, apple_y, 9)
        
    alive = True
    snake = [(2,3), (2,2)]

    display.clear()
    display.show(level)
    sleep(1000)
    display.clear()
    for x, y in snake:
        #display.show(y)
        display.set_pixel(x, y, 6)
    gen_apple(snake)
    # speed = 512
    dir = 1
    while alive:
        A, B = button_a.was_pressed(), button_b.was_pressed()
        if A and B:
            alive = False
            break
        elif B:
            dir = (dir + 3) % 4
        elif A:
            dir = (dir + 1) % 4
            
        tail_x, tail_y = snake[0]
        head_x, head_y = snake[-1]
        new_x, new_y = move_snake(head_x, head_y, dir)
        display.set_pixel(tail_x, tail_y, 0)
        if display.get_pixel(new_x, new_y) == 6:
            alive = False
            break
        elif display.get_pixel(new_x, new_y) == 0:
            snake.pop(0)
        elif display.get_pixel(new_x, new_y) == 9:
            display.set_pixel(tail_x, tail_y, 6)
            gen_apple(snake)
            
        display.set_pixel(new_x, new_y, 6)
        snake.append((new_x, new_y))
        if len(snake) >= 20:
            if speed >= 128:
                display.show(arrow_up)
                sleep(1000)
                game_snake(speed // 2, level + 1)
                return None
            else:
                display.show("WIN!")
                display.show(cup)
                sleep(1000)
                return None
        sleep(speed)
    display.show(Image.SKULL)
    sleep(1000)
    display.clear()

game_snake()