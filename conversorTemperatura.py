#Los atributos en objetos corresponden al estado

#Atributos
class Termometro():
    def __init__(self):  #CONSTRUCTOR EN VACÍO
        self.__unidadM = 'C'    #Al añadir la doble línea baja delante, los convertimos en privados por lo que creo un getter y setter
        self.__temperatura = 0
        
    def __str__(self):
        return "{}º {}".format(self.__temperatura, self.__unidadM)
   
# GETTER Y SETTER DE UNIDAD DE MEDIDA
    def unidadMedida(self, uniM=None):
        if uniM == None:
            return self.__unidadM
        else:
            if uniM == 'F' or uniM == 'C':
                self.__unidadM = uniM

# GETTER Y SETTER DE LA UNIDAD DE TEMPERATURA
    def temp(self, temperatura=None):
        if temperatura == None:
            return self.__temperatura
        else:
            self.__temperatura = temperatura
            
#CIRCUITERÍA
            
    #Funciones
    def __conversor(self, temperatura, unidad):
        if unidad == 'C':
            return "{}º F".format(temperatura * 9/5 + 32)
        elif unidad == 'F':
            return "{}º C".format((temperatura - 32) * 5/9)
        else:
            return "unidad incorrecta"
            T2
    def mide(self, uniM=None):
        if uniM == None or uniM == self.__unidadM:  #¿LA UNIDAD NO TIENE MEDIDA O CORRESPONDE CON LA EL ATRIBUTO INICIAL?, es decir, coincido o no se informa
            return self.__str__()
        else:           #SI ES OTRA HAGO LA CONVERSIÓN
            if uniM == 'F' or uniM == 'C':
                return self.__conversor(self.__temperatura, self.__unidadM)
            else:
                return self.__str__()   