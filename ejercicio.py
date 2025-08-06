# para poner al cuadrado se pone **
#ejercico 5
inicio = 0
limite = 0
print("prog. que imprime num pares ")
inicio = int(input("ungrese el valor de inicio:"))# int para agregar texto con valor númerico
limite =int(input("ahora el valor de fin"))
for x in range (inicio,limite):
    if(x % 2 == 0):
        print(f"l {x}",end=" ")