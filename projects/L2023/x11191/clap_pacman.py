from microbit import *
import music


while True:
    if microphone.was_event(SoundEvent.LOUD):
            display.show(Image.ALL_ARROWS)
            display.clear()
            display.show(Image.PACMAN)
            music.set_tempo(bpm=180)
            music.play(['B5:4', 'B6:4', 'F#5:4', 'D#5:4', 'B5:4', 'F#5:4', 'D#5:4','C6:4', 'C7:4', 'G5:4', 'E5:4', 'C6:4', 'G5:4', 'E5:4','B5:4', 'B6:4', 'F#5:4', 'D#5:4', 'B5:4', 'F#5:4', 'D#5:4','D#5:4', 'E5:4', 'F5:4', 'F#5:4', 'G5:4', 'G#5:4', 'A5:4', 'B5:4'])
            music.play(['B5:4', 'B6:4', 'F#5:4', 'D#5:4', 'B5:4', 'F#5:4', 'D#5:4','C6:4', 'C7:4', 'G5:4', 'E5:4', 'C6:4', 'G5:4', 'E5:4','B5:4', 'B6:4', 'F#5:4', 'D#5:4', 'B5:4', 'F#5:4', 'D#5:4','D#5:4', 'E5:4', 'F5:4', 'F#5:4', 'G5:4', 'G#5:4', 'A5:4', 'B5:4'])
            music.play(['B5:4', 'B6:4', 'F#5:4', 'D#5:4', 'B5:4', 'F#5:4', 'D#5:4','C6:4', 'C7:4', 'G5:4', 'E5:4', 'C6:4', 'G5:4', 'E5:4','B5:4', 'B6:4', 'F#5:4', 'D#5:4', 'B5:4', 'F#5:4', 'D#5:4','D#5:4', 'E5:4', 'F5:4', 'F#5:4', 'G5:4', 'G#5:4', 'A5:4', 'B5:4'])
            sleep(1000)
            display.show(Image.HAPPY)
            sleep(2200)
            display.scroll(67)
 