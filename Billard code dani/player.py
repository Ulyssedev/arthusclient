import pygame

#quille_x = 0
#quille_y = 0

#classe Quille
class Quille(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("Quilles/quillebleue.png")
        #quille_x = event.pos[0]
		#quille_y = event.pos[1]