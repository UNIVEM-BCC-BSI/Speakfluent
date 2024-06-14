import pygame
from config import * 
from level import *
from perguntas import PERG

class UI:
    def __init__(self):
        #geral
        self.tam_tela = pygame.display.get_surface()
        self.fonte_ui = pygame.font.Font(UI_fonte, UI_fonte_tam)
        self.fonte_obj = pygame.font.Font(UI_fonte, UI_fonte_obj)
        self.fonte_inter = pygame.font.Font(UI_fonte, UI_fonte_inter)
        self.pergunt = PERG()
        self.c = 0

    def vida(self,vida):
        texto_tela = self.fonte_ui.render(f'Vidas: {int(vida)}', False, COR_TEXTO)
        x = 90
        y = 30
        texto_rect = texto_tela.get_rect(center = (x,y))

        pygame.draw.rect(self.tam_tela,UI_BG_COR,texto_rect.inflate(10,10))
        self.tam_tela.blit(texto_tela, texto_rect)
        pygame.draw.rect(self.tam_tela,'red',texto_rect.inflate(10,10),3)

    def obj(self,obj):
        texto_tela = self.fonte_obj.render(f'{obj}', False, COR_TEXTO)
        x = self.tam_tela.get_size()[0] / 2
        y = 30
        texto_rect = texto_tela.get_rect(center = (x,y))

        pygame.draw.rect(self.tam_tela,UI_BG_COR,texto_rect.inflate(10,10))
        self.tam_tela.blit(texto_tela,texto_rect)
        pygame.draw.rect(self.tam_tela,'lightgreen',texto_rect.inflate(10,10),3)   

    def display(self, w, v, p, tipo):
        self.vida(w.vida)
        self.obj(w.obj)
        if v:
            self.pergunt.inter(w.perg, p, tipo)
