# Demanar un número a l'usuari
numero = input("Introdueix un número: ")

# Calcular la suma dels dígits
suma = 0
for digit in numero:
    if digit.isdigit():  # Comprovar que és un dígit
        suma += int(digit)

# Mostrar el resultat
print(f"La suma dels dígits de {numero} és: {suma}")

# Comprovar si és parell o senar
if suma % 2 == 0:
    print(f"{suma} és un número PARELL")
else:
    print(f"{suma} és un número SENAR")