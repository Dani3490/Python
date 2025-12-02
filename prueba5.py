for i in range(1, 1001):
    if (i%9==0 or i%7==0) and i%5!=0 and i%8!=0:
        print(i)
















"""
v1 = 10
while((v1>=5 and v1<=10) or (v1>=15 and v1<=20) or (v1>=25 and v1<=30)) and (v1!=6 and v1!=16 and v1!=26):
    v1 = int(input("Introdueix el primer operador: "))
    print(v1)
    print("Has insertat un número menor o igual que 3, adéu!")
def ordenar(x,y):
# Prec: Donats dos números
# Post: Els retorna amb ordre, primer el major i després el menor
    if x>y:
        return x, y
    elif y>x:
        return y, x
    else:
        return x, y
v1 = int(input("Introdueix el primer operador: "))
v2 = int(input("Introdueix el segon operador: "))

v1, v2 = ordenar(v1, v2)
for e in range(v2, v1+1):
    print(e)


r = v1 == v2
print(r)
r = v1 != v2
print(r)
r = v1 > v2
print(r)
r = v1 < v2
print(r)
r = v1 >= v2
print(r)
r = v1 <= v2
print(r)

v1 = int(input("Introdueix el primer operador: "))
v2 = int(input("Introdueix el segon operador: "))
r = v1 + v2
print(r)
r = v1 - v2
print(r)
r = v1 * v2
print(r)
r = v1 // v2 # Divisió entera
print(r)
r = v1 / v2 # Divisió real
print(r)
r = v1 % v2
print(r)
r = v1 ** v2
print(r)
r = v1 + (v2**2 / v1 - (v1%v2))
print(r)"""