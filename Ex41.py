# Demanar un número a l'usuari
numero = int(input("Introdueix un número menor de 100: "))

# Verificar que el número sigui menor de 100
if numero >= 100:
    print("Error: El número ha de ser menor de 100")
else:
    # Inicialitzar la suma
    suma = 0
    
    # Crear una llista per mostrar els números utilitzats
    numeros_utilitzats = []
    
    # Calcular la suma dels quadrats
    # Començar des de numero-4 i anar restant 4 cada vegada
    actual = numero - 4
    
    while actual > 0:
        suma += actual ** 2
        numeros_utilitzats.append(actual)
        actual -= 4
    
    # Mostrar el resultat
    print(f"\nNúmero introduït: {numero}")
    print(f"Números utilitzats: {numeros_utilitzats}")
    
    # Mostrar l'operació
    operacio = " + ".join([f"{n}²" for n in numeros_utilitzats])
    print(f"Operació: {operacio}")
    
    print(f"Suma total: {suma}")