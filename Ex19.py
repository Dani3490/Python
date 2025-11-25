def sumar_llista(llista):
    """
    Suma tots els valors d'una llista.
    
    Args:
        llista: Una llista de números
    
    Returns:
        La suma de tots els elements
    """
    suma = 0
    for element in llista:
        suma += element
    return suma


def multiplicar_llista(llista):
    """
    Multiplica tots els valors d'una llista.
    
    Args:
        llista: Una llista de números
    
    Returns:
        El producte de tots els elements
    """
    producte = 1
    for element in llista:
        producte *= element
    return producte


# PROVES DE LES FUNCIONS

print("=== PROVES DE sumar_llista() ===")
print(f"sumar_llista([1, 2, 3, 4]) = {sumar_llista([1, 2, 3, 4])}")  # 10
print(f"sumar_llista([5, 10, 15]) = {sumar_llista([5, 10, 15])}")    # 30
print(f"sumar_llista([100]) = {sumar_llista([100])}")                # 100
print(f"sumar_llista([]) = {sumar_llista([])}")                      # 0
print(f"sumar_llista([-5, 5, -3, 3]) = {sumar_llista([-5, 5, -3, 3])}")  # 0

print("\n=== PROVES DE multiplicar_llista() ===")
print(f"multiplicar_llista([1, 2, 3, 4]) = {multiplicar_llista([1, 2, 3, 4])}")  # 24
print(f"multiplicar_llista([5, 10, 2]) = {multiplicar_llista([5, 10, 2])}")      # 100
print(f"multiplicar_llista([7]) = {multiplicar_llista([7])}")                    # 7
print(f"multiplicar_llista([]) = {multiplicar_llista([])}")                      # 1
print(f"multiplicar_llista([2, 0, 5]) = {multiplicar_llista([2, 0, 5])}")        # 0
