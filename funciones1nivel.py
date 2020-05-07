def normal(jigo):  #esta x solo funciona en este ámbito, por lo que podría llamarse como queramos
    return jigo


def cuadrado(chirla):
    return chirla*chirla

def cubo(x):
    return x**3


def sumaTodos(limitTo, chorreras): #Especifica los valores para sumaTodos, limitTo como número total y f como la función sobre la que se calculará
    resultado = 0
    for ayoma in range(limitTo+1):
        resultado += chorreras(ayoma) #ayoma será cada uno de los valores de limitTo para la función chorreras(en le print se hace una llamada a aplicar chorreras como función normal, tal y como indica el print)
        
    return resultado

if __name__ == '__main__': #Este código diferencia si el siguiente bloque está siendo ejecutado directamento o invocado por otro, en ese caso no lo ejecuta
    #Solo si se ejecuta este archivo directamente
    print(sumaTodos(100, normal))  #Le pedimos que nos muestre la función sumaTodos para un limitTo=100 en una una función normal
                            # normal es una llamada a la función def normal (que en este caso no hace nada)
                        #
    print(sumaTodos(3, cuadrado))

#FUNCIONES DE PRIMER NIVEL
# PYTHON ADMITE FUNCIONES COMO PARÁMETROS DE ENTRADA
