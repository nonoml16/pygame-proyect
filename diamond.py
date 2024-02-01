import pygame
from config import *

class Diamond(pygame.sprite.Sprite):
    def __init__(self, game, x, y):
        self.game = game
        self._layer = ITEM_LAYER
        self.groups = self.game.all_sprites
        pygame.sprite.Sprite.__init__(self, self.groups)

        self.x = x * TILESIZE
        self.y = y * TILESIZE
        self.width = TILESIZE
        self.height = TILESIZE

        # Cargar la imagen del diamante desde el archivo diamond.png en la carpeta assets
        self.image = pygame.image.load('assets/diamond.png').convert_alpha()

        # Escalar la imagen al tamaño del mosaico
        self.image = pygame.transform.scale(self.image, (self.width, self.height))

        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y
