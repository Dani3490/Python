#a = [1, "a", "Capça", [2], 1, "a"]
a = [10, 9, 8, 7, 6, 5, 1, 2, 3, 4]
# Passar els elements de la llista string
for i in range(len(a)):
    a[i]=str(a[i])
# Crear un únic string separat per guió
print("-".join(a))










"""
b = a.copy()
b[0]=100
print(a)
print(a[::-1]) # Retorna una llista invertida, però no modifica l'original
print(a)
print(a.reverse()) # No retorna res, però modifica la llista original
print(a)
for e in a:
    print(e)
for i in range(len(a)):
    print("La posició {} té el valor {}".format(i,a[i]))
for i,e in enumerate(a):
    print("La posició {} té el valor {}".format(i,e))
a.append("Final")
print(a)
"""