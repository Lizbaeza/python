#números primos 
###### Desarrollado por Liz Baeza 
num = 10000
while True : #el while se usa para hacer como un ciclo mientras, y el true es verdadero 
    es_primo = True
    for x in range(2, num):# para saber si esta en el rango 
        if (num % x == 0):# el if es como un SI , es  una condicional
            es_primo = False

    if es_primo :
        print(f"es primo: {num}")

    num = num + 1