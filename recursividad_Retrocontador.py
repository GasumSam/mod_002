
# Ambas funciones son lo mismo

def retrocontador(e):
    print("{},".format(e), end="")
    if e != 0:
        retrocontador(e-1)

print(retrocontador(5))


def contadoratras(e):
    print("{},".format(e), end="")
    if e == 0:
        return None
    contadoratras(e-1)
    
print(contadoratras(10))


def sumatorio(n):
    if n != 0:   #if n > 0:
        return n + sumatorio(n-1)  #Solo ejecutas esta línea si n != 0
#Es necesario devolver algo que no sea None (peta al sumar con un número)
    return 0 #Devuelve 0, que sumado a n no altera el resultado

print(sumatorio(10))

#Cadena de funcionarios, el de más arriba no puede terminar hasta que no termina el funcionario anterior

# 5*4*3*2*1 =  120
def factorial(n):
    if n > 0:
        return n * factorial(n-1)
    return 1

print(factorial(5))