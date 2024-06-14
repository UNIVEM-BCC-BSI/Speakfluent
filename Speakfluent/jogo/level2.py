import pygame
from config import *
from tile import Tile
from jogador import Jogador
from debug import debug
from suporte import *
from ui import UI
from perguntas import PERG
from npcs import NPC

class level02:
    def __init__(self):

        self.tam_tela = pygame.display.get_surface()

        self.sprites_visiveis = GrupoCameraEixoY()
        self.sprites_obst = pygame.sprite.Group()

        self.pos_jogador = (400,300)

        self.criar_mapa()

        self.ui = UI()

        self.per = PERG()

        self.perguntas = False
        self.prof = ''
        self.concluido = False

        #Manipulação de status
        self.comp_vida = status['Vida']
        self.comp_pont = status['Pontos']
        self.tipo = ''

    def criar_mapa(self):

        layouts = {
            'fronteira': import_csv_layout('graficos/biblioteca/interior/map/map_Fronteira.csv'),
            'paredes': import_csv_layout('graficos/biblioteca/interior/map/map_Parede.csv'),
            'decoracao1': import_csv_layout('graficos/biblioteca/interior/map/map_Deco01.csv'),
            'decoracao2': import_csv_layout('graficos/biblioteca/interior/map/map_Deco02.csv'),
            'bib': import_csv_layout('graficos/biblioteca/interior/map/map_Entidades.csv')
        }

        graficos = {
            'parede': import_folder('graficos/biblioteca/interior/parede'),
            'deco': import_folder('graficos/biblioteca/interior/deco'),
            'biblio': import_folder('graficos/biblioteca/interior/prof')
        }

        for estilo, layout in layouts.items():
            for lin_index, linha in enumerate(layout):
                for col_index, coluna in enumerate(linha):
                    if coluna != '-1':

                        x = col_index * tilesize
                        y = lin_index * tilesize

                        if estilo == 'fronteira':
                            #Colocando as linhas de colisão
                            Tile((x,y), [self.sprites_obst],'invisivel')

                        if estilo == 'paredes':
                            if int(coluna) == 65: num = 0
                            if int(coluna) == 103: num = 1

                            ID = graficos['parede'][num]
                            Tile((x,y), [self.sprites_visiveis],'deco',ID)

                        if estilo == 'decoracao1':
                            img = graficos['deco'][int(coluna)]
                            Tile((x,y),[self.sprites_visiveis],'deco',img)

                        if estilo == 'decoracao2':
                            img = graficos['deco'][int(coluna)]
                            Tile((x,y),[self.sprites_visiveis],'deco',img)

                        if estilo == 'bib':
                            img = graficos['biblio'][int(coluna)]
                            Tile((x,y),[self.sprites_visiveis],'npcs',img)

        self.jogador = Jogador((self.pos_jogador),[self.sprites_visiveis], self.sprites_obst)

    def pos_prof(self):
        if self.comp_pont == 4:
            if self.sprites_visiveis.offset.x in range(-230,-130):
                if self.comp_pont == status['Pontos'] and self.comp_vida == status['Vida']:
                    self.prof = perg_biblio
                    self.tipo = 'Perg'
                elif self.comp_pont < status['Pontos']:
                    self.prof = cor_biblio
                    self.tipo = 'Acerto'
                elif self.comp_vida > status['Vida']:
                    self.prof = cor_biblio
                    self.tipo = 'Erro'
                if self.sprites_visiveis.offset.y in range(-60,-125):
                    if self.jogador.interac:
                        self.perguntas = True
            else:
                self.comp_pont = status['Pontos']
                self.comp_vida = status['Vida']
                self.perguntas = False
                self.per.respondeu = False
        
        return(self.perguntas,self.prof,self.tipo)


    def run(self):
        #Desenha a tela do jogo e a atualiza
        if status['Vida'] > 0:
            self.sprites_visiveis.cust_draw(self.jogador)
            self.sprites_visiveis.update()
            self.ui.display(self.jogador, self.pos_prof()[0],self.pos_prof()[1],self.tipo)
            debug(self.sprites_visiveis.offset)
        else:
            status['Nivel'] = 4


class GrupoCameraEixoY(pygame.sprite.Group):
    def __init__(self):
        super().__init__()

        #Grupo geral
        self.tam_tela = pygame.display.get_surface()

        self.offset = pygame.math.Vector2()
        self.meia_larg = self.tam_tela.get_size()[0] // 2
        self.meia_alt = self.tam_tela.get_size()[1] // 2

        #Criação do fundo
        self.chao = pygame.image.load('graficos/biblioteca/interior/img/Biblio_interior.png').convert()
        self.chao_rect = self.chao.get_rect(topleft = (0,0))

    def cust_draw(self,player):
        
        #offset
        self.offset.x = player.rect.centerx - self.meia_larg
        self.offset.y = player.rect.centery - self.meia_alt

        #Adicionando o chão
        self.offset_pos_chao = self.chao_rect.topleft - self.offset
        self.tam_tela.blit(self.chao, self.offset_pos_chao)

        for sprite in sorted(self.sprites(), key = lambda sprite: sprite.rect.centery):
            offset_pos = sprite.rect.topleft - self.offset
            self.tam_tela.blit(sprite.image,offset_pos)