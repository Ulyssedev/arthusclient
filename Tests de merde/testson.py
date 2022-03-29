import pygame
window_resolution = (640, 480)
launched = True

pygame.init()
pygame.display.set_caption("Test Son")
window_surface = pygame.display.set_mode(window_resolution)

celtic_song = pygame.mixer.Sound("hehehe-haclash-royale.ogg")
celtic_song.play()

pygame.display.flip()

while launched:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            launched = False
