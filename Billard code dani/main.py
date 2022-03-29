from game import Game
import pygame
from pygame.locals import *
pygame.init()

#ecran
pygame.display.set_caption("Billard")
screen = pygame.display.set_mode((1920,1080))

#icone
icon_32x32 = pygame.image.load("icones/billard.png")
pygame.display.set_icon(icon_32x32)

#background
bg = pygame.image.load("cartes/salle2.png")

FPS = 165

heheha = pygame.mixer.Sound("Sons/heheha.wav")
corona = pygame.mixer.Sound("Sons/corona.wav")
belayarika = pygame.mixer.Sound("Sons/belayarika.wav")

game = Game()

running = True

quille_x = 0
quille_y = 0


#belayarika.play()

lock = 0
angle = 0
#boucle pour pas fermer fenetre
while running:
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
                #heheha.play()
            elif event.button == 2:
                if lock == 0:
                    lock = 1
                elif lock == 1:
                    lock = 0
    