
# Una funcion es de nivel superior si admite como parámetros funciones o su resultado es una función o cumple ambas

#FUNCIÓN de máximo
def maxi(*l):  #*coge los elementos searados por comas
    if len(l) == 0: #l es una array
        return 0  #Si el máximo de l es nada, es igual a 0
    m = l[0]  # el valor inicial de la array l se asigna a la variable m
    for ix in range(1, len(l)):   #recorre los elementos de la array 
        if l[ix] > m: #si el elemento es mayor que m
            m = l[ix]  #el elemento m se asigna a la avariable m
                    #de esta forma m se quedará al final con el elemento mayor de la array
    return m  #vuelve a m


#FUNCIÓN de mínimo
def mini(*l):
    if len(l) == 0:
        return 0
    
    m = l[0]
    
    for ix in range(1, len(l)):
        if l[ix] < m:
            m = l[ix]
            
    return m


def media(*l):
    if len(l) == 0:
        return 0
    
    suma = 0  #Hay que especificar el valor
    
    for valor in l:
        suma += valor
    
    return suma / len(l)

#Creamos un diccionario
funciones = {
    'max': maxi,
    'min': mini,
    'med': media
   
    }


#funcion de primer nivel que nos devuelve otra funcion 
def returnF(nombre):
    nombre = nombre.lower()
    if nombre.lower() in funciones.keys(): #Si nombre(me lo pasas a minusculas) está dentro de las keys del diccionario funciones
        return funciones[nombre]
    
    return None

#invocando la función returnF(invoca una array del diccionario) ejecuta otra función

'''
Ejemplo: returnF('min')(1, 3, -1, 15, 9)
Devuelve_ -1

'''