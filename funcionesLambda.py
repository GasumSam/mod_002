#import funciones1nivel  #tengo acceso a las funciones de ese archivo

import sumaTodos from funciones1nivel


print(sumaTodos(3, lambda x: x**3)) #una función sin nombre / después de los dos puntos se especifica la función

'''
Esto es lo mismo
 
doble = lambda x: x*2

print(sumaTodos(3, doble))

'''