import pygame

class Quille(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("Quilles/quillebleue.png")