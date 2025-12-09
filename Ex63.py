def paraules_per_lletra(llista_paraules, lletra):
    return list(filter(lambda paraula: paraula.lower().startswith(lletra.lower()), llista_paraules))


# Exemples d'ús
paraules = ["maria", "manta", "peu", "mà"]

print(paraules_per_lletra(paraules, 'p'))  # ['peu']
print(paraules_per_lletra(paraules, 'm'))  # ['maria', 'manta', 'mà']
print(paraules_per_lletra(paraules, 'a'))  # []

# Més exemples
paraules2 = ["Pera", "poma", "Plàtan", "síndria", "taronja"]
print(paraules_per_lletra(paraules2, 'p'))  # ['Pera', 'poma', 'Plàtan']
print(paraules_per_lletra(paraules2, 'P'))  # ['Pera', 'poma', 'Plàtan']