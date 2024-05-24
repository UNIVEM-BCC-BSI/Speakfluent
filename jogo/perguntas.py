import pygame
from config import *

class PERG:
    def __init__(self):
        self.tam_tela = pygame.display.get_surface()
        self.fonte_inter = pygame.font.Font(UI_fonte, UI_fonte_inter)

        self.tam_quad = (200,50)

        self.pos_mouse = [0,0]
        self.respondeu = False

        self.esp_click = 900
        self.click = True
        self.temp_click = pygame.time.get_ticks()

        self.resp = ''

        self.vida = status['Vida']
        self.ponto = status['Pontos']
        self.cont = 0

    def inter(self, i, p , tipo):

        pos_msg = (self.tam_tela.get_size()[0] / 2, self.tam_tela.get_size()[1] / 2)

        if tipo == 'Perg':
            self.alt1 = p[i][1]
            self.alt2 = p[i][2]
            self.alt3 = p[i][3]
            self.alt4 = p[i][4]
            self.correta = p[i][5]

            #Pergunta
            text = self.fonte_inter.render(p[i][0], False, COR_PERG)
            x = self.tam_tela.get_size()[0] / 2
            y = 90
            text_rect = text.get_rect(center = (x,y))
            pygame.draw.rect(self.tam_tela,UI_BG_COR_PERG,text_rect.inflate(self.tam_quad))
            self.tam_tela.blit(text, text_rect)
            pygame.draw.rect(self.tam_tela,'Black',text_rect.inflate(self.tam_quad),3)

            #Resp 001
            resp1 = self.fonte_inter.render(self.alt1, False, COR_PERG)
            posA = (self.tam_tela.get_size()[0] / 2, self.tam_tela.get_size()[1] / 2)

            self.resp1_rect = resp1.get_rect(center = (posA))
            pygame.draw.rect(self.tam_tela,UI_BG_COR_PERG,self.resp1_rect.inflate(self.tam_quad))
            self.tam_tela.blit(resp1, self.resp1_rect)
            pygame.draw.rect(self.tam_tela,'Black',self.resp1_rect.inflate(self.tam_quad),3)

            #Resp 002

            resp2 = self.fonte_inter.render(self.alt2, False, COR_PERG)
            posB = (posA[0], posA[1] + 100)

            self.resp2_rect = resp1.get_rect(center = (posB))
            pygame.draw.rect(self.tam_tela,UI_BG_COR_PERG,self.resp2_rect.inflate(self.tam_quad))
            self.tam_tela.blit(resp2, self.resp2_rect)
            pygame.draw.rect(self.tam_tela,'Black',self.resp2_rect.inflate(self.tam_quad),3)

            #Resp 003

            resp3 = self.fonte_inter.render(self.alt3, False, COR_PERG)
            posC = (posB[0], posB[1] + 100)

            self.resp3_rect = resp3.get_rect(center = (posC))
            pygame.draw.rect(self.tam_tela,UI_BG_COR_PERG,self.resp3_rect.inflate(self.tam_quad))
            self.tam_tela.blit(resp3, self.resp3_rect)
            pygame.draw.rect(self.tam_tela,'Black',self.resp3_rect.inflate(self.tam_quad),3)

            #Resp 004

            resp4 = self.fonte_inter.render(self.alt4, False, COR_PERG)
            posD = (posC[0], posC[1] + 100)

            self.resp4_rect = resp4.get_rect(center = posD)
            pygame.draw.rect(self.tam_tela,UI_BG_COR_PERG,self.resp4_rect.inflate(self.tam_quad))
            self.tam_tela.blit(resp4,self.resp4_rect)
            pygame.draw.rect(self.tam_tela,'Black',self.resp4_rect.inflate(self.tam_quad),3)

            self.Resp()

        elif tipo == 'Acerto':
            msg = self.fonte_inter.render(p[0],False, COR_PERG)
            self.msg_rect = msg.get_rect(center = pos_msg)
            pygame.draw.rect(self.tam_tela,UI_BG_COR_PERG,self.msg_rect.inflate(self.tam_quad))
            self.tam_tela.blit(msg,self.msg_rect)
            pygame.draw.rect(self.tam_tela,'Black',self.msg_rect.inflate(self.tam_quad),3)

        elif tipo == 'Erro':
            msg = self.fonte_inter.render(p[1],False,COR_PERG)
            self.msg_rect = msg.get_rect(center = pos_msg)
            pygame.draw.rect(self.tam_tela,UI_BG_COR_PERG,self.msg_rect.inflate(self.tam_quad))
            self.tam_tela.blit(msg,self.msg_rect)
            pygame.draw.rect(self.tam_tela,'Black',self.msg_rect.inflate(self.tam_quad),3)

        elif tipo == 'Fim':
            msg = self.fonte_inter.render(p[2],False,COR_PERG)
            self.msg_rect = msg.get_rect(center = pos_msg)
            pygame.draw.rect(self.tam_tela,UI_BG_COR_PERG,self.msg_rect.inflate(self.tam_quad))
            self.tam_tela.blit(msg,self.msg_rect)
            pygame.draw.rect(self.tam_tela,'Black',self.msg_rect.inflate(self.tam_quad),3)
        
    def Resp(self):
        
        if pygame.mouse.get_pressed()[0] == 1:
            self.pos_mouse = pygame.mouse.get_pos()
            if self.resp1_rect.collidepoint(self.pos_mouse):
                if self.alt1 == self.correta:
                    self.resp = 'Acertou'
                    self.ponto += 1
                    self.cont += 1
                else:
                    self.resp = 'Errou'
                    self.vida -= 1
                    self.cont += 1
            if self.resp2_rect.collidepoint(self.pos_mouse):
                if self.alt2 == self.correta:
                    self.resp = 'Acertou'
                    self.ponto += 1
                    self.cont += 1
                else:
                    self.resp = 'Errou'
                    self.vida -= 1
                    self.cont += 1
            if self.resp3_rect.collidepoint(self.pos_mouse):
                if self.alt3 == self.correta:
                    self.resp = 'Acertou'
                    self.ponto += 1
                    self.cont += 1
                else:
                    self.resp = 'Errou'
                    self.vida -= 1
                    self.cont += 1
            if self.resp4_rect.collidepoint(self.pos_mouse):
                if self.alt4 == self.correta:
                    self.resp = 'Acertou'
                    self.ponto += 1
                    self.cont += 1
                else:
                    self.resp = 'Errou'
                    self.vida -= 1
                    self.cont += 1
            self.pos_mouse = pygame.mouse.set_pos([620,240])

            status['Vida'] = self.vida
            status['Pontos'] = self.ponto
