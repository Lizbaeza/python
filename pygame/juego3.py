### Desarrollado por liz 
import random

def lanzar_dados():
    dado1 = random.randint(1, 6)
    dado2 = random.randint(1, 6)
    return dado1, dado2

def jugar():
    print("🎲 Bienvenido al juego de dados 🎲")
    while True:
        input("Presiona Enter para lanzar los dados...")
        d1, d2 = lanzar_dados()
        print(f"Lanzaste: {d1} y {d2}")
        print(f"Suma total: {d1 + d2}")
        
        opcion = input("¿Quieres lanzar de nuevo? (s/n): ").lower()
        if opcion != 's':
            print("Gracias por jugar. ¡Hasta luego!")
            break

# Ejecutar el juego
jugar()
