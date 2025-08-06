#diccionario con usuarios y contraseñas
usuarios = {"juan":"1234","maria":"abcd","ana": "qwerty"}
#solicita el nombre de usuario
usuario = input("ingrese su nombre de usuario")
#verifica si el usuario existe 
if usuario in usuarios:
    intentos = 0
    while True:
        contraseña = input("ingrese su contraseña: ")
        if contraseña == usuarios[usuario]:
            print("¡ACCESO CONCEDIDO!")
            break
        
        elif(intentos < 3):
            intentos += 1
            print("contraseña incorrecta. Intento " ,intentos , "de 3")

        else:
            print("Acceso bloqueado.Demasiados Intentos.")
            break

else:
    print("El usuario no existe :( ") 