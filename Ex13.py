opcio=int(input("""Elegeixi una opció:
                1.Suma
                2.Resta
                3.Multiplicació
                4.Divisió
                0.Sortir
                """))
a = int(input("Escriu el primer operand: "))
b = int(input("Escriu el segon operand: "))
if opcio==1:
    print("La suma de {} + {} és {}".format (a, b, a+b))
elif opcio==2:
    print("La resta de {} - {} és {}".format (a, b, a-b))
elif opcio==3:
    print("La multiplicació de {} * {} és {}".format (a, b, a*b))
elif opcio==4:
    print("La divisió de {} / {} és {}".format (a, b, a/b))