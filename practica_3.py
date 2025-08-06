# Traductor español-inglés con diccionario
#### Desarrolado por Liz Baeza.
traductor = {
"hola": "hello",
"adiós": "goodbye",
"gracias": "thank you",
"por favor": "please",
"perro": "dog",
"gato": "cat"}

while True:# mientras sea verdadero
    palabra = input("\nIntroduce una palabra en español (0 para salir): ").lower() #.lower para facilitar palabras
    
    if palabra == "0":#SI la palabra es igual a 0 finalizar
        print("Programa finalizado.")
        break

    if palabra in traductor:
        print(f"La traducción de '{palabra}' es: '{traductor[palabra]}'")
    else:
        print(f"La palabra '{palabra}' no está en el diccionario.")
        agregar = input("¿Deseas agregar esta palabra al diccionario? (s/n): ").lower()
        if agregar == "s":
            traduccion = input(f"Introduce la traducción de '{palabra}': ").lower()
            traductor[palabra] = traduccion
            print(f"Palabra '{palabra}' agregada con la traducción '{traduccion}'")   
        else:
            print("Palabra no agregada.")

print("\nDiccionario final:")
for esp, ing in traductor.items():
    print(f"{esp} -> {ing}")
