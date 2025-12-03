def eliminarcapicua(llista):
    if len(llista) <= 2:
        return []
    else:
        return llista[1:-1]
llista1 = [1, 2, 3, 4, 5]
resultat1 = eliminarcapicua(llista1)
print(f"Llista original: {llista1}")
print(f"Llista resultant: {resultat1}")
print()

llista2 = ['a', 'b', 'c', 'd', 'e', 'f']
resultat2 = eliminarcapicua(llista2)
print(f"Llista original: {llista2}")
print(f"Llista resultant: {resultat2}")
print()

llista3 = [10, 20]
resultat3 = eliminarcapicua(llista3)
print(f"Llista original: {llista3}")
print(f"Llista resultant: {resultat3}")
print()

llista4 = [100]
resultat4 = eliminarcapicua(llista4)
print(f"Llista original: {llista4}")
print(f"Llista resultant: {resultat4}")
print()

llista5 = []
resultat5 = eliminarcapicua(llista5)
print(f"Llista original: {llista5}")
print(f"Llista resultant: {resultat5}")