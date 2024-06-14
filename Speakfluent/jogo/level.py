import pygame
from config import *
from tile import Tile
from jogador import Jogador
from debug import debug
from suporte import *
from ui import UI
from perguntas import PERG
from npcs import NPC

class level:
    def __init__(self):

        self.replay()

        self.per = PERG()

        self.perguntas = False
        self.prof = ''
        self.concluido = False

        #Inicializando status do jogador

        #Manipulação de status
        self.comp_vida = status['Vida']
        self.comp_pont = status['Pontos']
        self.tipo = ''

    def replay(self):

        # Para pegar o tamanho do display
        self.tam_tela = pygame.display.get_surface()
        
        # Setup de grupo de sprites
        self.sprites_visiveis = GrupoCameraEixoY()
        self.sprites_obst = pygame.sprite.Group()

        self.pos_jogador = (170,200)

        #setup do sprite
        self.criar_mapa()

        #interface de usuário
        self.ui = UI()

        status['Respawn'] = 0

    def criar_mapa(self):

        layouts = {
            'fronteira': import_csv_layout('graficos/escola/interior/map/map_Fronteira.csv'),
            'paredes': import_csv_layout('graficos/escola/interior/map/map_Paredes.csv'),
            'decoracao': import_csv_layout('graficos/escola/interior/map/map_Deco.csv'),
            'npc': import_csv_layout('graficos/escola/interior/map/map_Entidades.csv')
        }

        graficos = {
            'parede': import_folder('graficos/escola/interior/parede'),
            'decorac': import_folder('graficos/escola/interior/deco'),
            'profs': import_folder('graficos/profs')
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
                            #Coloca as paredes(apenas questão estética)
                            #Puxa o id do sprite e busca o grafico na lista de graficos
                            if int(coluna) == 512: num = 0
                            if int(coluna) == 604: num = 1
                            if int(coluna) == 1264: num = 2
                            if int(coluna) == 1265: num = 3
                            if int(coluna) == 1266: num = 4

                            ID = graficos['parede'][num]
                            Tile((x,y), [self.sprites_visiveis],'deco', ID)

                        if estilo == 'decoracao':
                            #Coloca as decorações do mapa
                            if int(coluna) == 1596: num = 0 #Porta 001
                            if int(coluna) == 1644: num = 12 #Baixo porta 001
                            if int(coluna) == -2147482052: num = 1 #Porta 002
                            if int(coluna) == -2147482004: num = 14 #Baixo porta 002
                            if int(coluna) == 687: num = 15 #Placa 001
                            if int(coluna) == 735: num = 16 #Placa 002
                            if int(coluna) == 2400: num = 17 #Avisos 001
                            if int(coluna) == 2401: num = 18 #Avisos 002
                            if int(coluna) == 2123: num = 19 #Mesa prof 001
                            if int(coluna) == 2171: num = 20 #Mesa prof 002
                            if int(coluna) == 2219: num = 2 #Mesa prof 003
                            if int(coluna) == 2124: num = 13 #Invisivel 
                            if int(coluna) == 2172: num = 3 #Cadeira prof 001
                            if int(coluna) == 2220: num = 4 #Cadeira prof 002
                            if int(coluna) == 2358: num = 7 #Mesa aluno 001
                            if int(coluna) == 2406: num = 8 #Mesa aluno 002
                            if int(coluna) == 2357: num = 5 #Cadeira aluno 001
                            if int(coluna) == 2405: num = 6 #Cadeira aluno 002
                            if int(coluna) == 2319: num = 9 #Lousa 001
                            if int(coluna) == 2367: num = 10 #Lousa 002
                            if int(coluna) == 2415: num = 11 #Lousa 003

                            ID = graficos['decorac'][num]
                            Tile((x,y), [self.sprites_visiveis],'deco', ID)
                        
                        if estilo == 'npc':
                            if coluna == '0':
                                nome = 'prof1'
                            elif coluna == '1':
                                nome = 'prof2'
                            else:
                                nome = 'prof3_2'
                            NPC(nome,(x,y),[self.sprites_visiveis])

        self.jogador = Jogador((self.pos_jogador),[self.sprites_visiveis], self.sprites_obst)

    def pos_prof(self):

        '''     Otmização de código para colocar dps
            Lembrar de quando acabar optimizar essa parte do código, colocando a zona de interação comum para todos
            e apenas depois testar qual professor esta na frente do jogador:

            *- Código otmizado -*

            if self.sprites_visiveis.offset.x in range(-62, 8):
                if self.jogador.interac:
                    if self.sprites_visiveis.offset.y in range (164, 282):
                        self.prof = perg_prof1
                    elif self.sprites_visiveis.offset.y in range (610, 770):
                        self.prof = perg_prof2
                    elif self.sprites_visiveis.offset.y in range (1080, 1240):
                        self.prof = perg_prof3
                    self.perguntas = True
        '''

        if self.comp_pont < 3:
            
            #Prof 001
            if self.sprites_visiveis.offset.y in range (162, 284):
                if self.comp_pont == status['Pontos'] and self.comp_vida == status['Vida']:
                    self.prof = perg_prof1
                    self.tipo = 'Perg'
                elif self.comp_pont < status['Pontos']:
                    self.prof = cor_prof
                    self.tipo = 'Acerto'
                elif self.comp_vida > status['Vida']:
                    self.prof = cor_prof
                    self.tipo = 'Erro'
                if self.sprites_visiveis.offset.x in range(-70, 6):
                    if self.jogador.interac:
                        self.perguntas = True
            #prof 002
            elif self.sprites_visiveis.offset.y in range (610, 770):
                if self.comp_pont == status['Pontos'] and self.comp_vida == status['Vida']:
                    self.prof = perg_prof2
                    self.tipo = 'Perg'
                elif self.comp_pont < status['Pontos']:
                    self.prof = cor_prof
                    self.tipo = 'Acerto'
                elif self.comp_vida > status['Vida']:
                    self.prof = cor_prof
                    self.tipo = 'Erro'
                if self.sprites_visiveis.offset.x in range(-70, 6):
                    if self.jogador.interac:
                        self.perguntas = True
            #prof 003
            elif self.sprites_visiveis.offset.y in range (1080, 1240):
                if self.comp_pont == status['Pontos'] and self.comp_vida == status['Vida']:
                    self.prof = perg_prof3
                    self.tipo = 'Perg'
                elif self.comp_pont < status['Pontos']:
                    self.prof = cor_prof
                    self.tipo = 'Acerto'
                elif self.comp_vida > status['Vida']:
                    self.prof = cor_prof
                    self.tipo = 'Erro'
                if self.sprites_visiveis.offset.x in range(-70, 6):
                    if self.jogador.interac:
                        self.perguntas = True
            
            else:
                self.comp_pont = status['Pontos']
                self.comp_vida = status['Vida']
                self.perguntas = False
                self.per.respondeu = False

        elif self.comp_pont == 3:
            #Prof001
            if self.sprites_visiveis.offset.y in range (162, 284):
                if self.comp_pont < status['Pontos']:
                    self.prof = cor_prof
                    self.tipo = 'Acerto'
                if self.sprites_visiveis.offset.x in range(-70, 6):
                    if self.jogador.interac:
                        self.perguntas = True
            #Prof002
            if self.sprites_visiveis.offset.y in range (610, 770):
                if self.comp_pont < status['Pontos']:
                    self.prof = cor_prof
                    self.tipo = 'Acerto'
                if self.sprites_visiveis.offset.x in range(-70, 6):
                    if self.jogador.interac:
                        self.perguntas = True
            #Prof003
            if self.sprites_visiveis.offset.y in range (1080, 1240):
                if self.comp_pont < status['Pontos']:
                    self.prof = cor_prof
                    self.tipo = 'Acerto'
                if self.sprites_visiveis.offset.x in range(-70, 6):
                    if self.jogador.interac:
                        self.perguntas = True
            else:
                self.comp_pont += 1
                self.perguntas = False
                self.per.respondeu = False

        elif self.comp_pont > 3:
            if self.sprites_visiveis.offset.x in range(-62, 8):
                if self.sprites_visiveis.offset.y in range (164, 282):
                    if self.jogador.interac:
                        self.prof = cor_prof
                        self.tipo = 'Fim'
                        self.perguntas = True
                elif self.sprites_visiveis.offset.y in range (610, 770):
                    if self.jogador.interac:
                        self.prof = cor_prof
                        self.tipo = 'Fim'
                        self.perguntas = True
                elif self.sprites_visiveis.offset.y in range (1080, 1240):
                    if self.jogador.interac:
                        self.prof = cor_prof
                        self.tipo = 'Fim'
                        self.perguntas = True
            else:
                self.perguntas = False
                        #self.per.respondeu = False

        return (self.perguntas,self.prof,self.tipo)
    
    def run(self):
        #update de tela e desenha o jogo
        if status['Vida'] > 0:
            if status['Respawn'] == 1:
                self.replay()
            self.sprites_visiveis.cust_draw(self.jogador)
            self.sprites_visiveis.update()
            self.ui.display(self.jogador, self.pos_prof()[0], self.pos_prof()[1], self.tipo)
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

        #Criando o fundo
        self.chao = pygame.image.load('graficos/escola/interior/img/interior_esc.png').convert()
        self.chao_rect = self.chao.get_rect(topleft = (0,0))

    def cust_draw(self,player):

        #Offset
        self.offset.x = player.rect.centerx - self.meia_larg
        self.offset.y = player.rect.centery - self.meia_alt
        
        #Adicionando o chão
        self.offset_pos_chao = self.chao_rect.topleft - self.offset
        self.tam_tela.blit(self.chao, self.offset_pos_chao)

        #for sprite in self.sprites():
        for sprite in sorted(self.sprites(), key = lambda sprite: sprite.rect.centery):
            offset_pos = sprite.rect.topleft - self.offset
            self.tam_tela.blit(sprite.image,offset_pos)
