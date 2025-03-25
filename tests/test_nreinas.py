import pytest
from src.nreinas import resolver_nreinas, es_seguro

def test_es_seguro():
    tablero = [[0] * 4 for _ in range(4)]
    tablero[0][1] = 1  # Coloca una reina en (0,1)
    assert es_seguro(tablero, 1, 3, 4) is True  # Posición segura
    assert es_seguro(tablero, 1, 1, 4) is False  # Misma columna

def test_resolver_4_reinas():
    N = 4
    tablero = [[0] * N for _ in range(N)]
    assert resolver_nreinas(tablero, 0, N) is True
    # Verifica que hay exactamente una reina por fila/columna
    assert sum(sum(fila) for fila in tablero) == N