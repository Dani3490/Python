def paraula_mes_llarga(llista_paraules):
    paraula_llarga = ""
    
    for paraula in llista_paraules:
        if len(paraula) > len(paraula_llarga):
            paraula_llarga = paraula
    
    return paraula_llarga

resultat = paraula_mes_llarga(["Hola", "Ramis", "IES", "Paraula"])
print(resultat)
print(paraula_mes_llarga(["Python", "Java", "C", "JavaScript"]))
print(paraula_mes_llarga(["a", "bb", "ccc"]))