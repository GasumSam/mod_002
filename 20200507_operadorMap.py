#Operador map

lista = [1, 3, -1, 15, 9]

listaDobles = map(lambda x: x*2, lista) #map indica que la función lambda se aplicara sobre cada uno de los índices, en este caso X:, es decir, desde el valor determinado en su índice 0 (en nuestro caso con el valor 1) en adelante.
#A cada elemento se le hace la transformación lambda



''' 
list(listaDobles)
Out[25]: [2, 6, -2, 30, 18]
'''

'''
def romanNumbers(x):
    .......
    #con una función que determina número romanos, por ejemplo
    
romanos = map(romanNumbers, lista)

    #el map indicaría en este caso que la función def romanNumbers se aplica sobre cada uno de los elementos de la lista