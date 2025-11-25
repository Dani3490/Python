def gran(a, b):
    """
    Retorna el major de dos números.
    
    Paràmetres:
        a: primer número
        b: segon número
    
    Retorna:
        El número més gran dels dos
    """
    if a > b:
        return a
    else:
        return b

# Proves
print("=== Proves de la funció gran() ===")
print(f"gran(5, 3) = {gran(5, 3)}")           # 5
print(f"gran(10, 25) = {gran(10, 25)}")       # 25
print(f"gran(-5, -10) = {gran(-5, -10)}")     # -5
print(f"gran(7, 7) = {gran(7, 7)}")           # 7
print(f"gran(3.14, 2.71) = {gran(3.14, 2.71)}")  # 3.14
print(f"gran(0, -5) = {gran(0, -5)}")         # 0