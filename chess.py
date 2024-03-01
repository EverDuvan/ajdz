import pygame
from piece import *
# Inicializa Pygame
pygame.init()

# Estado de movimiento y pieza seleccionada
moving = False
selected_piece = None

# Bucle principal del juego
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            for piece in pieces:
                if piece.rect.collidepoint(mouse_x, mouse_y):
                    moving = True
                    selected_piece = piece
                    break
        elif event.type == pygame.MOUSEBUTTONUP:
            moving = False
            selected_piece = None
        elif event.type == pygame.MOUSEMOTION and moving:
            new_x, new_y = pygame.mouse.get_pos()
            selected_piece.rect.x = new_x - selected_piece.rect.width // 2
            selected_piece.rect.y = new_y - selected_piece.rect.height // 2

    # Limpia la pantalla
    screen.fill((255, 255, 255))

    # Dibuja las casillas del tablero
    for row in range(8):
        for col in range(8):
            color = WHITE if (row + col) % 2 == 0 else BLACK
            pygame.draw.rect(screen, color, (col * 80, row * 80, 80, 80))

    # Dibuja las piezas
    for piece in pieces:
        piece.draw(screen)

    # Actualiza la pantalla
    pygame.display.update()
# Sal del programa
pygame.quit()
