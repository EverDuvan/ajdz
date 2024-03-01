import pygame

class Piece:
    def __init__(self, name, color, x, y):
        self.name = name
        self.color = color
        self.image = pygame.image.load(f'pieces/{name}{color}.png')
        self.image = pygame.transform.scale(self.image, (80, 80))
        self.x = x
        self.y = y

    def move(self, new_x, new_y):
        self.x = new_x
        self.y = new_y

    def draw(self, screen):
        screen.blit(self.image, (self.x * 80, self.y * 80))
    
    def is_valid_move(self, new_x, new_y):
        # Comprueba si el movimiento es diagonal y dentro del tablero
        return (abs(self.x - new_x) == abs(self.y - new_y)) and (0 <= new_x <= 7) and (0 <= new_y <= 7)

# Configuración de la ventana
WIDTH, HEIGHT = 640, 640
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Chamanco")

# Colores
WHITE = (255, 255, 255)
BLACK = (100, 100, 100)

for row in range(8):
    for col in range(8):
        color = WHITE if (row + col) % 2 == 0 else BLACK
        pygame.draw.rect(screen, color, (col * 80, row * 80, 80, 80))

    rookw = Piece('Rook', 'White', 0, 7)
    rookw.draw(screen)
    knightw = Piece('Knight', 'White', 1, 7)
    knightw.draw(screen)
    bishopw = Piece('Bishop', 'White', 2, 7)
    bishopw.draw(screen)
    queenw = Piece('Queen', 'White', 3, 7)
    queenw.draw(screen)
    kingw = Piece('King', 'White', 4, 7)
    kingw.draw(screen)
    bishopw2 = Piece('Bishop', 'White', 5, 7)
    bishopw2.draw(screen)
    knightw2 = Piece('Knight', 'White', 6, 7)
    knightw2.draw(screen)
    rookw2 = Piece('Rook', 'White', 7, 7)
    rookw2.draw(screen)
    pawnw1 = Piece('Pawn', 'White', 0, 6)
    pawnw1.draw(screen)
    pawnw2 = Piece('Pawn', 'White', 1, 6)
    pawnw2.draw(screen)
    pawnw3 = Piece('Pawn', 'White', 2, 6)
    pawnw3.draw(screen)
    pawnw4 = Piece('Pawn', 'White', 3, 6)
    pawnw4.draw(screen)
    pawnw5 = Piece('Pawn', 'White', 4, 6)
    pawnw5.draw(screen)
    pawnw6 = Piece('Pawn', 'White', 5, 6)
    pawnw6.draw(screen)
    pawnw7 = Piece('Pawn', 'White', 6, 6)
    pawnw7.draw(screen)
    pawnw8 = Piece('Pawn', 'White', 7, 6)
    pawnw8.draw(screen)
    rookb = Piece('Rook', 'Black', 0, 0)
    rookb.draw(screen)
    knightb = Piece('Knight', 'Black', 1, 0)
    knightb.draw(screen)
    bishopb = Piece('Bishop', 'Black', 2, 0)
    bishopb.draw(screen)
    queenb = Piece('Queen', 'Black', 3, 0)
    queenb.draw(screen)
    kingb = Piece('King', 'Black', 4, 0)
    kingb.draw(screen)
    bishopb2 = Piece('Bishop', 'Black', 5, 0)
    bishopb2.draw(screen)
    knightb2 = Piece('Knight', 'Black', 6, 0)
    knightb2.draw(screen)
    rookb2 = Piece('Rook', 'Black', 7, 0)
    rookb2.draw(screen)
    pawnb1 = Piece('Pawn', 'Black', 0, 1)
    pawnb1.draw(screen)
    pawnb2 = Piece('Pawn', 'Black', 1, 1)
    pawnb2.draw(screen)
    pawnb3 = Piece('Pawn', 'Black', 2, 1)
    pawnb3.draw(screen)
    pawnb4 = Piece('Pawn', 'Black', 3, 1)
    pawnb4.draw(screen)
    pawnb5 = Piece('Pawn', 'Black', 4, 1)
    pawnb5.draw(screen)
    pawnb6 = Piece('Pawn', 'Black', 5, 1)
    pawnb6.draw(screen)
    pawnb7 = Piece('Pawn', 'Black', 6, 1)
    pawnb7.draw(screen)
    pawnb8 = Piece('Pawn', 'Black', 7, 1)
    pawnb8.draw(screen)
    
