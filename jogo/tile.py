import pygame
from config import *

class Tile(pygame.sprite.Sprite):
    def __init__(self, pos, grupos, tipo_sprite, superficie = pygame.Surface((tilesize,tilesize))):
        super().__init__(grupos)
        self.tipo_sprite = tipo_sprite
        self.image = superficie
        self.rect = self.image.get_rect(topleft = pos)
        self.hitbox = self.rect.inflate(0,-10)