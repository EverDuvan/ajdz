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
            #new_x, new_y = snap_to_grid(new_x, new_y)
            # Verifica si el movimiento es válido para la pieza seleccionada
            if selected_piece.is_valid_move(new_x // 80, new_y // 80):
                if current_turn == selected_piece.color:
                    print (f'pieza: {selected_piece.color}, turno: {current_turn}')
                    selected_piece.move(new_x // 80, new_y // 80)
                    current_turn = 'Black'
                elif selected_piece.is_valid_move(new_x // 80, new_y // 80) and current_turn == selected_piece.color:
                    print (f'pieza: {selected_piece.color}, turno: {current_turn}')
                    selected_piece.move(new_x // 80, new_y // 80)
                    current_turn = 'White'
            #else:
                #print('Invalid move')

    screen.fill((255, 255, 255))

    for row in range(8):
        for col in range(8):
            color = WHITE if (row + col) % 2 == 0 else BLACK
            pygame.draw.rect(screen, color, (col * 80, row * 80, 80, 80))

    for piece in pieces:
        piece.draw(screen)

    pygame.display.update()
pygame.quit()