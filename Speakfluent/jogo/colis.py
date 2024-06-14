import pygame

class colis(pygame.sprite.Sprite):
    def __init__(self,grupos):
        super().__init__(grupos)
            
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