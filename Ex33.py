def noms_que_comencen_per(llista_noms):
    contador = 0
    for nom in llista_noms:
        if nom and nom[0].lower() == 'a':
            contador += 1
    return contador

noms = ["Anna", "Berta", "Albert", "Carla", "antonio"]
resultat = noms_que_comencen_per(noms)
print(f"Noms que comencen per 'a': {resultat}") 


noms2 = ["Pere", "Maria", "Joan"]
resultat2 = noms_que_comencen_per(noms2)
print(f"Noms que comencen per 'a': {resultat2}") 


noms3 = ["Àlex", "amanda", "ANDREU"]
resultat3 = noms_que_comencen_per(noms3)
print(f"Noms que comencen per 'a': {resultat3}") 