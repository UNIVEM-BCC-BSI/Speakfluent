import pygame
from config import *

class Jogador(pygame.sprite.Sprite):
    def __init__(self, pos, grupos, obst_sprites):
        super().__init__(grupos)
        self.image = pygame.image.load('Speakfluent_v0.0.1/graphics/test/player.png').convert_alpha()
        self.rect = self.image.get_rect(topleft = pos)
        self.hitbox = self.rect.inflate(0, -26)

        #Movimentação
        self.direc = pygame.math.Vector2()
        self.velo = 5

        #Colisão
        self.obst_sprites = obst_sprites

    def input(self):

        teclas = pygame.key.get_pressed()

        if teclas[pygame.K_w]:
            self.direc.y = -1
        elif teclas[pygame.K_s]:
            self.direc.y = 1
        else:
            self.direc.y = 0
        if teclas[pygame.K_a]:
            self.direc.x = -1
        elif teclas[pygame.K_d]:
            self.direc.x = 1
        else:
            self.direc.x = 0

    def mov(self, velo):
        if self.direc.magnitude() != 0:
            self.direc = self.direc.normalize()
        
        self.hitbox.x += self.direc.x * velo
        self.colis('horizontal')
        self.hitbox.y += self.direc.y * velo
        self.colis('vertical')
        self.rect.center = self.hitbox.center

    def colis(self, direc):
        if direc == 'horizontal':
            for sprite in self.obst_sprites:
                if sprite.hitbox.colliderect(self.hitbox):
                    if self.direc.x > 0:        #Nos movendo para a direita
                        self.hitbox.right = sprite.hitbox.left
                    if self.direc.x < 0:        #Nos movendo para a esquerda
                        self.hitbox.left = sprite.hitbox.right

        if direc == 'vertical':
            for sprite in self.obst_sprites:
                if sprite.hitbox.colliderect(self.hitbox):
                    if self.direc.y > 0:        #Nos movendo para baixo
                        self.hitbox.bottom = sprite.hitbox.top
                    if self.direc.y < 0:        #Nos movendo para cima
                        self.hitbox.top = sprite.hitbox.bottom

    def update(self):
        self.input()
        self.mov(self.velo)
