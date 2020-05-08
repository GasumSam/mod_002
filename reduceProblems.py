from functools import reduce

def SumatorioClasico(l):
    resultado = 0
    for valor in l:
        resultado += valor
        
    return resultado

def SumatorioDobleClasico(l):
    resultado = 0
    for valor in l:
        resultado += valor *2
        
    return resultado

def ProductoTotal(l):
    resultado = 1
    for valor in l:
        resultado *= valor
    return resultado

lista = [1, 3 , -1, 15 , 9]

sumatorio = reduce(lambda x, y: x + y, lista)
# creo una copia de la lista
l = lista [:] # copia de la lista para todos sus elementos
# añado el neutro para la suma en la posición cero, de esta forma creo el valor de referencia en el reduce (que def sí permite indicarlo con resultado =)
l.insert(0,0)
sumatorioDobles = reduce(lambda x, y: x + y*2, l)

print(sumatorio)
print(sumatorioDobles)


#Al trabajar con listas, otraLista = l, otraLista apunta a l, por lo que si modificamos otraLista, modificaremos l (un espejo)
#Al utilizar [:] estamos indicando que la nueva variable tome los elementos (todos) de la lista, es decir una copia, no un espejo
#De esta forma si modificamos otraLista tras el = l[:], l no se verá alterada
#En nuestro ejercicio de eliminar el error de reduce, como no queríamos cargarnos la lista original, ser realiza una copia de 
    #sus elementos con [:], para seguidamente insertar a l (l.insert) el valor 0 para su posición 0
        #Así se crea el valor de referencia para el reduce con lambda, como ocurría con la def