def lenp(frase):
    paraules = frase.split()
    return list(map(len, paraules))


# Exemples d'ús
print(lenp("Hola món com estàs"))
# Sortida: [4, 3, 3, 5]

print(lenp("Python és genial"))
# Sortida: [6, 2, 6]

print(lenp("Aquesta és una prova"))
# Sortida: [7, 2, 3, 5]

print(lenp("a"))
# Sortida: [1]