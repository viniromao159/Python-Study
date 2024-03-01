import pygame

pygame.init() #Inicia
pygame.mixer.music.load('musica.mp3') #Carrega
pygame.mixer.music.play() #toca
input()
pygame.event.wait()#Encerra após o fim
