def menu_principal():
    opcio=0
    while opcio<1 or opcio>3:
        opcio = int(input(""" Elegeixi una opció:
                      1. Calculadora
                      2. Calculadora real (floats)
                      3. Sortir \n"""))
    if opcio>0 and opcio<4:
        return opcio
    else:
        print("L'opció seleccionada no es correcte,torni-ho a provar!!\n")
        
menu_principal()