import pygame, sys
from boton import Boton

pygame.init()

def obtener_fuente(tamano):
    """Devuelve Press-Start-2P en el tamaño deseado"""
    return pygame.font.Font("assets/Alice_in_Wonderland_3.ttf", tamano)


