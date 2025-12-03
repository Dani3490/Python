def esta_ordenada(llista):
    # Casos especials: llistes buides o d'un sol element
    if len(llista) <= 1:
        return "està ordenada de forma ascendent"
    
    # Comprovem si està ordenada ascendentment
    ascendent = True
    for i in range(len(llista) - 1):
        if llista[i] > llista[i + 1]:
            ascendent = False
            break
    
    # Comprovem si està ordenada descendentment
    descendent = True
    for i in range(len(llista) - 1):
        if llista[i] < llista[i + 1]:
            descendent = False
            break
    
    # Retornem el resultat
    if ascendent:
        return "està ordenada de forma ascendent"
    elif descendent:
        return "està ordenada de forma descendent"
    else:
        return "no està ordenada"


# Proves de la funció
print("=== PROVES DE LA FUNCIÓ esta_ordenada() ===\n")

# Prova 1: Llista ordenada descendent
print("Prova 1:")
resultat1 = esta_ordenada([3, 2, 1])
print(f"esta_ordenada([3, 2, 1]) → {resultat1}\n")

# Prova 2: Llista ordenada ascendent
print("Prova 2:")
resultat2 = esta_ordenada([4, 5, 6])
print(f"esta_ordenada([4, 5, 6]) → {resultat2}\n")

# Prova 3: Llista no ordenada
print("Prova 3:")
resultat3 = esta_ordenada([1, 3, 2])
print(f"esta_ordenada([1, 3, 2]) → {resultat3}\n")

# Proves addicionals
print("=== PROVES ADDICIONALS ===\n")

# Prova 4: Llista amb un sol element
print("Prova 4:")
resultat4 = esta_ordenada([5])
print(f"esta_ordenada([5]) → {resultat4}\n")

# Prova 5: Llista buida
print("Prova 5:")
resultat5 = esta_ordenada([])
print(f"esta_ordenada([]) → {resultat5}\n")

# Prova 6: Llista amb elements repetits (ascendent)
print("Prova 6:")
resultat6 = esta_ordenada([1, 2, 2, 3])
print(f"esta_ordenada([1, 2, 2, 3]) → {resultat6}\n")

# Prova 7: Llista amb elements repetits (descendent)
print("Prova 7:")
resultat7 = esta_ordenada([5, 4, 4, 2])
print(f"esta_ordenada([5, 4, 4, 2]) → {resultat7}\n")

# Prova 8: Llista més llarga ascendent
print("Prova 8:")
resultat8 = esta_ordenada([1, 2, 3, 4, 5, 6, 7, 8])
print(f"esta_ordenada([1, 2, 3, 4, 5, 6, 7, 8]) → {resultat8}\n")

# Prova 9: Llista més llarga descendent
print("Prova 9:")
resultat9 = esta_ordenada([10, 8, 6, 4, 2])
print(f"esta_ordenada([10, 8, 6, 4, 2]) → {resultat9}\n")

# Prova 10: Llista no ordenada complexa
print("Prova 10:")
resultat10 = esta_ordenada([5, 3, 7, 2, 9])
print(f"esta_ordenada([5, 3, 7, 2, 9]) → {resultat10}\n")