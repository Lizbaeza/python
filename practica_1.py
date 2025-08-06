notas = []

for x in range(3):
    nota = 0
    while nota <1 or nota > 5:
        nota = int(input(f"nota {x+1}: "))

    notas.append(nota)

suma = 0
for x in range (len(notas)):
    suma = suma + notas [x]
promedio= suma / len(notas)
print(f"promedio: {promedio}")

if (promedio > 1.7):
    print("APROBADO ;) ")
else:
    print("REPROBADO :( ")