from ventiuno21feb import *

class Juego:
    def __init__(self):
        self.mazo = Mazo ()
        self.casa = Mazo (True)
        self.jugador = Mazo(True)
    
    def iniciar_juego (self):
        self.casa.agregar_carta(self.mazo.dar_carta())
        self.casa.agregar_carta(self.mazo.dar_carta())
        self.jugador.agregar_carta(self.mazo.dar_carta())
        self.jugador.agregar_carta(self.mazo.dar_carta())
    
    def mostrar_juego(self):
        print ("jugador: ")
        self.jugador.mostrar_cartas()
        print ("casa: ")
        self.casa.mostrar_cartas()