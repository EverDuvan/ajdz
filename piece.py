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

    def draw(self, screen):
        # Dibuja la imagen en la pantalla utilizando el atributo rect
        screen.blit(self.image, self.rect)
    
    def is_valid_move(self, new_x, new_y):
        # Comprueba si el movimiento es diagonal y dentro del tablero
        return (abs(self.x - new_x) == abs(self.y - new_y)) and (0 <= new_x <= 7) and (0 <= new_y <= 7)

##########################################################################################################

def snap_to_grid(x, y):
    """
    Redondea las coordenadas x e y al entero más cercano para ajustar a la cuadrícula.
    Además, ajusta las coordenadas para que las piezas se coloquen en el centro de las cuadrículas.
    """
    grid_size = 80 # Tamaño de la cuadrícula
    # Ajusta las coordenadas para que las piezas se coloquen en el centro de las cuadrículas
    return round(x / grid_size) * grid_size + grid_size // 2, round(y / grid_size) * grid_size + grid_size // 2

def is_grid_occupied(x, y, selected_piece):
    for piece in pieces:
        if piece != selected_piece and piece.rect.x // 80 == x and piece.rect.y // 80 == y:
            return True
    return False


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