### Desarrollado por Liz Baeza 
calificaciones = [1,2,3,5,5]
nombres = ["Moises","Camila","Fernanda","Pablo","Tania"]
lista_variada = [True, 10.5 ,"abc",[ 0,1,1]]

print("estudiante: ", nombres[2])# la lista viaja el 0 hata el limite
print("calificación: ", calificaciones[-2])
print("lista dentro de otra: ", lista_variada[3][0])
print("imprimir un rango o slices", nombres[1:2])
print(lista_variada)

# agregar elementos a la lista
nombres.append("Anibal")
print(nombres)

# remover elementos de una lista 
nombres.remove("Pablo")
print(nombres)
