def comptar_digits_string(num):
    """Compta els dígits convertint el número a string"""
    return len(str(abs(num)))

# Programa principal
def main():
    while True:
        try:
            numero = int(input("Introdueix un número (entre 1 i 900000): "))
            
            if 1 <= numero <= 900000:
                digits = comptar_digits_string(numero)
                print(f"El número {numero} té {digits} dígit(s)")
                break
            else:
                print("Error: El número ha d'estar entre 1 i 900000")
        except ValueError:
            print("Error: Introdueix un número vàlid")

if __name__ == "__main__":
    main()