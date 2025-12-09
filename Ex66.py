def comptar_coincidencies(llista):
    comptador = 0
    for index, valor in enumerate(llista):
        if index == valor:
            comptador += 1
    return comptador


# Exemples d'ús
print(comptar_coincidencies([0, 2, 3, 3, 4]))  # Retorna: 3
# Coincidències: índex 0=valor 0, índex 3=valor 3, índex 4=valor 4

print(comptar_coincidencies([0, 1, 2, 3, 4]))  # Retorna: 5
# Tots coincideixen

print(comptar_coincidencies([5, 6, 7, 8, 9]))  # Retorna: 0
# Cap coincidència

print(comptar_coincidencies([1, 1, 2, 3]))     # Retorna: 2
# Coincidències: índex 2=valor 2, índex 3=valor 3