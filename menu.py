import pygame, sys
import json
from boton import Boton
from fuente import obtener_fuente
from caja_de_texto import *
from constantes import *


class Menu:
    def __init__(self):
        pygame.init
        self.pantalla = pygame.display.set_mode((WIGHT, HEIGHT))
        pygame.display.set_caption(TITULO_JUEGO)
        
        self.fondo = pygame.image.load(FONDO)
        self.reloj = pygame.time.Clock()
        self.fuente = pygame.font.Font(TIPO_LETRA,FUENTE_BARRA)
        self.caja = Caja_De_Texto((WIGHT - ANCHO_BARRA)/2, HEIGHT/2, ANCHO_BARRA, ALTO_BARRA, self.fuente)
        self.ejecutando = True
        self.menu_principal()
        #self.jugar()
        self.opciones()
        self.creditos()
        self.graficos()
        self.audio()
        self.nombre_personaje()
    
    def controles(self):
        while True:
            
            pos_mouse_opciones= pygame.mouse.get_pos()
            
            self.pantalla.blit(self.fondo, (0, 0))
            
            texto_controles = obtener_fuente(45).render(CONTROLES, True, BLANCO)
            rect_controles = texto_controles.get_rect(center=(WIGHT/2, 150))
            self.pantalla.blit(texto_controles, rect_controles)
            
            volver_opciones = Boton(imagen=None, posicion=(50, 20), texto_entrada=RETROCEDER, 
                                    fuente=obtener_fuente(20), color_base=BLANCO_OSCURO, color_hovering=BLANCO)
            volver_opciones.cambiarColor(pos_mouse_opciones)
            volver_opciones.actualizar(self.pantalla)
            
            for evento in pygame.event.get():
                if evento.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if evento.type == pygame.MOUSEBUTTONDOWN:
                    if volver_opciones.verificarEntrada(pos_mouse_opciones):
                        self.opciones()

            pygame.display.update()
    
    def nombre_personaje(self):
        while True:
            pos_mouse_opciones= pygame.mouse.get_pos()

            self.pantalla.blit(self.fondo, (0, 0))
            
            
            texto_nombre = obtener_fuente(45).render(NOMBRE_PERSONAJE, True, BLANCO)
            rect_nombre = texto_nombre.get_rect(center=(WIGHT/2, 300))
            self.pantalla.blit(texto_nombre, rect_nombre)
            
            volver_opciones = Boton(imagen=None, posicion=(50, 20), texto_entrada=RETROCEDER, 
                                    fuente=obtener_fuente(20), color_base=BLANCO_OSCURO, color_hovering=BLANCO)
            volver_opciones.cambiarColor(pos_mouse_opciones)
            volver_opciones.actualizar(self.pantalla)
            
            for evento in pygame.event.get():
                if evento.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if evento.type == pygame.MOUSEBUTTONDOWN:
                    if volver_opciones.verificarEntrada(pos_mouse_opciones):
                        self.menu_principal()
                
                self.caja.manejar_evento(evento)
            
                if evento.type == pygame.KEYDOWN:
                    if evento.key == pygame.K_RETURN:
                        self.menu_principal()
                
                

            self.caja.actualizar()
            self.caja.dibujar(self.pantalla)
            pygame.display.flip()
            self.reloj.tick(30)

            pygame.display.update()
    
    def graficos(self):
        while True:
            
            pos_mouse_opciones= pygame.mouse.get_pos()

            self.pantalla.blit(self.fondo, (0, 0))
            
            texto_graficos = obtener_fuente(45).render(GRAFICOS, True, BLANCO)
            rect_graficos = texto_graficos.get_rect(center=(WIGHT/2, HEIGHT/4))
            self.pantalla.blit(texto_graficos, rect_graficos)
            
            volver_opciones = Boton(imagen=None, posicion=(50, 20), texto_entrada=RETROCEDER, 
                                    fuente=obtener_fuente(20), color_base=BLANCO_OSCURO, color_hovering=BLANCO)
            volver_opciones.cambiarColor(pos_mouse_opciones)
            volver_opciones.actualizar(self.pantalla)
            
            for evento in pygame.event.get():
                if evento.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if evento.type == pygame.MOUSEBUTTONDOWN:
                    if volver_opciones.verificarEntrada(pos_mouse_opciones):
                        self.opciones()

            pygame.display.update()
            
    def audio(self):
        while True:

            pos_mouse_opciones= pygame.mouse.get_pos()
            
            self.pantalla.blit(self.fondo, (0, 0))
            
            texto_audio = obtener_fuente(45).render(AUDIO, True, BLANCO)
            rect_audio = texto_audio.get_rect(center=(WIGHT/2, HEIGHT/4))
            self.pantalla.blit(texto_audio, rect_audio)
            
            volver_opciones = Boton(imagen=None, posicion=(50, 20), texto_entrada=RETROCEDER, 
                                    fuente=obtener_fuente(20), color_base=BLANCO_OSCURO, color_hovering=BLANCO)
            volver_opciones.cambiarColor(pos_mouse_opciones)
            volver_opciones.actualizar(self.pantalla)
            
            for evento in pygame.event.get():
                if evento.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if evento.type == pygame.MOUSEBUTTONDOWN:
                    if volver_opciones.verificarEntrada(pos_mouse_opciones):
                        self.opciones()

            pygame.display.update()
            
    def opciones(self):
        while True:
            
            pos_mouse_opciones= pygame.mouse.get_pos()

            self.pantalla.blit(self.fondo, (0, 0))

            texto_opciones = obtener_fuente(45).render(OPCIONES, True, BLANCO)
            rect_opciones = texto_opciones.get_rect(center=(WIGHT/2, HEIGHT/4))
            self.pantalla.blit(texto_opciones, rect_opciones)

            volver_opciones = Boton(imagen=None, posicion=(50, 20), texto_entrada=RETROCEDER, 
                                    fuente=obtener_fuente(20), color_base=BLANCO_OSCURO, color_hovering=BLANCO)
            volver_opciones.cambiarColor(pos_mouse_opciones)
            volver_opciones.actualizar(self.pantalla)
            
            graficos = Boton(imagen=None, posicion=(WIGHT/2, HEIGHT/2), texto_entrada=GRAFICOS,
                                    fuente=obtener_fuente(20), color_base=BLANCO_OSCURO, color_hovering=BLANCO)
            graficos.cambiarColor(pos_mouse_opciones)
            graficos.actualizar(self.pantalla)
            
            audio = Boton(imagen=None, posicion=(WIGHT/2, (HEIGHT/1.8)), texto_entrada=AUDIO,
                        fuente=obtener_fuente(20), color_base=BLANCO_OSCURO, color_hovering=BLANCO)
            audio.cambiarColor(pos_mouse_opciones)
            audio.actualizar(self.pantalla)
            
            controles = Boton(imagen=None, posicion=(WIGHT/2, HEIGHT/1.636), texto_entrada=CONTROLES,
                        fuente=obtener_fuente(20), color_base=BLANCO_OSCURO, color_hovering=BLANCO)
            controles.cambiarColor(pos_mouse_opciones)
            controles.actualizar(self.pantalla)

            for evento in pygame.event.get():
                if evento.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if evento.type == pygame.MOUSEBUTTONDOWN:
                    if volver_opciones.verificarEntrada(pos_mouse_opciones):
                        self.menu_principal()
                    if graficos.verificarEntrada(pos_mouse_opciones):
                        self.graficos()
                    if audio.verificarEntrada(pos_mouse_opciones):
                        self.audio()
                    if controles.verificarEntrada(pos_mouse_opciones):
                        self.controles()

            pygame.display.update()

    def creditos(self):
        while True:

            pos_mouse_opciones= pygame.mouse.get_pos()
            
            self.pantalla.blit(self.fondo, (0, 0))
            
            texto_opciones = obtener_fuente(45).render(LISTA[0], True, BLANCO)
            rect_opciones = texto_opciones.get_rect(center=(WIGHT/2, HEIGHT/4))
            self.pantalla.blit(texto_opciones, rect_opciones)
            
            for i in range(1, len(LISTA)):
                texto_opciones = obtener_fuente(20).render(LISTA[i], True, BLANCO)
                rect_opciones = texto_opciones.get_rect(center=(WIGHT/2, 300 + i * 40))
                self.pantalla.blit(texto_opciones, rect_opciones)

            volver_opciones = Boton(imagen=None, posicion=(50, 20), texto_entrada=RETROCEDER, 
                                    fuente=obtener_fuente(20), color_base=BLANCO_OSCURO, color_hovering=BLANCO)

            volver_opciones.cambiarColor(pos_mouse_opciones)
            volver_opciones.actualizar(self.pantalla)

            for evento in pygame.event.get():
                if evento.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if evento.type == pygame.MOUSEBUTTONDOWN:
                    if volver_opciones.verificarEntrada(pos_mouse_opciones):
                        self.menu_principal()

            pygame.display.update()
    
    def menu_principal(self):
        while True:
            
            pos_mouse_opciones= pygame.mouse.get_pos()
            
            self.pantalla.blit(self.fondo, (0, 0))

            texto_menu = obtener_fuente(80).render(TITULO_JUEGO, True, BLANCO)
            rect_menu = texto_menu.get_rect(center=(WIGHT/2, HEIGHT/4))

            boton_jugar = Boton(imagen=None, posicion=(WIGHT/2, HEIGHT/1.6), texto_entrada=INICIAR_PARTIDA, 
                                fuente=obtener_fuente(25), color_base=BLANCO_OSCURO, color_hovering=BLANCO)
            
            boton_opciones = Boton(imagen=None, posicion=(WIGHT/2, HEIGHT/1.44), texto_entrada=OPCIONES,
                                fuente=obtener_fuente(25), color_base=BLANCO_OSCURO, color_hovering=BLANCO)
            
            boton_creditos = Boton(imagen=None, posicion=(WIGHT/2, HEIGHT/1.31), texto_entrada=CREDITOS,
                                fuente=obtener_fuente(25), color_base=BLANCO_OSCURO, color_hovering=BLANCO)
            
            boton_salir = Boton(imagen=None, posicion=(WIGHT/2, HEIGHT/1.2), texto_entrada=SALIR_DEL_JUEGO, 
                                fuente=obtener_fuente(25), color_base=BLANCO_OSCURO, color_hovering=BLANCO)

            self.pantalla.blit(texto_menu, rect_menu)

            for boton in [boton_jugar, boton_opciones, boton_creditos, boton_salir]:
                boton.cambiarColor(pos_mouse_opciones)
                boton.actualizar(self.pantalla)
            
            for evento in pygame.event.get():
                if evento.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if evento.type == pygame.MOUSEBUTTONDOWN:
                    if boton_jugar.verificarEntrada(pos_mouse_opciones):
                        self.nombre_personaje()
                    if boton_opciones.verificarEntrada(pos_mouse_opciones):
                        self.opciones()
                    if boton_creditos.verificarEntrada(pos_mouse_opciones):
                        self.creditos()
                    if boton_salir.verificarEntrada(pos_mouse_opciones):
                        pygame.quit()
                        sys.exit()

            pygame.display.update()
