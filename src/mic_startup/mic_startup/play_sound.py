import pygame

pygame.mixer.init()
sound = pygame.mixer.Sound('17.wav')
playing = sound.play()
while playing.get_busy():
    pygame.time.delay(100)  

