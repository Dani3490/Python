def es_de_traspas(any):
    if any % 400 == 0:
        return True
    elif any % 100 == 0:
        return False
    elif any % 4 == 0:
        return True
    else:
        return False
print(es_de_traspas(2024))  
print(es_de_traspas(2000))  
print(es_de_traspas(1900))  
print(es_de_traspas(2023))  
print(es_de_traspas(2100))  
print(es_de_traspas(2400))  