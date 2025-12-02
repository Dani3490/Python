# Demanar l'any actual
any_actual = int(input("Any actual: "))

# Llistes per emmagatzemar les dades
noms = []
anys_naixement = []
edats = []

# Recollir les dades de les 4 persones
print("\nIntrodueix les dades de 4 persones:")
for i in range(4):
    print(f"\nPersona {i+1}:")
    nom = input("  Nom: ")
    any_naixement = int(input("  Any de naixement: "))
    
    # Calcular l'edat
    edat = any_actual - any_naixement
    
    # Guardar les dades
    noms.append(nom)
    anys_naixement.append(any_naixement)
    edats.append(edat)

# Imprimir la taula
print(f"\nAny actual {any_actual}")
print(f"{'Nom':<20}{'Data naixement':<20}{'Anys que farà aquest any'}")
print("-" * 60)

for i in range(4):
    print(f"{noms[i]:<20}{anys_naixement[i]:<20}{edats[i]}")
