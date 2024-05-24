import pygame
from config import *
from suporte import import_folder
from colis import colis
from random import randint
from perguntas import PERG

class Jogador(colis):
    def __init__(self, pos, grupos, obst_sprites):
        super().__init__(grupos)
        self.image = pygame.image.load('graficos/teste/player.png').convert_alpha()
        self.rect = self.image.get_rect(topleft = pos)
        self.hitbox = self.rect.inflate(0, -26)

        self.click = PERG()

        #Setup dos graficos
        self.assets_jogador()
        self.status = 'baixo'
        self.frame_index = 0
        self.anim_vel = 0.15

        #Movimentação
        self.direc = pygame.math.Vector2()
        self.velo = 5

        #Colisão
        self.obst_sprites = obst_sprites

        #Var de interação
        self.interac = False

        #Espera para interação
        self.esp_inter = 900

    def assets_jogador(self):
        path_jog = 'graficos/player/'
        self.anima = {
            'cima': [], 'baixo': [], 'esq': [], 'dir': [],
            'idle_cima': [], 'idle_baixo': [], 'idle_esq': [], 'idle_dir': []
        }

        for anim in self.anima.keys():
            path_comp = path_jog + anim
            self.anima[anim] = import_folder(path_comp)

    def stats(self):
        self.vida = status['Vida']
        self.pontos = status['Pontos']

        self.obj = objetivos[self.pontos]

    def input(self):

        teclas = pygame.key.get_pressed()

        #Mov Horizontal
        if teclas[pygame.K_w] or teclas[pygame.K_UP]:
            self.direc.y = -1
            self.status = 'cima'
        elif teclas[pygame.K_s] or teclas[pygame.K_DOWN]:
            self.direc.y = 1
            self.status = 'baixo'
        else:
            self.direc.y = 0

        #Mov Vertical
        if teclas[pygame.K_a] or teclas[pygame.K_LEFT]:
            self.direc.x = -1
            self.status = 'esq'
        elif teclas[pygame.K_d] or teclas[pygame.K_RIGHT]:
            self.direc.x = 1
            self.status = 'dir'
        else:
            self.direc.x = 0

        #Interação
        if teclas[pygame.K_e] and not self.interac:
            self.interac = True
            self.perg = randint(0,2)
            self.temp_inter = pygame.time.get_ticks()
    
    def get_status(self):

        #Status de idle
        if self.direc.x == 0 and self.direc.y == 0:
            if not 'idle' in self.status:
                self.status = 'idle_' + self.status

    def mov(self, velo):
        if self.direc.magnitude() != 0:
            self.direc = self.direc.normalize()
        
        self.hitbox.x += self.direc.x * velo
        self.colis('horizontal')
        self.hitbox.y += self.direc.y * velo
        self.colis('vertical')
        self.rect.center = self.hitbox.center

    def cooldown(self):
        temp_atual = pygame.time.get_ticks()

        if self.interac:
            if temp_atual - self.temp_inter >= self.esp_inter:
                self.interac = False

    def animacao(self):
        animacao = self.anima[self.status]

        #Loop de endereçamento de imagens
        self.frame_index += self.anim_vel
        if self.frame_index >= len(animacao):
            self.frame_index = 0

        #Adicionando imagens
        self.image = animacao[int(self.frame_index)]
        self.rect = self.image.get_rect(center = self.hitbox.center)

    def update(self):
        self.stats()
        self.input()
        self.mov(self.velo)
        self.get_status()
        self.animacao()
        self.cooldown()
