def superposicio(llista1, llista2):
    for element in llista1:
        if element in llista2:
            return True
    return False
# Proves
print(superposicio([1, 2, 3], [3, 4, 5]))  # True (tenen el 3 en comú)
print(superposicio([1, 2, 3], [4, 5, 6]))  # False (cap element en comú)
print(superposicio(['a', 'b'], ['c', 'a']))  # True (tenen la 'a' en comú)
print(superposicio([], [1, 2, 3]))  # False (llista buida)
print(superposicio([1, 2], []))  # False (llista buida)