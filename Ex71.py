def llegir_fitxer_basic(nom_fitxer):
    try:
        fitxer = open(nom_fitxer, 'r', encoding='utf-8')
        contingut = fitxer.read()
        fitxer.close()
        return contingut
    except FileNotFoundError:
        print(f"Error: El fitxer '{nom_fitxer}' no existeix.")
        return None
    except PermissionError:
        print(f"Error: No tens permisos per llegir '{nom_fitxer}'.")
        return None
    except Exception as e:
        print(f"Error inesperat: {e}")
        return None

def llegir_fitxer_with(nom_fitxer):
    try:
        with open(nom_fitxer, 'r', encoding='utf-8') as fitxer:
            return fitxer.read()
    except FileNotFoundError:
        print(f"Error: El fitxer '{nom_fitxer}' no existeix.")
        return None
    except PermissionError:
        print(f"Error: No tens permisos per llegir '{nom_fitxer}'.")
        return None
    except Exception as e:
        print(f"Error inesperat: {e}")
        return None

def llegir_fitxer_complet(nom_fitxer):
    return llegir_fitxer_with(nom_fitxer)

def llegir_fitxer_linies(nom_fitxer):
    try:
        with open(nom_fitxer, 'r', encoding='utf-8') as fitxer:
            return fitxer.readlines()
    except FileNotFoundError:
        print(f"Error: El fitxer '{nom_fitxer}' no existeix.")
        return None
    except PermissionError:
        print(f"Error: No tens permisos per llegir '{nom_fitxer}'.")
        return None
    except Exception as e:
        print(f"Error inesperat: {e}")
        return None

# Programa principal de prova
def main():
    print("=== PROVES DE LECTURA DE FITXERS ===\n")
    
    # Crear un fitxer de prova
    with open("prova.txt", "w", encoding='utf-8') as f:
        f.write("Hola món!\nAixò és una prova.\nTercera línia.")
    
    # Provar lectura correcta
    print("1. Lectura normal:")
    contingut = llegir_fitxer_with("prova.txt")
    if contingut:
        print(contingut)
    
    print("\n2. Lectura línia per línia:")
    linies = llegir_fitxer_linies("prova.txt")
    if linies:
        for i, linia in enumerate(linies, 1):
            print(f"Línia {i}: {linia.strip()}")
    
    print("\n3. Fitxer inexistent:")
    llegir_fitxer_with("no_existeix.txt")
    
    print("\n4. Lectura completa amb validació:")
    contingut_complet = llegir_fitxer_complet("prova.txt")
    if contingut_complet:
        print(contingut_complet)
    
    # Netejar
    import os
    os.remove("prova.txt")

if __name__ == "__main__":
    main()
