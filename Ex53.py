def index_paraula(llista, paraula):
    try:
        return llista.index(paraula)
    except ValueError:
        return -1
    # Exemple 1: Paraula que existeix
paraules = ["anna", "carles", "joan", "maria", "pere"]
resultat = index_paraula(paraules, "maria")
print(f"L'índex de 'maria' és: {resultat}")  

# Exemple 2: Paraula que no existeix
resultat = index_paraula(paraules, "laura")
print(f"L'índex de 'laura' és: {resultat}") 

# Exemple 3: Primera paraula
resultat = index_paraula(paraules, "anna")
print(f"L'índex de 'anna' és: {resultat}") 