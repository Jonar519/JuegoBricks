def tiene_ciclo(secuencia):
    if not secuencia:  # Si la lista está vacía
        return False
    
    tortuga = liebre = 0  # Empezamos en el primer índice (0)

    while True:
        # Verificar límites y None
        if (
            tortuga >= len(secuencia) or 
            liebre >= len(secuencia) or
            secuencia[tortuga] is None or
            secuencia[liebre] is None
        ):
            return False

        # Mover tortuga 1 paso
        tortuga = secuencia[tortuga]
        
        # Mover liebre 2 pasos
        liebre = secuencia[liebre]
        if liebre >= len(secuencia) or secuencia[liebre] is None:
            return False
        liebre = secuencia[liebre]

        # Detección de ciclo
        if tortuga == liebre:
            return True