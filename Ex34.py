def noms_que_comencen_per(llista_noms, lletra):
    """
    Compta quants noms de la llista comencen per una lletra determinada.
    Gestiona noms buits i valida l'entrada.
    """
    if not isinstance(lletra, str) or len(lletra) != 1:
        return "Error: Has de proporcionar una única lletra"
    
    comptador = 0
    for nom in llista_noms:
        if nom and nom[0].lower() == lletra.lower():
            comptador += 1
    return comptador

noms = ["Anna", "Berta", "Albert", "Carla", "antonio"]
resultat = noms_que_comencen_per(noms)
print(f"Noms que comencen per 'a': {resultat}") 


noms2 = ["Pere", "Maria", "Joan"]
resultat2 = noms_que_comencen_per(noms2)
print(f"Noms que comencen per 'a': {resultat2}") 


noms3 = ["Àlex", "amanda", "ANDREU"]
resultat3 = noms_que_comencen_per(noms)
print(f"Noms que comencen per 'a': {resultat3}") 