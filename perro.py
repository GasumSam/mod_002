class Perro():
    def __init__(self, n, e, p):  #El constructor me permite construir la instancia (la copia del objeto que fija las características)
        self.nombre = n  #El atributo nombre de la clase propia (self) es el que ocupa el segundo lugar del paréntesis
        self.edad = e
        self.peso = p

        #Self no se informa, ya está informado de forma implícita, en el caso de añadir parámetro sí se informa
    def ladrar(self): #El primer parámetro de los miembros de una clase es la propia clase # en vez de self podemos poner cualquier cosa
        if self.peso >= 8:
            print("GUAU, GUAU")
        else:
            print("ay, ay")
            
            #El primer parámetro es siempre la instancia, recuerda
         
    def __str__(self):  #Método específico que devuelve una cadena
        return "Perro {}, e: {}, p: {}".format(self.nombre, self.edad, self.peso)
    

class PerroAsistencia(Perro):
    def __init__(self, nombre, edad, peso, amo):
        Perro.__init__(self, nombre, edad, peso)
        self.amo = amo 
        self.trabajando = False  #Crea ubn atributo nuevo. Cuando se invoca por defecto a False
            
    def __str__(self):   #Al ser una función que procede de la anterior clase, lo que se está haciendo es 'sobreescribir' el método
        return "Perro de asistencia de {}".format(self.amo)
            
    def pasear(self):
        print("{} ayudo a mi dueño, {} a pasear". format(self.nombre, self.amo))

    def ladrar(self):   #Sobreescribimos ladrar
        if self.trabajando:
            print("shhhhh, no puedo ladrar")
        else:
            Perro.ladrar(self)  #Invoco a la instancia original  (Método padre)
    
            
            
            
'''
salchicho = Perro('Salchicho', 3, 12)

lola = Perro('Lola', 8, 1.5)

miko = Perro('Miko', 8, 3)

'''