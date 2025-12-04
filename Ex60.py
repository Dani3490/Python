def es_primer(num):
    """
    Funció que determina si un número és primer
    """
    if num < 2:
        return False
    if num == 2:
        return True
    if num % 2 == 0:
        return False
    
    # Només cal comprovar fins a l'arrel quadrada del número
    for i in range(3, int(num ** 0.5) + 1, 2):
        if num % i == 0:
            return False
    return True

# Trobar tots els primers entre 1 i 100
primers = []

for num in range(1, 101):
    if es_primer(num):
        primers.append(num)

# Mostrar resultats
print("Números primers entre 1 i 100:")
print("-" * 50)

# Mostrar els primers en files de 10
for i in range(0, len(primers), 10):
    print(" ".join(f"{p:3d}" for p in primers[i:i+10]))

print("-" * 50)
print(f"\nTotal de números primers: {len(primers)}")