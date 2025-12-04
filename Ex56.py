# Demanar els dos números a l'usuari
num1 = int(input("Introdueix el primer número: "))
num2 = int(input("Introdueix el segon número: "))

# Assegurar que num1 sigui el més petit
if num1 > num2:
    num1, num2 = num2, num1

# Sumar tots els números entre num1 i num2 (inclosos)
suma = 0
for i in range(num1, num2 + 1):
    suma += i

print(f"La suma de tots els números entre {num1} i {num2} és: {suma}")