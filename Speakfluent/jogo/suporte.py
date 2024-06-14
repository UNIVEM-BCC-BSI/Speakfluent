from csv import reader
from os import walk
import pygame

pygame.init()

#Importa o mapa csv para o python e o organiza em matriz
def import_csv_layout(path):
    mapa_terreno = []
    with open(path) as mapa_do_nivel:
        layout = reader(mapa_do_nivel, delimiter = ',')
        for linha in layout:
            mapa_terreno.append(list(linha))
        return mapa_terreno

#Importa os elementos graficos do mapa csv
def import_folder(path):
    img_ls = []
    for _,__,img_arq in walk(path):
        for img in img_arq:
            path_comp = path + '/' + img
            img_surf = pygame.image.load(path_comp).convert_alpha()
            img_ls.append(img_surf)
    return img_ls