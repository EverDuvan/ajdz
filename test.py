import pygame
import sys

# Inicialización de pygame
pygame.init()

# Configuración de la ventana
WIDTH, HEIGHT = 640, 640
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Ajedrez en Pygame")

# Colores
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

class Piece:
    def __init__(self, name, color, x, y):
        self.name = name
        self.color = color
        self.image = pygame.image.load(f'pieces/{name}{color}.png')
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

# Crear objetos de alfiles
bishop_white = Piece('Bishop', 'White', 2, 0)
bishop_black = Piece('Bishop', 'Black', 5, 7)

# Bucle principal del juego
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            new_x = mouse_x // 80
            new_y = 7 - (mouse_y // 80) # El tablero se invierte en el eje Y
            if bishops_selected:
                if bishops_selected.is_valid_move(new_x, new_y):
                    bishops_selected.move(new_x, new_y)
                    bishops_selected = None
                else:
                    print("Movimiento inválido")
            else:
                if bishop_white.is_valid_move(new_x, new_y):
                    bishop_white.move(new_x, new_y)
                elif bishop_black.is_valid_move(new_x, new_y):
                    bishop_black.move(new_x, new_y)

    # Dibuja el tablero
    for row in range(8):
        for col in range(8):
            color = WHITE if (row + col) % 2 == 0 else BLACK
            pygame.draw.rect(screen, color, (col * 80, row * 80, 80, 80))

    # Dibuja los alfiles
    bishop_white.draw(screen)
    bishop_black.draw(screen)

    pygame.display.flip()
