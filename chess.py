import pygame
import sys
from piece import *

# Inicialización de pygame
pygame.init()

# Bucle principal del juego
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # Obtén la posición del mouse en la pantalla
            mouse_x, mouse_y = pygame.mouse.get_pos()
            # Calcula la posición del alfil blanco en la pantalla
            #bishopw.x * 80,  bishopw.y * 80
            # Comprueba si el mouse está dentro del alfil blanco
            if mouse_x >= bishopw.x * 80 and mouse_x <= bishopw.x * 80 + 80 and mouse_y >= bishopw.y * 80 and mouse_y <= bishopw.y * 80 + 80:
                print("Alfil blanco seleccionado")
            if mouse_x >= bishopb.x * 80 and mouse_x <= bishopb.x * 80 + 80 and mouse_y >= bishopb.y * 80 and mouse_y <= bishopb.y * 80 + 80:
                print("Alfil negro seleccionado")
                # Realiza alguna acción con el alfil blanco

    pygame.display.flip()
