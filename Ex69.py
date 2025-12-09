def potencies(exponent):
    return [num ** exponent for num in range(10)]

# Exemples d'ús
print("Quadrat (potència 2):", potencies(2))
print("Cub (potència 3):", potencies(3))
print("Potència 4:", potencies(4))
print("Potència 5:", potencies(5))