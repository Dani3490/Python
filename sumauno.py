"""
Llegir el numero de frase i ses frases
A cada frase substituir les consonants per una Majúscula
Imprimir ses frases modificades
"""



def llegir_frases(n):
    llista = list()
    for i in range(n):
        llista.append(input(""))
        return llista

def escriure_frases(llista):
# Prec: donada una llista d'element
# Post: imprimeix cada element de la llista
    for e in llista:
        print(e)

def convertir_majuscules(s):
    vocal="aeiouAEIOU"
    llista = list(s)
    for i,e in enumerate(s):
        if e in vocal:
            llista[i]=e.upper()
    return "".join(llista)


#Programa Principal
n = int(input(""))
llista= llegir_frases(n)
for i,e in enumerate(llista)
    llista[i]=convertir_majuscules(e)
escriure_frases(llista)