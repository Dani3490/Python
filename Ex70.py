def dividir(dividend, divisor):
    if divisor == 0:
        print("ERROR: No es pot dividir per zero!")
        return None
    else:
        resultat = dividend / divisor
        return resultat

# Exemples d'ús
print(dividir(10, 2))    # Output: 5.0
print(dividir(10, 0))    # Output: ERROR: No es pot dividir per zero! / None