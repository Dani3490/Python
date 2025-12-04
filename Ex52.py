def crear_llista_fitxer(nom_fitxer):
    llista_paraules = []
    
    try:
        with open(nom_fitxer, 'r', encoding='utf-8') as fitxer:
            for linia in fitxer:
                # Divideix cada línia en paraules
                paraules = linia.split()
                # Afegeix cada paraula a la llista
                llista_paraules.extend(paraules)
        
        print(f"✓ Fitxer llegit correctament!")
        print(f"✓ Total de paraules: {len(llista_paraules)}")
        return llista_paraules
    
    except FileNotFoundError:
        print(f"✗ Error: El fitxer '{nom_fitxer}' no existeix.")
        return []
    except Exception as e:
        print(f"✗ Error inesperat: {e}")
        return []


# PROVES DE LA FUNCIÓ

# Primer, creem un fitxer de prova
print("=== CREANT FITXER DE PROVA ===")
with open('prova.txt', 'w', encoding='utf-8') as f:
    f.write("Hola món!\n")
    f.write("Això és una prova.\n")
    f.write("Python és genial.\n")
print("Fitxer 'prova.txt' creat.\n")

# Prova 1: Llegir el fitxer creat
print("=== PROVA 1: Llegir fitxer existent ===")
llista1 = crear_llista_fitxer('prova.txt')
print(f"Llista resultant: {llista1}\n")

# Prova 2: Intentar llegir un fitxer que no existeix
print("=== PROVA 2: Fitxer inexistent ===")
llista2 = crear_llista_fitxer('no_existeix.txt')
print(f"Llista resultant: {llista2}\n")

# Prova 3: Crear un fitxer amb més contingut
print("=== PROVA 3: Fitxer amb més contingut ===")
with open('text_llarg.txt', 'w', encoding='utf-8') as f:
    f.write("Catalunya és una comunitat autònoma d'Espanya.\n")
    f.write("Barcelona és la capital de Catalunya.\n")
    f.write("El català és la llengua oficial juntament amb el castellà.\n")

llista3 = crear_llista_fitxer('text_llarg.txt')
print(f"Primeres 10 paraules: {llista3[:10]}")
print(f"Llista completa: {llista3}\n")

# Prova 4: Mostrar estadístiques
print("=== PROVA 4: Estadístiques ===")
print(f"Número total de paraules: {len(llista3)}")
print(f"Primera paraula: {llista3[0]}")
print(f"Última paraula: {llista3[-1]}")
print(f"Paraules úniques: {len(set(llista3))}")