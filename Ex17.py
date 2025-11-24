"""
Definir una funció que calculi la longitud d’una llista o d’una cadena donada.
Prova-la amb diferents exemples.
"""


def ex17(a):
    return len(a)

# Programa principal
a=[1, 3, 4, "Pedro", [3,6], "a", [1, [3,4],5]]
print(ex17(a))
b = "Som en Joan Ramis, i tú què tal estàs?"
print(ex17(b))
c=[]
print(ex17(c))
