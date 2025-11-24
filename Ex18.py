"""
Definir una funció que agafi un caràcter i retorni vertader si és una vocal i en cas contrari retorni fals. 
Prova-la amb diferents exemples.
"""



def ex18(c):
    v = "aeiouAEIOUàáèéìíòóùúÀÁÈÉÌÍÒÓÙÚ"
    if c in v:
        return True
    else:
        return False

# Programa Principal
c = input("Escriu un caràcter per a provar si és o no vocal: ")
print(ex18(c))