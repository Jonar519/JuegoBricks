def es_sudoku_valido(tablero):
    # Verifica filas
    for fila in tablero:
        if len(set(fila)) != 9 or any(not 1 <= num <= 9 for num in fila):
            return False
    
    # Verifica columnas
    for col in zip(*tablero):
        if len(set(col)) != 9:
            return False
    
    # Verifica subcuadrículas 3x3
    for i in range(0, 9, 3):
        for j in range(0, 9, 3):
            subgrid = [
                tablero[x][y]
                for x in range(i, i + 3)
                for y in range(j, j + 3)
            ]
            if len(set(subgrid)) != 9:
                return False
    return True