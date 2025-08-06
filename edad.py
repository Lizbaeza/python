#desarrollado porLiz Baeza 
edad=int (input(f"ingrese su edad:"))
print(f"usted tiene {edad} años")
if edad >=18:
    print(f"usted es mayor de edad . Acceda a la licencia de adulto") 
elif edad<18 and edad >=16 :
    print (f"usted es menor de edad.licencia de Menor")
else:
    print (f"usted no puede tener aun licencia")
    diferencia = 18 - edad
    print(f"vuelva dentro de {diferencia} años")




