import pytest
from src.sudoku import es_sudoku_valido

def test_sudoku_valido():
    tablero_valido = [
        [5, 3, 4, 6, 7, 8, 9, 1, 2],
        [6, 7, 2, 1, 9, 5, 3, 4, 8],
        [1, 9, 8, 3, 4, 2, 5, 6, 7],
        [8, 5, 9, 7, 6, 1, 4, 2, 3],
        [4, 2, 6, 8, 5, 3, 7, 9, 1],
        [7, 1, 3, 9, 2, 4, 8, 5, 6],
        [9, 6, 1, 5, 3, 7, 2, 8, 4],
        [2, 8, 7, 4, 1, 9, 6, 3, 5],
        [3, 4, 5, 2, 8, 6, 1, 7, 9]
    ]
    assert es_sudoku_valido(tablero_valido) is True

def test_sudoku_invalido_fila():
    tablero_invalido = [
        [5, 5, 5, 6, 7, 8, 9, 1, 2],  # Fila con números repetidos
        [6, 7, 2, 1, 9, 5, 3, 4, 8],
        # ... resto del tablero ...
    ]
    assert es_sudoku_valido(tablero_invalido) is False