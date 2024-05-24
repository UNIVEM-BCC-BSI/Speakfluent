import pygame, sys
from config import *
from menu import Menu
from level import level
from gmov import gameover

class Jogo:
    def __init__(self):
        
        #setup geral
        pygame.init()
        self.tela = pygame.display.set_mode((largura, altura))
        pygame.display.set_caption('Speakfluent')
        self.clock = pygame.time.Clock()

        self.menu = Menu()
        self.Level = level()
        self.gameover = gameover()

    def run(self):
        while True:
            for evento in pygame.event.get():
                if evento.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            if status['Nivel'] == 0:
                self.tela.fill(COR_FUNDO_MENU)
                self.menu.run()
                pygame.display.update()
                self.clock.tick(fps)
            if status['Nivel'] == 1:
                self.tela.fill('black')
                self.Level.run()
                pygame.display.update()
                self.clock.tick(fps)
            if status['Nivel'] == 2:
                pass
            if status['Nivel'] == 3:
                pass               
            if status['Nivel'] == 4:
                self.tela.fill(COR_FUNDO_GAMEOVER)
                self.gameover.run()
                pygame.display.update()
                self.clock.tick(fps)

if __name__ == '__main__':
    jogo = Jogo()
    jogo.run()