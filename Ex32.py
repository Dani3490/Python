def mostrar_majors_que(tupla, valor):
    """
    Funció que mostra tots els elements d'una tupla que són majors que un valor donat.
    
    Paràmetres:
    tupla: tupla de números enters
    valor: número enter per comparar
    """
    print(f"\nNúmeros majors que {valor}:")
    trobats = False
    
    for numero in tupla:
        if numero > valor:
            print(numero, end=" ")
            trobats = True
    
    if not trobats:
        print("No hi ha cap número major.")
    else:
        print()  # Salt de línia al final


# Programa principal
def main():
    print("=== PROGRAMA PER TROBAR MAJORS DE 18 ANYS ===\n")
    
    # Demanar quants números vol introduir l'usuari
    quantitat = int(input("Quants números vols introduir? "))
    
    # Crear una llista per emmagatzemar els valors
    valors = []
    
    # Llegir els valors
    print(f"\nIntrodueix {quantitat} números enters (edats):")
    for i in range(quantitat):
        numero = int(input(f"  Número {i+1}: "))
        valors.append(numero)
    
    # Convertir la llista a tupla
    tupla_valors = tuple(valors)
    
    # Mostrar la tupla creada
    print(f"\nTupla creada: {tupla_valors}")
    
    # Cridar la funció per mostrar els majors de 18
    mostrar_majors_que(tupla_valors, 18)


# Executar el programa
if __name__ == "__main__":
    main()