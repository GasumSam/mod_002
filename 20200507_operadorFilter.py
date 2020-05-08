#Operador filter

lista = [1, 3, -1, 15, 9]


listaPares = filter(lambda x: x % 2 == 0, lista) # filtra de todos los que entran (x:) los que cumplan la siguiente condición, que el resto de x / 2 sea igual a 0 
                                            #Y lo aplicas a lista
'''
#El equivalente a lambda sería esto:

def f(x):
    if x % 2 == 0:
        return x
    else 
        return None
    
    # Es decir, si para los elementos x de la lista f, si x es par (resto = 0), dalo por válido volviendo a x
        #Si no es par, devuelve None
'''        
                
#def esPar(x):
#    return x % 2 == 0
    
#listaPares = filter(lambda x: x % 2 == 0, lista)
#listaPares1 = filter(esPar, lista)
    #Ambas opciones arrojan el mismo valor

#Para todos los valores que sean True, x se va a guardar