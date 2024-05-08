import pygame, sys
from config import *
from level import level

class Jogo:
    def __init__(self):
        
        #setup geral
        pygame.init()
        self.tela = pygame.display.set_mode((largura, altura))
        pygame.display.set_caption('Zelda')
        self.clock = pygame.time.Clock()

        self.Level = level()

    def run(self):
        while True:
            for evento in pygame.event.get():
                if evento.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            self.tela.fill('Black')
            self.Level.run()
            pygame.display.update()
            self.clock.tick(fps)
            


if __name__ == '__main__':
    jogo = Jogo()
    jogo.run()