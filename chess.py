import pygame
from piece import *

pygame.init()

moving = False
selected_piece = None
current_turn = 'White'

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
            # Verifica si el movimiento es válido para la pieza seleccionada
            if selected_piece.is_valid_move(new_x // 80, new_y // 80) and current_turn == selected_piece.color:
                destination_piece = None
                for piece in pieces:
                    if piece.rect.collidepoint(new_x, new_y):
                        destination_piece = piece
                        break
                
                if destination_piece is None or destination_piece.color != selected_piece.color:
                    if destination_piece is not None:
                        pieces.remove(destination_piece)  # Elimina la pieza del oponente
                    selected_piece.move(new_x // 80, new_y // 80)
                    current_turn = 'Black' if current_turn == 'White' else 'White'

    screen.fill((255, 255, 255))
    for row in range(8):
        for col in range(8):
            color = WHITE if (row + col) % 2 == 0 else BLACK
            pygame.draw.rect(screen, color, (col * 80, row * 80, 80, 80))
    for piece in pieces:
        piece.draw

    pygame.display.update()
pygame.quit()
