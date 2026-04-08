def calcular_media(n1, n2, n3, n4):
    notas = [n for n in [n1, n2, n3, n4] if n is not None]
    if not notas:
        return None
    if any(n < 0 or n > 10 for n in notas):
        return None
    return round(sum(notas) / len(notas), 2)