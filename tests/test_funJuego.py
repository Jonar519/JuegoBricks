import pytest
from src.funJuego import iniciar_juego, mover_personaje, finalizar_juego

def test_iniciar_juego(capsys):
    iniciar_juego()
    captured = capsys.readouterr()
    assert captured.out == "¡Iniciando juego!!!\n"

def test_mover_personaje(capsys):
    # Prueba con dirección válida
    mover_personaje("derecha")
    captured = capsys.readouterr()
    assert captured.out == "Moviendo personaje hacia derecha\n"

    # Prueba con otra dirección
    mover_personaje("arriba")
    captured = capsys.readouterr()
    assert captured.out == "Moviendo personaje hacia arriba\n"

def test_finalizar_juego(capsys):
    finalizar_juego()
    captured = capsys.readouterr()
    assert captured.out == "¡Fin del juego!!\n"

def test_flujo_completo_juego(capsys):
    # Simula el flujo completo del juego
    iniciar_juego()
    mover_personaje("izquierda")
    finalizar_juego()
    
    captured = capsys.readouterr()
    expected_output = (
        "¡Iniciando juego!!!\n"
        "Moviendo personaje hacia izquierda\n"
        "¡Fin del juego!!\n"
    )
    assert captured.out == expected_output