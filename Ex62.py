from functools import reduce

def Passar_a_Numero(llista):
    return reduce(lambda acum, digit: acum * 10 + digit, llista, 0)

# Exemples d'ús
print(Passar_a_Numero([3, 4, 1, 5]))  # 3415
print(Passar_a_Numero([1, 2, 3]))      # 123
print(Passar_a_Numero([7]))            # 7
print(Passar_a_Numero([0, 5, 9]))      # 59