#prom de calif
calif = 1
Sumatoria = 0
contador = 0
while (calif != 0):
    calif = int(input ("ingrese calif:"))
    if (calif != 0):
        if (calif >= 1 and calif <= 5):
            Sumatoria = Sumatoria + calif
            contador = contador + 1
        else:
            print("dato invalido")


print("-------------------")
print(f"promedio general: {Sumatoria / contador} ")