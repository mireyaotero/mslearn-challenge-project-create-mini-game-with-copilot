import random

opciones = ['piedra', 'papel', 'tijeras']

def eleccion_usuario():
    eleccion = input("Elige piedra, papel o tijeras: ")
    if eleccion in opciones:
        return eleccion
    else:
        print("Entrada no válida. Inténtalo de nuevo.")
        return eleccion_usuario()

def eleccion_computadora():
    return random.choice(opciones)

def determinar_ganador(usuario, computadora):
    if usuario == computadora:
        return "Es un empate"
    elif (usuario == "piedra" and computadora == "tijeras") or (usuario == "papel" and computadora == "piedra") or (usuario == "tijeras" and computadora == "papel"):
        return "¡Ganaste!"
    else:
        return "Perdiste"

def seguir_jugando():
    respuesta = input("¿Quieres seguir jugando? (sí/no): ")
    if respuesta.lower() == 'sí':
        juego()
    elif respuesta.lower() == 'no':
        print("¡Gracias por jugar!")
    else:
        print("Entrada no válida. Inténtalo de nuevo.")
        seguir_jugando()

def juego():
    usuario = eleccion_usuario()
    computadora = eleccion_computadora()
    print("Tu elección:", usuario)
    print("Elección de la computadora:", computadora)
    print(determinar_ganador(usuario, computadora))
    seguir_jugando()

#choose to continue playing or not
juego()