import pygame, sys
from config import *
from level import level

class gameover:
    def __init__(self):
        self.tam_tela = pygame.display.get_surface()

        self.level = level()

        self.fonte_titulo = pygame.font.Font(UI_fonte, 120)
        self.fonte_bot = pygame.font.Font(UI_fonte, 60)

        self.quad = (60,60)

        self.vida = status['Vida']
        self.nivel = status['Nivel']   

    def escritas(self):
        titulo = self.fonte_titulo.render('Game Over',False,'White')
        x = self.tam_tela.get_size()[0] / 2
        y = 100
        self.titulo_rect = titulo.get_rect(center = (x,y))
        self.tam_tela.blit(titulo, self.titulo_rect)

        pos_bots = (self.tam_tela.get_size()[0] / 2,
                    self.tam_tela.get_size()[1] / 2)

        tentar = self.fonte_bot.render('(1) Tentar novamente',False,'Black')
        self.tent_rect = tentar.get_rect(center = (pos_bots))
        pygame.draw.rect(self.tam_tela,'White',self.tent_rect.inflate(self.quad))
        self.tam_tela.blit(tentar,self.tent_rect)
        pygame.draw.rect(self.tam_tela,'Gold',self.tent_rect.inflate(self.quad),5)

        sair = self.fonte_bot.render('(2) Quit',False,'Black')
        self.sair_rect = sair.get_rect(center = (pos_bots[0],pos_bots[1] + 150))
        pygame.draw.rect(self.tam_tela,'White',self.sair_rect.inflate(self.quad))
        self.tam_tela.blit(sair,self.sair_rect)
        pygame.draw.rect(self.tam_tela,'Gold',self.sair_rect.inflate(self.quad),5)

    def click(self):
        tecla = pygame.key.get_pressed()

        if tecla[pygame.K_1]:
            self.level.run()
            status['Vida'] = 3
            status['Pontos'] = 0
            status['Respawn'] = 1
            status['Nivel'] = 1

        if tecla[pygame.K_2]:
            pygame.quit()
            sys.exit()

    def run(self):
        self.escritas()
        self.click()
        