# Skull Reflex Game
A fast-paced reaction game built for the BBC micro:bit using MicroPython. Test your reflexes and see how long you can keep your streak alive!
## Author
**x11195**
## How to Play
1. Start the game: Press Button A to begin.
2. Wait for the cue: The screen will clear, and after a random delay (1 to 3 seconds), an image will appear.
3. React quickly: You have exactly 1.5 seconds to make the right move:
   * 💀 If you see a SKULL: Quickly SHAKE the micro:bit.
   * 🔲 If you see a SQUARE: DO NOT SHAKE the micro:bit (stay completely still).
## Scoring
* Success: If you react correctly, your current score increases by 1 and scrolls across the screen (e.g., +1, +2).
* Game Over: If you shake on a square, fail to shake on a skull, or take too long, a SAD face will appear. Your final high score (HS) will then scroll across the screen, and your current score resets to 0.
## Controls
* Button A: Start a new round.
* Shake Gesture: Defeat the skull target.