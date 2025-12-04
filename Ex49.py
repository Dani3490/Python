def hi_ha_duplicats(llista):
    return len(llista) != len(set(llista))
print("=== PROVES DE LA FUNCIÓ hi_ha_duplicats() ===\n")

llista1 = [1, 2, 3, 4, 2, 5]
print(f"Llista: {llista1}")
print(f"Hi ha duplicats? {hi_ha_duplicats(llista1)}")
print()

llista2 = [1, 2, 3, 4, 5]
print(f"Llista: {llista2}")
print(f"Hi ha duplicats? {hi_ha_duplicats(llista2)}")
print()

llista3 = ["poma", "pera", "taronja", "poma"]
print(f"Llista: {llista3}")
print(f"Hi ha duplicats? {hi_ha_duplicats(llista3)}")
print()

llista4 = []
print(f"Llista: {llista4}")
print(f"Hi ha duplicats? {hi_ha_duplicats(llista4)}")
print()

llista5 = [42]
print(f"Llista: {llista5}")
print(f"Hi ha duplicats? {hi_ha_duplicats(llista5)}")
print()

llista6 = [7, 7, 7, 7]
print(f"Llista: {llista6}")
print(f"Hi ha duplicats? {hi_ha_duplicats(llista6)}")
print()

llista_original = [1, 2, 3, 2, 4]
print(f"Llista original abans: {llista_original}")
resultat = hi_ha_duplicats(llista_original)
print(f"Llista original després: {llista_original}")
print(f"La llista no s'ha modificat: {llista_original == [1, 2, 3, 2, 4]}")