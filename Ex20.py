"""
Definir una funció invertir() que calculi la inversa d’una cadena. 
Ex: invertir(“Soc del Ramis”) hauria de tornar la cadena “simaR led coS”.
"""


def invertir(cadena):
    return cadena[::-1]

# Proves
print(invertir("Soc del Ramis"))  # simaR led coS
print(invertir("Python"))          # nohtyP
print(invertir("Anna"))            # annA