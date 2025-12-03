# Demanar un número a l'usuari
numero = input("Introdueix un número: ")

print(f"Dígits parells de {numero}:")

# Recórrer cada dígit
for digit in numero:
    if digit.isdigit():  # Verificar que és un dígit
        if int(digit) % 2 == 0:  # Comprovar si és parell
            print(digit, end=" ")

print()  # Salt de línia final