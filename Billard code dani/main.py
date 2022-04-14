from game import Game
import pygame
from pygame.locals import *
pygame.init()


pygame.display.set_caption("Billard Du Daniel")
screen = pygame.display.set_mode((1920,1080))


icon_32x32 = pygame.image.load("icones/billard.png")
pygame.display.set_icon(icon_32x32)

bg = pygame.image.load("cartes/salle2.png")

FPS = 165

heheha = pygame.mixer.Sound("Sons/heheha.wav")
corona = pygame.mixer.Sound("Sons/corona.wav")
belayarika = pygame.mixer.Sound("Sons/belayarika.wav")

game = Game()
imcount = 0
running = True

quille_x = 0
quille_y = 0

rotated_image = game.player.image

lock = 0
angle = 0


while running:
    game.player.image = rotated_image
    screen.blit(bg, (0, 0))
    screen.blit(game.player.image, (quille_x, quille_y))
    pygame.display.flip()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if lock == 0 and event.button == 1:
                quille_x = event.pos[0]
                quille_y = event.pos[1]
                screen.blit(game.player.image, (quille_x, quille_y))
                heheha.play()
            elif event.button == 2:
                if lock == 0:
                    lock = 1
                elif lock == 1:
                    lock = 0
            elif lock == 1 and event.button == 3:
                rotated_image = pygame.transform.rotate(game.player.image, angle)
                angle += 1
                screen.blit(rotated_image, (quille_x, quille_y))
                #game.player.image = pygame.transform.rotate(game.player.image, 1)
                
    