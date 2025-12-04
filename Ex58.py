def elements_parells(llista):
    """
    Donada una llista de paraules, retorna només les que estan en posició parell.
    Les posicions parells són: 0, 2, 4, 6, etc.
    """
    resultat = []
    for i in range(len(llista)):
        if i % 2 == 0:  # Si la posició és parell
            resultat.append(llista[i])
    return resultat


# Forma alternativa més compacta amb slicing
def elements_parells_v2(llista):
    """
    Versió alternativa utilitzant slicing.
    [::2] significa: des del principi fins al final, de 2 en 2
    """
    return llista[::2]


# PROVES DE LA FUNCIÓ
print("=== PROVES DE LA FUNCIÓ elements_parells() ===\n")

# Prova 1
paraules1 = ["gat", "gos", "ocell", "peix", "cavall", "conill"]
print(f"Llista original: {paraules1}")
print(f"Elements en posició parell: {elements_parells(paraules1)}")
print(f"Versió 2: {elements_parells_v2(paraules1)}")
print()

# Prova 2
paraules2 = ["dilluns", "dimarts", "dimecres", "dijous", "divendres", "dissabte", "diumenge"]
print(f"Llista original: {paraules2}")
print(f"Elements en posició parell: {elements_parells(paraules2)}")
print()

# Prova 3
paraules3 = ["hola", "adéu"]
print(f"Llista original: {paraules3}")
print(f"Elements en posició parell: {elements_parells(paraules3)}")
print()

# Prova 4 - Llista amb un sol element
paraules4 = ["únic"]
print(f"Llista original: {paraules4}")
print(f"Elements en posició parell: {elements_parells(paraules4)}")
print()

# Prova 5 - Llista buida
paraules5 = []
print(f"Llista original: {paraules5}")
print(f"Elements en posició parell: {elements_parells(paraules5)}")