def concatenar_llistes(llista1, llista2, connector):
    return [f"{elem1}{connector}{elem2}" for elem1, elem2 in zip(llista1, llista2)]


# Exemple d'ús
llista1 = ['sub', 'supra']
llista2 = ['campió', 'campiona']
connector = '-'

resultat = concatenar_llistes(llista1, llista2, connector)
print(resultat) 