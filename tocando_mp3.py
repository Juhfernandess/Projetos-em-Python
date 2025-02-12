#aça um programa em Python que abra e reproduza o áudio de um arquivo MP3.

import pygame

# Inicializa o mixer de som do pygame
pygame.mixer.init()

# Carrega o arquivo MP3
pygame.mixer.music.load("caminho/do/seu/arquivo.mp3")

# Reproduz o áudio
pygame.mixer.music.play()

# Aguarda até o áudio terminar
while pygame.mixer.music.get_busy():
    pygame.time.Clock().tick(10)
