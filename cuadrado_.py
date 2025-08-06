# EJERCICIO DEL CUADRADO Y TRIANGULO
# Desarrollado por Liz Baeza 
limite = int(input("ingrese el número que quiere su triangulo: \n"))# la barra invertida es para que los resultados salga en una sola fila
for x in range (limite):
    print("#" * x)# el print es como el imprimir 


tam = int(input("ingrese el número que requiere su cuadrado: \n"))# el int se usa para cargar una número
for x in range(1,tam + 1):
    if (x != 1 )and (x != tam):
        print("*"+" " * (tam - 2)+ "*")
    else:# else es como el SI/NO
        print("*" * tam)
