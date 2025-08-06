texto = input('Introduce un nombre de fichero')
nombre_fichero = 'archivo-' + texto + '.txt'
f = open(nombre_fichero, 'w')  # apertura w = write, r = read, a = append
mensaje = input("Ingrese un texto")
f.write(f'{mensaje}\n')
f.close()
