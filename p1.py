def sumaTodos(ninoPolla):
    resultado = 0
    for chocho in range(0, ninoPolla+1):
        resultado += chocho
        
    return resultado

print(sumaTodos(1000))

def sumaTodosLosCuadrados(limitTo):
    resultado = 0
    for i in range(limitTo+1):
        resultado += i*i
        
    return resultado

print(sumaTodosLosCuadrados(3))