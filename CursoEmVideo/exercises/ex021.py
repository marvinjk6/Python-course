''' TOCANDO UM MP3
Faça um programa em Python que abra e Reproduza o áudio de um arquivo MP3


Para fazer esse desafio o Guanabara usou um módulo chamado pygame
Instalar: pip install pygame
'''

import pygame
pygame.init()
pygame.mixer.music.load('Coloque o nome do arquivo')
pygame.mixer.music.play()
pygame.event.wait()
