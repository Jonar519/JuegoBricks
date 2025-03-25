from datetime import datetime

def es_fin_de_semana():
    hoy = datetime.now()
    return hoy.weekday() >= 5  # 5 = sábado, 6 = domingo