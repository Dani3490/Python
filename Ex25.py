def crear_punts(x, y, caracter='*'):
    return (x, y, caracter)

def dibuixar_cor():
    punts = []
    
    for y in range(15, -15, -1):
        for x in range(-30, 31):

            eq = ((x * 0.05) ** 2 + (y * 0.1) ** 2 - 1) ** 3 - (x * 0.05) ** 2 * (y * 0.1) ** 3
            
            if eq <= 0:
                punts.append(crear_punts(x, y, '.'))
    
    print("\n" + "="*60)
    print(" "*20 + "COR AMB PYTHON")
    print("="*60 + "\n")
    
    graella = {}
    for punt in punts:
        x, y, car = punt
        if y not in graella:
            graella[y] = {}
        graella[y][x] = car
    
    for y in range(15, -15, -1):
        linia = ""
        for x in range(-30, 31):
            if y in graella and x in graella[y]:
                linia += graella[y][x]
            else:
                linia += " "
        print(linia)
    
    print("\n" + "="*60)

dibuixar_cor()