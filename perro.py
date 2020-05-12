class Dog():
    def __init__(self): #Cuando intentes peter los atributos (miko = Dog('miko', 3, 8'), peta. Est� especificado solo el propio atributo self
        self.nombre = ""
        self.edad = None
        self.peso = None 

    def ladrar(self):
        if self.peso == None:
            print("Soy un fantasma")
            
        if self.peso >= 8:
            print("GUAUm GUAU")
        else:
            print("ay, ay")
            

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
        self.__trabajando = False  #Crea ubn atributo nuevo. Cuando se invoca por defecto a False
        
        #con rantanplan.trabajando = True cambio el estad y su ladrido cambia
            
    def __str__(self):   #Al ser una función que procede de la anterior clase, lo que se está haciendo es 'sobreescribir' el método
        return "Perro de asistencia de {}".format(self.amo)
            
    def pasear(self):
        print("{} ayudo a mi dueño, {} a pasear". format(self.nombre, self.amo))

    def ladrar(self):   #Sobreescribimos ladrar
        if self.trabajando:
            print("shhhhh, no puedo ladrar")
        else:
            Perro.ladrar(self)  #Invoco a la instancia original  (Método padre)
    
#definimos nuevos m�todos
            
    def trabajando(self, valor=None): #El valor, si no se informa en la funci�n, le doy el valor nulo 
        if valor == None:   #No se ha informado el valor? pues me devuelves el que tiene
            return self.__trabajando
        else:       #Se ha informado el valor? Si la respuesta es s�, as�gnalo a __trabajando
            self.__trabajando = valor 
            
#trabajando() GETTER
#trabajando(True)   SETTER
            
            # rantanplan._PerroAsistencia__trabajando()
            # rantanplan.trabajando()  GETTER
            # rantanplan.trabajando(True/False)  SETTER
            
            
            
'''
salchicho = Perro('Salchicho', 3, 12)

lola = Perro('Lola', 8, 1.5)

miko = Perro('Miko', 8, 3)

'''