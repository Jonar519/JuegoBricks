import pytest
from src.grafos import tiene_ciclo

def test_ciclo_detectado():
    # Ciclo: 0→1→2→0 (valores: [1, 2, 0])
    assert tiene_ciclo([1, 2, 0]) is True

def test_sin_ciclo():
    assert tiene_ciclo([1, 2, 3, None]) is False  # Termina en None
    assert tiene_ciclo([None]) is False  # Solo un elemento None
    assert tiene_ciclo([]) is False  # Lista vacía

def test_ciclo_autorreferencia():
    # Ciclo: 0→0 (valor: [0])
    assert tiene_ciclo([0]) is True

def test_indices_fuera_de_rango():
    assert tiene_ciclo([1, 5]) is False  # 5 está fuera del rango
    assert tiene_ciclo([2, -1]) is False  # Índice negativo