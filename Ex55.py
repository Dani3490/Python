print("NÚMEROS PARELLS FINS A 100:")
print("=" * 40)

# Mètode 1: Amb range i pas de 2
for numero in range(2, 101, 2):
    print(numero, end=", " if numero < 100 else "\n")