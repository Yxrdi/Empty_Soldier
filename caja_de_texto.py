import pygame
import os
import json
from constantes import *

class Caja_De_Texto:
    def __init__(self, x, y, ancho, alto, fuente):
        self.rectangulo = pygame.Rect(x, y, ancho, alto)
        self.color_inactivo = pygame.Color(BLANCO_OSCURO)
        self.color_activo = pygame.Color(BLANCO)
        self.color = self.color_inactivo
        self.fuente = fuente
        self.texto = ''
        self.superficie_texto = self.fuente.render(self.texto, True, pygame.Color(BLANCO))
        self.activa = False

    def manejar_evento(self, evento):
        if evento.type == pygame.MOUSEBUTTONDOWN:
            self.activa = self.rectangulo.collidepoint(evento.pos)
            if self.activa:
                self.color = self.color_activo
            else:
                self.color = self.color_inactivo

        if (evento.type == pygame.KEYDOWN) and self.activa:
            if evento.key == pygame.K_RETURN:
                self.guardar_texto_auto(self.texto)
                self.texto = ""
                    
            elif evento.key == pygame.K_BACKSPACE:
                self.texto = self.texto[:-1]
            else:
                self.texto += evento.unicode
            self.superficie_texto = self.fuente.render(self.texto, True, pygame.Color(BLANCO))

    def actualizar(self):
        ancho = max(500, self.superficie_texto.get_width() + 10)
        self.rectangulo.w = ancho

    def dibujar(self, pantalla):
        pantalla.blit(self.superficie_texto, (self.rectangulo.x + 5, self.rectangulo.y + 10))
        pygame.draw.rect(pantalla, self.color, self.rectangulo, 2)

    def guardar_texto(self, nombre_clave, nuevo_texto):
        nuevo_texto = nuevo_texto.strip()
        if not nuevo_texto or not nombre_clave:
            return

        datos = {}

        if os.path.exists("datos.json"):
            with open("datos.json", "r", encoding="utf-8") as archivo:
                try:
                    contenido = json.load(archivo)
                    if isinstance(contenido, dict):
                        datos = contenido
                except json.JSONDecodeError:
                    datos = {}

        datos[nombre_clave] = nuevo_texto

        with open("datos.json", "w", encoding="utf-8") as archivo:
            json.dump(datos, archivo, ensure_ascii=False, indent=4)

        print(f"Texto guardado bajo la clave '{nombre_clave}': {nuevo_texto}")

    def guardar_texto_auto(self, nuevo_texto):
        """Genera una clave automáticamente para guardar el texto"""
        datos = {}
        if os.path.exists("datos.json"):
            with open("datos.json", "r", encoding="utf-8") as archivo:
                try:
                    contenido = json.load(archivo)
                    if isinstance(contenido, dict):
                        datos = contenido
                except json.JSONDecodeError:
                    datos = {}

        # clave única
        
        clave = "texto_1"

        self.guardar_texto(clave, nuevo_texto)
