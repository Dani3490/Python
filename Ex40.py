def demanar_capital():
    """Demana i valida el capital inicial"""
    while True:
        try:
            capital = float(input("Introdueix la quantitat a sol·licitar (50000€ - 800000€): "))
            if 50000 <= capital <= 800000:
                return capital
            else:
                print("Error: La quantitat ha d'estar entre 50000€ i 800000€")
        except ValueError:
            print("Error: Introdueix un valor numèric vàlid")

def demanar_interes():
    """Demana i valida l'interès"""
    while True:
        try:
            interes = float(input("Introdueix l'interès anual (0.5% - 13%): "))
            if 0.5 <= interes <= 13:
                return interes
            else:
                print("Error: L'interès ha d'estar entre 0.5% i 13%")
        except ValueError:
            print("Error: Introdueix un valor numèric vàlid")

def demanar_anys():
    """Demana i valida el número d'anys"""
    while True:
        try:
            anys = int(input("Introdueix el número d'anys (3 - 40): "))
            if 3 <= anys <= 40:
                return anys
            else:
                print("Error: Els anys han d'estar entre 3 i 40")
        except ValueError:
            print("Error: Introdueix un valor enter vàlid")

def calcular_capital_final(capital_inicial, interes, anys):
    """Calcula el capital final amb la fórmula d'interès compost"""
    capital_final = capital_inicial * (1 + interes/100) ** anys
    return capital_final

# Programa principal
print("=" * 50)
print("CALCULADORA DE CAPITAL FINAL AMB INTERÈS COMPOST")
print("=" * 50)
print()

# Demanar dades a l'usuari
capital_inicial = demanar_capital()
interes = demanar_interes()
anys = demanar_anys()

# Calcular el capital final
capital_final = calcular_capital_final(capital_inicial, interes, anys)

# Mostrar resultats
print()
print("=" * 50)
print("RESULTATS")
print("=" * 50)
print(f"Capital inicial: {capital_inicial:.2f}€")
print(f"Interès anual: {interes}%")
print(f"Període: {anys} anys")
print(f"Capital final: {capital_final:.2f}€")
print(f"Benefici obtingut: {capital_final - capital_inicial:.2f}€")
print("=" * 50)