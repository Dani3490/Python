def es_palindrom(paraula):
    """
    Retorna True si la paraula és un palíndrom, False en cas contrari.
    
    Args:
        paraula: string a comprovar
    
    Returns:
        bool: True si és palíndrom, False si no ho és
    """
    paraula = paraula.lower()  # Convertim a minúscules
    return paraula == paraula[::-1]
# Proves
paraules_test = ["radar", "ara", "civic", "rallar", "tapat", "simis", "refer", "hola", "Python"]

print("Comprovació de palíndroms:")
print("-" * 40)

for paraula in paraules_test:
    resultat = es_palindrom(paraula)
    print(f"{paraula:10} -> {'SÍ és palíndrom' if resultat else 'NO és palíndrom'}")# Proves
paraules_test = ["radar", "ara", "civic", "rallar", "tapat", "simis", "refer", "hola", "Python"]

print("Comprovació de palíndroms:")
print("-" * 40)

for paraula in paraules_test:
    resultat = es_palindrom(paraula)
    print(f"{paraula:10} -> {'SÍ és palíndrom' if resultat else 'NO és palíndrom'}")