from re import T
import pygame
from config import *
from tile import Tile
from jogador import Jogador
from debug import debug

class level:
    def __init__(self):

        # Para pegar o tamanho do display
        self.tam_tela = pygame.display.get_surface()
        
        # Setup de grupo de sprites
        self.sprites_visiveis = GrupoCameraEixoY() ##
        self.sprites_obst = pygame.sprite.Group()

        #setup do sprite
        self.criar_mapa()

    def criar_mapa(self):
        for index_linha, linha in enumerate(mapa):
            for index_coluna, coluna in enumerate(linha):
                x = index_coluna * tilesize
                y = index_linha * tilesize
                if coluna == 'x':
                    Tile((x,y),[self.sprites_visiveis, self.sprites_obst])
                if coluna == 'p':
                    self.jogador = Jogador((x,y),[self.sprites_visiveis], self.sprites_obst)


    def run(self):
        #update e desenha o jogo
        self.sprites_visiveis.cust_draw(self.jogador)
        self.sprites_visiveis.update()
        #debug(self.jogador.direc)


class GrupoCameraEixoY(pygame.sprite.Group):
    def __init__(self):
        
        #Grupo geral
        super().__init__()
        self.tam_tela = pygame.display.get_surface()
        self.meia_larg = self.tam_tela.get_size()[0] // 2
        self.meia_alt = self.tam_tela.get_size()[1] // 2
        self.offset = pygame.math.Vector2()

    def cust_draw(self,player):

        #Offset
        self.offset.x = player.rect.centerx - self.meia_larg
        self.offset.y = player.rect.centery - self.meia_alt

        #for sprite in self.sprites():
        for sprite in sorted(self.sprites(), key = lambda sprite: sprite.rect.centery):
            offset_pos = sprite.rect.topleft - self.offset
            self.tam_tela.blit(sprite.image,offset_pos)