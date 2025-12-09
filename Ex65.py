def llista_a_diccionari(llista):
    return {element: index for index, element in enumerate(llista)}

# Exemple d'ús
tupla = ('casa', 'cotxe', 'cadira', 'taula')
resultat = llista_a_diccionari(tupla)
print(resultat)