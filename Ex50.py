import random

def llista_20_elements():
    llista = []
    for i in range(20):
        llista.append(random.randint(1, 100))
    return llista

def te_duplicats(llista):
    if len(llista) != len(set(llista)):
        return True
    else:
        return False

def mostrar_duplicats(llista):

    duplicats = []
    for element in llista:
        if llista.count(element) > 1 and element not in duplicats:
            duplicats.append(element)
            print(f"  - El número {element} apareix {llista.count(element)} vegades")
    
    if len(duplicats) == 0:
        print("  No hi ha elements duplicats")

# PROGRAMA PRINCIPAL
print("=" * 50)
print("GENERADOR DE LLISTES ALEATÒRIES")
print("=" * 50)

# Generar la llista
la_meva_llista = llista_20_elements()

# Mostrar la llista
print(f"\nLlista generada: {la_meva_llista}")
print(f"Número d'elements: {len(la_meva_llista)}")

# Comprovar si té duplicats
if te_duplicats(la_meva_llista):
    print("\n✓ La llista TÉ elements duplicats:")
    mostrar_duplicats(la_meva_llista)
else:
    print("\n✓ La llista NO té elements duplicats")

# Estadístiques addicionals
print(f"\nElements únics: {len(set(la_meva_llista))}")
print(f"Elements duplicats: {len(la_meva_llista) - len(set(la_meva_llista))}")