numero = int(input("Introdueix un número (entre 1 i 20): "))

# Validar que el número estigui entre 1 i 20
while numero < 1 or numero > 20:
    print("Error! El número ha d'estar entre 1 i 20.")
    numero = int(input("Introdueix un número (entre 1 i 20): "))

# Imprimir la taula de multiplicar
print(f"\nTaula de multiplicar del {numero}:")
print("-" * 25)

for i in range(1, 11):
    resultat = numero * i
    print(f"{numero} x {i:2d} = {resultat:3d}")