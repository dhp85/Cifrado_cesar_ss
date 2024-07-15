from modelos import Cifrador
from simple_screen import Screen_manager, Input, cls, locate

class VistaEncabezado:
    def __init__(self, x=1, y=1):
        self.x = x
        self.y = y

    def paint(self):
        locate(self.x, self.y, "=============")
        locate(self.x, self.y + 1,"CIFRADO CESAR")
        locate(self.x, self.y +2, "=============")
        



class VistaCifrador:
    def __init__(self, etiqueta: str, x, y):
        self.etiqueta = etiqueta
        self.y = y
        self.x = x
        

    def paint(self):
        locate(self.x, self.y, self.etiqueta)
        return Input()    


print(__name__)
if __name__=="__main__":
    with Screen_manager:

        vi = VistaEncabezado()
        vc = VistaCifrador("Distancia cifrado: ", 1, 4)
        vc2 = VistaCifrador("Mensaje a Cifrar: ", 1, 5)
        vi.paint()
        vc.paint()