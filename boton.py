import pygame

class Boton():
    def __init__(self, imagen, posicion, texto_entrada, fuente, color_base, color_hovering):
        self.imagen = imagen
        self.x_posicion = posicion[0]
        self.y_posicion = posicion[1]
        self.fuente = fuente
        self.color_base = color_base
        self.color_hovering = color_hovering
        self.texto_entrada = texto_entrada
        self.texto = self.fuente.render(self.texto_entrada, True, self.color_base)

        # Si no se proporciona una imagen, se usa el texto como imagen.
        if self.imagen is None:
            self.imagen = self.texto

        # Rectángulos para la imagen y el texto
        self.rect = self.imagen.get_rect(center=(self.x_posicion, self.y_posicion))
        self.rect_texto = self.texto.get_rect(center=(self.x_posicion, self.y_posicion))

    def actualizar(self, pantalla):
        #Actualiza la visualización del botón en la pantalla.
        if self.imagen is not None:
            pantalla.blit(self.imagen, self.rect)
        pantalla.blit(self.texto, self.rect_texto)

    def verificarEntrada(self, posicion):
        #Verifica si la posición del ratón está dentro del área del botón.
        return self.rect.collidepoint(posicion)

    def cambiarColor(self, posicion):
        #Cambia el color del texto dependiendo de si el ratón está sobre el botón.
        if self.verificarEntrada(posicion) == True:
            self.texto = self.fuente.render(self.texto_entrada, True, self.color_hovering)
        else:
            self.texto = self.fuente.render(self.texto_entrada, True, self.color_base)
