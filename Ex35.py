def comptar_vocals(paraula):
    # Convertir a minúscules per comptar totes les vocals
    paraula = paraula.lower()
    
    # Diccionari per emmagatzemar el comptador
    vocals = {'a': 0, 'e': 0, 'i': 0, 'o': 0, 'u': 0}
    
    # Comptar cada vocal
    for lletra in paraula:
        if lletra in vocals:
            vocals[lletra] += 1
    
    # Mostrar el resultat
    print(f"Hi ha {vocals['a']} a's, {vocals['e']} e's, {vocals['i']} i's, {vocals['o']} o's i {vocals['u']} u's.")
    
    return vocals

comptar_vocals("Ratapinyada")
comptar_vocals("Programació")
comptar_vocals("Barcelona")
resultat = comptar_vocals("Hola")
print(resultat)  