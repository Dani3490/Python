def elimina_duplicats(llista):
    vista = set()
    resultat = []
    
    for element in llista:
        if element not in vista:
            vista.add(element)
            resultat.append(element)
    
    return resultat
llista1 = [1, 2, 3, 2, 4, 1, 5]
print(elimina_duplicats(llista1))  # [1, 2, 3, 4, 5]

llista2 = ["poma", "plàtan", "poma", "taronja", "plàtan"]
print(elimina_duplicats(llista2))  # ['poma', 'plàtan', 'taronja']

llista3 = [1, 1, 1, 1]
print(elimina_duplicats(llista3))  # [1]

llista4 = []
print(elimina_duplicats(llista4))  # []

llista5 = [1, 2, 3, 4, 5]
print(elimina_duplicats(llista5))  # [1, 2, 3, 4, 5]