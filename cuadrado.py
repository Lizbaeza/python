#ejercicio de cuadrado desarrollado por Liz 
print("Programa que imprime números pares y un cuadrado de asteriscos")

# Solicita al usuario los valores de inicio y fin
inicio = int(input("Ingrese el valor de inicio: "))
limite = int(input("Ahora el valor de fin: "))

# Recorre el rango desde inicio hasta límite (sin incluir el límite)
for x in range(inicio,limite):
    if( x % 2 == 0):  # Si el número es par
        print(f"Número par: {x}")
        print("*"* x)
        print()  # Línea en blanco entre cuadrados
