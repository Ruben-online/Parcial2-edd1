from binary_tree import *


while True:
    print("\nMenu principal, Juego adivinanzas")
    print("1. Construir el arbol de adivinanzas")
    print("2. Iniciar el juego")
    print("3. Reiniciar el juego")
    print("4. Salir del juego")

    menu_option = input("Ingrese una opcion: ")

    if menu_option == "1":
        arbol = construir_arbol()

    elif menu_option == "2":
        if arbol:
            jugar(arbol)
        else:
            print("Por favor, primero debes de construir el arbol binario.")

    elif menu_option == "3":
        arbol = None

    elif menu_option == "4":
        print("Saliendo del programa...")
        break
    else:
        print("Intentelo de nuevo")