def tiene_ciclo(secuencia):
    if len(secuencia) <= 1:
        return False
    
    tortuga = liebre = secuencia[0]
    while True:
        tortuga = secuencia[tortuga]  # Avanza 1 paso
        liebre = secuencia[secuencia[liebre]]  # Avanza 2 pasos
        if tortuga == liebre:
            return True
        if tortuga >= len(secuencia) or liebre >= len(secuencia):
            return False