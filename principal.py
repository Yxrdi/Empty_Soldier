import pygame, sys
from menu import*


class Juego:
    def __init__(self):
        pygame.init
        self.pantalla = pygame.display.set_mode((WIGHT, HEIGHT))
        pygame.display.set_caption(TITULO_JUEGO)
        self.menu = Menu()
        
    def bucle_juego(self):
        while True:
            self.pantalla.blit()
            for evento in pygame.event.get():
                if evento.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            self.menu.menu_principal()
                    
            pygame.display.update()
            
        
        
        
        
        

if __name__ == "__main__":
    juego = Juego()
    juego.bucle_juego()
    