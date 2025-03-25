def es_seguro(tablero, fila, col, N):
    # Verifica la columna
    for i in range(fila):
        if tablero[i][col] == 1:
            return False
    
    # Diagonal superior izquierda
    for i, j in zip(range(fila, -1, -1), range(col, -1, -1)):
        if tablero[i][j] == 1:
            return False
    
    # Diagonal superior derecha
    for i, j in zip(range(fila, -1, -1), range(col, N)):
        if tablero[i][j] == 1:
            return False
    
    return True

def resolver_nreinas(tablero, fila, N):
    if fila >= N:
        return True
    
    for col in range(N):
        if es_seguro(tablero, fila, col, N):
            tablero[fila][col] = 1
            if resolver_nreinas(tablero, fila + 1, N):
                return True
            tablero[fila][col] = 0  # Backtrack
    return False