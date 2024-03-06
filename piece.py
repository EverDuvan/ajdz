import pygame

class Piece:
    def __init__(self, name, color, x, y):
        self.name = name
        self.color = color
        self.image = pygame.image.load(f'pieces/{name}{color}.png')
        self.image = pygame.transform.scale(self.image, (80, 80))
        self.x = x
        self.y = y
        # Inicializa el atributo rect con las coordenadas y dimensiones de la imagen
        self.rect = self.image.get_rect()
        self.rect.x = x * 80
        self.rect.y = y * 80

    def move(self, new_x, new_y):
        self.x = new_x
        self.y = new_y
        # Actualiza el atributo rect con la nueva posición
        self.rect.x = new_x * 80
        self.rect.y = new_y * 80

    @property
    def draw(self):
        # Dibuja la imagen en la pantalla utilizando el atributo rect
        return screen.blit(self.image, self.rect)

    def is_valid_move(self, new_x, new_y):
            if self.name == 'Knight':
                knight_moves = [(1, 2), (2, 1), (-1, 2), (2, -1), (-1, -2), (-2, -1), (1, -2), (-2, 1)]
                return (new_x - self.x, new_y - self.y) in knight_moves and (0 <= new_x <= 7) and (0 <= new_y <= 7)
            elif self.name == 'Rook':
                rook_moves = [(1, 0), (0, 1), (-1, 0), (0, -1), (1, 1), (-1, 1), (1, -1), (-1, -1)]
                return (new_x - self.x, new_y - self.y) in rook_moves and (0 <= new_x <= 7) and (0 <= new_y <= 7)
            elif self.name == 'Bishop':
                 bishop_moves = [(1, 1), (-1, 1), (1, -1), (-1, -1)]
                 return (new_x - self.x, new_y - self.y) in bishop_moves and (0 <= new_x <= 7) and (0 <= new_y <= 7)
            elif self.name == 'Queen':
                queen_moves = [(1, 0), (0, 1), (-1, 0), (0, -1), (1, 1), (-1, 1), (1, -1), (-1, -1)]
                return (new_x - self.x, new_y - self.y) in queen_moves and (0 <= new_x <= 7) and (0 <= new_y <= 7)
            elif self.name == 'King':
                 kinng_moves = [(1, 0), (0, 1), (-1, 0), (0, -1), (1, 1), (-1, 1), (1, -1), (-1, -1)]
                 return (new_x - self.x, new_y - self.y) in kinng_moves and (0 <= new_x <= 7) and (0 <= new_y <= 7)
            elif self.name == 'Pawn':
                if self.color == 'White':
                    # Movimiento especial del peón blanco en su primer movimiento (dos casillas hacia arriba)
                    if self.y == 6 and new_y == 4 and new_x == self.x:
                        return True
                    # Movimiento normal del peón blanco (una casilla hacia arriba)
                    elif new_y == self.y - 1 and new_x == self.x:
                        return True
                    # Captura en diagonal hacia la izquierda
                    elif new_y == self.y - 1 and (new_x == self.x - 1 or new_x == self.x + 1):
                        return True
                elif self.color == 'Black':
                    # Movimiento especial del peón negro en su primer movimiento (dos casillas hacia abajo)
                    if self.y == 1 and new_y == 3 and new_x == self.x:
                        return True
                    # Movimiento normal del peón negro (una casilla hacia abajo)
                    elif new_y == self.y + 1 and new_x == self.x:
                        return True
                    # Captura en diagonal hacia la derecha
                    elif new_y == self.y + 1 and (new_x == self.x - 1 or new_x == self.x + 1):
                        return True

# Configuración de la ventana
WIDTH, HEIGHT = 640, 640
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Chamanco")
# Colores
WHITE = (255, 255, 255)
BLACK = (100, 100, 100)

rookw = Piece('Rook', 'White', 0, 7)
knightw = Piece('Knight', 'White', 1, 7)
bishopw = Piece('Bishop', 'White', 2, 7)
queenw = Piece('Queen', 'White', 3, 7)
kingw = Piece('King', 'White', 4, 7)
bishopw2 = Piece('Bishop', 'White', 5, 7)
knightw2 = Piece('Knight', 'White', 6, 7)
rookw2 = Piece('Rook', 'White', 7, 7)
pawnw1 = Piece('Pawn', 'White', 0, 6)
pawnw2 = Piece('Pawn', 'White', 1, 6)
pawnw3 = Piece('Pawn', 'White', 2, 6)
pawnw4 = Piece('Pawn', 'White', 3, 6)
pawnw5 = Piece('Pawn', 'White', 4, 6)
pawnw6 = Piece('Pawn', 'White', 5, 6)
pawnw7 = Piece('Pawn', 'White', 6, 6)
pawnw8 = Piece('Pawn', 'White', 7, 6)
rookb = Piece('Rook', 'Black', 0, 0)
knightb = Piece('Knight', 'Black', 1, 0)
bishopb = Piece('Bishop', 'Black', 2, 0)
queenb = Piece('Queen', 'Black', 3, 0)
kingb = Piece('King', 'Black', 4, 0)
bishopb2 = Piece('Bishop', 'Black', 5, 0)
knightb2 = Piece('Knight', 'Black', 6, 0)
rookb2 = Piece('Rook', 'Black', 7, 0)
pawnb1 = Piece('Pawn', 'Black', 0, 1)
pawnb2 = Piece('Pawn', 'Black', 1, 1)
pawnb3 = Piece('Pawn', 'Black', 2, 1)
pawnb4 = Piece('Pawn', 'Black', 3, 1)
pawnb5 = Piece('Pawn', 'Black', 4, 1)
pawnb6 = Piece('Pawn', 'Black', 5, 1)
pawnb7 = Piece('Pawn', 'Black', 6, 1)
pawnb8 = Piece('Pawn', 'Black', 7, 1)

pieces= [rookw,
        knightw,
        bishopw,
        queenw,
        kingw,
        bishopw2,
        knightw2,
        rookw2,
        pawnw1,
        pawnw2,
        pawnw3,
        pawnw4,
        pawnw5,
        pawnw6,
        pawnw7,
        pawnw8,
        rookb,
        knightb,
        bishopb,
        queenb,
        kingb,
        bishopb2,
        knightb2,
        rookb2,
        pawnb1,
        pawnb2,
        pawnb3,
        pawnb4,
        pawnb5,
        pawnb6,
        pawnb7,
        pawnb8,
        ]