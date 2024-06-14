import pygame, sys
from config import *

class Menu:
    def __init__(self):
        self.tam_tela = pygame.display.get_surface()

        self.fonte_titulo = pygame.font.Font(UI_fonte, 120)
        self.fonte_bot = pygame.font.Font(UI_fonte, 60)

        self.quad = (60,60)

        self.nivel = status['Nivel']

    def escritas(self):
        titulo = self.fonte_titulo.render('Speakfluent',False,'Black')
        x = self.tam_tela.get_size()[0] / 2
        y = 100
        self.titulo_rect = titulo.get_rect(center = (x,y))
        self.tam_tela.blit(titulo, self.titulo_rect)

        pos_bots = (self.tam_tela.get_size()[0] / 2,
                    self.tam_tela.get_size()[1] / 2)

        start = self.fonte_bot.render('Start',False,'Black')
        self.start_rect = start.get_rect(center = (pos_bots))
        pygame.draw.rect(self.tam_tela,'White',self.start_rect.inflate(self.quad))
        self.tam_tela.blit(start,self.start_rect)
        pygame.draw.rect(self.tam_tela,'Black',self.start_rect.inflate(self.quad),5)

        sair = self.fonte_bot.render('Quit',False,'Black')
        self.sair_rect = sair.get_rect(center = (pos_bots[0],pos_bots[1] + 150))
        pygame.draw.rect(self.tam_tela,'White',self.sair_rect.inflate(self.quad))
        self.tam_tela.blit(sair,self.sair_rect)
        pygame.draw.rect(self.tam_tela,'Black',self.sair_rect.inflate(self.quad),5)
    
    def click(self):
        if pygame.mouse.get_pressed()[0] == 1:
            self.pos_mouse = pygame.mouse.get_pos()
            if self.start_rect.collidepoint(self.pos_mouse):
                status['Nivel'] = 1
            elif self.sair_rect.collidepoint(self.pos_mouse):
                pygame.quit()
                sys.exit()

    def run(self):
        self.escritas()
        self.click()