def gran(a, b, c):
    """
    Retorna el major de tres números.
    
    Paràmetres:
    a, b, c: Números a comparar
    
    Retorna:
    El número més gran dels tres
    """
    if a >= b and a >= c:
        return a
    elif b >= a and b >= c:
        return b
    else:
        return c


# Proves
print("=== Proves de la funció gran() ===")
print(f"gran(5, 7, 3) = {gran(5, 7, 3)}")           # 7
print(f"gran(10, 4, 25) = {gran(10, 4, 25)}")       # 25
print(f"gran(-5, -1, -10) = {gran(-5, -1, -10)}")     # -1
print(f"gran(7, 7, 6) = {gran(7, 7, 6)}")           # 7
print(f"gran(3.14, 5.25, 2.71) = {gran(3.14, 5.25, 2.71)}")  # 5.25
print(f"gran(0, -2, -5) = {gran(0, -2, -5)}")         # 0