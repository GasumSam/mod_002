#Operador reduce
#Recorre todos los elementos devolviendo un único valor

from functools import reduce

lista = [1, 3, -1, 15, 9]

sumatorio = reduce(lambda x, y: x + y, lista)


reduce(lambda x, y: x + y, lista)

# x, y dos parametros donde es x + y y se aplica sobre la lista

# la primera x representa el valor de acumulado, el valor que me va a devolver el reduce
# Ejem: x = 1, x + y /  1 + 3 / x = 4 / 4 + -1 / 3 + 15 / 18 + 9 / x=27


suma100 = reduce(lambda x, y: x + y, range(101))

sumatorioDobles = reduce(lambda x, y: x + y*2, lista)

  