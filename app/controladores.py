from vista import VistaCifrador, VistaEncabezado
from modelos import Cifrador
from simple_screen import Print, locate, Input, init, finish, cls



def main(): 
    init()
    
    while True:
        locate(100, 2)
        Print("CIFRADO CESAR")

        locate(100, 3)
        Print("=============")

        locate(100, 4)
        distancia = int(Input("Distancia cifrado: "))

        locate(100, 5)
        mensaje = Input("Mensaje a descifrar: ")

        cifrado = Cifrador(distancia)
        mensaje_cifrado = cifrado.cifrar(mensaje)

        locate(100, 6)
        Print(f"Mensaje cifrado: {mensaje_cifrado}")

        locate(100, 7)
        seguir = Input("¿Otro mensaje (S/n)?")
        if seguir.lower() != "s":
            break
        cls()
finish()    

if __name__ == "__main__":
    main()