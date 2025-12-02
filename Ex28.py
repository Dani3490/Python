def filtrar_paraules(llista_paraules, x):
    resultat = []
    for paraula in llista_paraules:
        if len(paraula) > x:
            resultat.append(paraula)
    return resultat

paraules = ["casa", "cotxe", "ordinador", "sol", "muntanya"]
print(filtrar_paraules(paraules, 4))

paraules = ["gat", "gos", "elefant", "formiga"]
print(filtrar_paraules(paraules, 3))

paraules = ["Python", "és", "genial"]
print(filtrar_paraules(paraules, 5))
