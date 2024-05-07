class Nodo:
    def __init__(self, pregunta, izquierda=None, derecha=None):
        self.pregunta = pregunta
        self.izquierda = izquierda
        self.derecha = derecha


def jugar(nodo):
    respuesta = input(nodo.pregunta + " (si/no): ").lower()
    if respuesta == "si":
        if nodo.izquierda:
            jugar(nodo.izquierda)
        else:
            print("Adivinaste!")
    elif respuesta == "no":
        if nodo.derecha:
            jugar(nodo.derecha)
        else:
            objeto = input("No has adivinado.")
            pregunta = input("Ingresa una pregunta que distinga {} de {}: ".format(objeto, nodo.pregunta))
            respuesta_nueva = input("Cual es la respuesta a la pregunta para {}? (si/no): ".format(objeto)).lower()
            if respuesta_nueva == "si":
                nodo.derecha = Nodo(objeto)
                nodo.izquierda = Nodo(nodo.pregunta)
            else:
                nodo.izquierda = Nodo(objeto)
                nodo.derecha = Nodo(nodo.pregunta)
    else:
        print("Respuesta invalida. Por favor, responde con 'si' o 'no'.")
        jugar(nodo)


def reiniciar_juego():
    respuesta = input("Quieres jugar de nuevo? (si/no): ").lower()
    return respuesta == "si"


def construir_arbol():
    arbol = Nodo("Es un animal?",
                 Nodo("Tiene patas?",
                      Nodo("Es domestico?",
                           Nodo("Perro"),
                           Nodo("Gato")),
                      Nodo("Vuela?",
                           Nodo("Pajaro"),
                           Nodo("Halcon"))),
                 Nodo("Es un objeto?",
                      Nodo("Se utiliza para escribir?",
                           Nodo("Lapiz"),
                           Nodo("Lapicero")),
                      Nodo("Es un medio de transporte?",
                           Nodo("Carro"),
                           Nodo("Bus"))))
    print("Arbol de adivinanzas construido con exito.")
    return arbol

arbol = None
