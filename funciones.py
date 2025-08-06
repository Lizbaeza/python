def cargar_lista():
    """Función para cargar elementos a una lista desde el teclado."""
    lista = []
    while True:
        elemento = input("Introduce un elemento (0 para terminar): ")
        if elemento == "0":
            break
        lista.append(elemento)
    return lista

def imprimir_lista(lista):
    """Función para imprimir los elementos de una lista."""
    print("\nContenido de la lista:")
    for i, item in enumerate(lista, start=1):
        print(f"{i}. {item}")

# Programa principal
if __name__ == "__main__":
    print("=== CARGA DE LISTA ===")
    mi_lista = cargar_lista()
    imprimir_lista(mi_lista)
