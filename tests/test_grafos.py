import pytest
from src.grafos import tiene_ciclo

def test_ciclo_detectado():
    # Secuencia con ciclo: 0 -> 1 -> 2 -> 3 -> 1 -> ...
    secuencia_con_ciclo = [1, 2, 3, 1]
    assert tiene_ciclo(secuencia_con_ciclo) is True

def test_sin_ciclo():
    secuencia_sin_ciclo = [1, 2, 3, None]  # Termina en None
    assert tiene_ciclo(secuencia_sin_ciclo) is False