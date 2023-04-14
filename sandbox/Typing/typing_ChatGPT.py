import pygame
import random

# initialize pygame
pygame.init()

# load sound files
sounds = {}
for i in range(ord('b'), ord('n')):
    sound_file = chr(i) + ".wav"
    sound = pygame.mixer.Sound(sound_file)
    sounds[i] = sound

# load special sound for space bar
space_sound = pygame.mixer.Sound("a.wav")

# set up the display
screen = pygame.display.set_mode((400, 300))

# main game loop
playing_sounds = []
done = False
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                done = True
            elif event.key == pygame.K_SPACE:
                space_sound.play()
            elif event.key == pygame.K_LCTRL and pygame.key.get_mods() & pygame.KMOD_CTRL:
                # stop all sounds if Control+S is pressed
                for sound in playing_sounds:
                    sound.stop()
                playing_sounds.clear()
            else:
                if len(playing_sounds) < 5:
                    sound = sounds.get(event.key)
                    if sound is not None:
                        sound.play()
                        playing_sounds.append(sound)
                else:
                    for sound in playing_sounds:
                        sound.stop()
                    playing_sounds.clear()

        #elif event.type == pygame.KEYUP:
        #    if event.key == pygame.K_SPACE:
        #        space_sound.stop()

    # draw the screen
    screen.fill((255, 255, 255))
    pygame.display.flip()

# clean up
pygame.quit()
