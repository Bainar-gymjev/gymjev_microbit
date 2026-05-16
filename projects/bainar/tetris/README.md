# Micro:bit Tetris

## Author

David Bainar

## Description

A small Tetris-inspired game for the BBC micro:bit.

The game uses fixed triomino shapes instead of traditional tetrominoes.
Unlike classic Tetris:

- pieces cannot be rotated
- pieces can wrap around the screen through the side walls
- the game ends when it is not possible to place new block

After the game ends, the final score is displayed on the LED screen.

## Shapes

The game uses the following triominoes:

    ##   ##   ##    #   #    ###   #
    ##   #     #   ##   ##

## Controls

- **Button A** — move piece left
- **Button B** — move piece right

## Scoring

- **1 point** for each placed piece
- **5 points** for clearing one row
- **15 points** for clearing two rows at the same time