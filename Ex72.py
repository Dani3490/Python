import os

# 1. Crear el directori /home/cicles/AO/Prova
directori = "/home/daniel-manteca/AO/Prova"

# Crear el directori (amb parents=True per crear directoris intermedis si no existeixen)
try:
    os.makedirs(directori, exist_ok=True)
    print(f"Directori creat: {directori}")
except Exception as e:
    print(f"Error creant el directori: {e}")

# 2. Canviar-nos a aquest directori
os.chdir(directori)
print(f"Directori actual: {os.getcwd()}")

# 3. Crear el fitxer Ex12.txt i escriure els noms dels companys
nom_fitxer = "Ex12.txt"

# Obrir el fitxer en mode escriptura
with open(nom_fitxer, 'w', encoding='utf-8') as fitxer:
    # Escriure noms dels companys
    fitxer.write("Mohamed Mak\n")
    fitxer.write("Izan G\n")
    fitxer.write("Luca\n")
    fitxer.write("Raul\n")
    fitxer.write("Joan\n")
    fitxer.write("Pol\n")
    fitxer.write("Ian\n")
    fitxer.write("Russel\n")
    fitxer.write("Yousef\n")
    fitxer.write("Edgar\n")
    fitxer.write("Iker A\n")
    fitxer.write("Iker H\n")
    fitxer.write("Mohamed Mam\n")
    fitxer.write("Lucas\n")
    fitxer.write("Osama\n")
    fitxer.write("Fabian\n")
    fitxer.write("Justin\n")
    fitxer.write("Aitor\n")
    fitxer.write("Izan P\n")
    fitxer.write("Rafel\n")
    fitxer.write("Daniel\n")
print("Noms dels companys escrits i fitxer tancat")

# 4. Obrir el fitxer per afegir els noms dels professors
with open(nom_fitxer, 'a', encoding='utf-8') as fitxer:
    # Afegir noms dels professors
    fitxer.write("Joan Carreras\n")
    fitxer.write("David Labiano\n")
    fitxer.write("Irene Coll\n")
    fitxer.write("Pep Malle\n")
    fitxer.write("Manel Bosch\n")
    fitxer.write("Jesus Capo\n")
print("Noms dels professors afegits i fitxer tancat")

# 5. Obrir el fitxer i posar tot el contingut dins una llista
with open(nom_fitxer, 'r', encoding='utf-8') as fitxer:
    llista_noms = fitxer.readlines()

# Netejar els salts de línia
llista_noms = [nom.strip() for nom in llista_noms]

# Mostrar la llista
print("\n=== LLISTA DE NOMS ===")
print(llista_noms)

print("\n=== Contingut complet ===")
for i, nom in enumerate(llista_noms, 1):
    print(f"{i}. {nom}")