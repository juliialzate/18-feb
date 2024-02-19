
class Animal: 
    def __init__(self, nombre, raza): 
        self.nombre = nombre
        self.raza = raza 
    
    def pasear(self):
        pass

    def alimentar(self):
        pass

    def dar_info(self):
        return self.nombre + " de raza: " + self.raza 

class Mascota(Animal):
    def __init__(self, nombre, raza, propietario):
        
        self.propietario = propietario 
        super(Mascota,self).__init__(nombre, raza)

class Gato(Mascota):
    def pasear (self): 
        print ("Paseando al gato" + self.dar_info() + " " + self.propietario)
    
    def alimentar (self):
        print ("Alimentando al gato" + self.dar_info() + " " + self.propietario)

class Perro(Mascota):
    def pasear (self): 
        print ("Paseando al perro " + self.dar_info() + " " + self.propietario)
    
    def alimentar (self):
        print ("Alimentando al perro " + self.dar_info() + " " + self.propietario)

class Lagarto(Mascota):
    def pasear (self): 
        print ("Paseando al lagarto" + self.dar_info() + " " + self.propietario)
    
    def alimentar (self):
        print ("Alimentando al lagarto" + self.dar_info() + " " + self.propietario)

if __name__ == '__main__':
    mascotas = [Perro(" Neron ", " Bulldog ", " Juli"), Gato(" Garfield ", " Angora ", " Juanito "), Lagarto(" Sra. Kipling ", " Mediterraneo ", " Willy ")]
    for m in mascotas: 
        m.pasear()
        m.alimentar()