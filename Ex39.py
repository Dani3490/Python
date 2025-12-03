# Demanem dues paraules a l'usuari
paraula1 = input("Escriu la primera paraula: ").lower()
paraula2 = input("Escriu la segona paraula: ").lower()

# Comprovem si rimen
if len(paraula1) >= 3 and len(paraula2) >= 3:
    # Comparem les 3 darreres lletres
    if paraula1[-3:] == paraula2[-3:]:
        print("Les paraules RIMEN")
    # Comparem les 2 darreres lletres
    elif paraula1[-2:] == paraula2[-2:]:
        print("Les paraules RIMEN UN POC")
    else:
        print("Les paraules NO RIMEN")
elif len(paraula1) >= 2 and len(paraula2) >= 2:
    # Si alguna paraula té menys de 3 lletres, només comparem les 2 darreres
    if paraula1[-2:] == paraula2[-2:]:
        print("Les paraules RIMEN UN POC")
    else:
        print("Les paraules NO RIMEN")
else:
    print("Les paraules són massa curtes per comparar")