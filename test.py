class Piece:
    # Otras partes del código...

    def is_valid_move(self, new_x, new_y):
        if self.name == 'Knight':
            # Lógica para el caballo...
        elif self.name == 'Rook':
            # Movimiento horizontal o vertical hasta colisionar o capturar
            if (new_x == self.x or new_y == self.y) and not self._is_obstructed(new_x, new_y):
                return True
        elif self.name == 'Bishop':
            # Movimiento diagonal hasta colisionar o capturar
            if abs(new_x - self.x) == abs(new_y - self.y) and not self._is_obstructed(new_x, new_y):
                return True
        elif self.name == 'Queen':
            # Movimiento horizontal, vertical o diagonal hasta colisionar o capturar
            if ((new_x == self.x or new_y == self.y) or (abs(new_x - self.x) == abs(new_y - self.y))) \
                    and not self._is_obstructed(new_x, new_y):
                return True
        elif self.name == 'King':
            # Movimiento a una casilla adyacente hasta colisionar o capturar
            if abs(new_x - self.x) <= 1 and abs(new_y - self.y) <= 1:
                return True
        elif self.name == 'Pawn':
            # Lógica para el peón...

    def _is_obstructed(self, new_x, new_y):
        # Verifica si hay piezas en el camino del movimiento
        # Implementa lógica para detectar obstrucciones (otras piezas)
