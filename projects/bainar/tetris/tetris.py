# Imports go at the top
from microbit import *
from random import randint

triominos = (((1,0), (1,1), (2,0), (2,1)),
             ((2,0), (3,0), (1,0)),
             ((2,0), (3,0), (2,1)),
             ((1,0), (2,0), (2,1)),
             ((2,0), (2,1), (3,1)), 
             ((1,1), (2,0), (2,1)),
             ((2,0),),
            )

board = [[False, False, False, False, False],  # first always empty row
        [False, False, False, False, False],
        [False, False, False, False, False],
        [False, False, False, False, False],
        [False, False, False, False, False],
        [False, False, False, False, False],
        [True, True, True, True, True],  # last always full row
        ]

move_interval = 100
drop_interval = 900

def write(coord_list, intensity):
    for coord in coord_list:
        display.set_pixel(coord[0], coord[1], intensity)


def move(block, way):
    new_block = []
    for b in block:
        new_block.append(((b[0] + way[0]) % 5, b[1] + way[1]))  # no sidewalls
        if board[new_block[-1][1] + 1][new_block[-1][0]]:
            return block, False
            
    write(block, 0)
    write(new_block, 9)
    return new_block, True
    
def full_rows_test():
    global score
    mult = 1
    for i, row in enumerate(board[:-1]):
        if all(row):
            score += 5 * mult
            mult += 1
            for j in range(0, i):
                for k in range(5):
                    board[i-j][k] = board[i-j-1][k]
            display.clear()
            for i in range(5):
                for j in range(5):
                    if board[i+1][j]:
                        display.set_pixel(j,i,9)

def debug_print():
    out_text = ''
    for i in range(7):
        for j in range(5):
            if board[i][j]:
                out_text += '#'
            else:
                out_text += '.'
        out_text += '\n'
    print(out_text)
                        

display.show(Image('05550:'
                   '59995:'
                   '05950:'
                   '05950:'
                   '00500:')
            )
sleep(1000)
display.clear()
last_drop = running_time()
last_move = running_time()
score = 0
while True:
    block = triominos[randint(0, len(triominos) - 1)]
    print(block)
    if any([board[i+1][j] for j,i in block]):
        break
    write(block, 9)
    while True:
        if running_time() - last_move > move_interval:
            if button_a.was_pressed():
                last_move = running_time()
                block, _ = move(block, (-1,0))
            if button_b.was_pressed():
                last_move = running_time()
                block, _ = move(block, (1,0))
        if running_time() - last_drop > drop_interval:
            last_drop = running_time()
            block, falling = move(block, (0,1))
            if not falling:
                score += 1
                for b in block:
                    board[b[1] + 1][b[0]] = True
                full_rows_test()
                break
                       
display.scroll(score)