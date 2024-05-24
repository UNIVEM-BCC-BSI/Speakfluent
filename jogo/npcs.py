import pygame
from config import *
from colis import colis

class NPC(colis):
    def __init__(self,nome,pos,grupos):

        #Setup geral
        super().__init__(grupos)
        self.tipo_sprite = 'npc'

        #Setup dos graficos
        self.image = pygame.image.load(f'graficos/profs/{nome}.png')
        self.rect = self.image.get_rect(topleft = pos)
        #self.hitbox = self.rect.inflate(100,20)
        

    def get_dist_jogador(self,jogador):
        vet_npc = pygame.math.Vector2(self.rect.center)
        vet_jogador = pygame.math.Vector2(jogador.rect.center)
        dist = (vet_jogador - vet_npc).magnitude()

        return dist

    def status(self,jogador):
        dist = self.get_dist_jogador(jogador)

        if dist <= 80:
            self.status = 'Dentro do raio'
        else:
            self.status = 'Fora do raio'