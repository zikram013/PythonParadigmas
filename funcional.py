from functools import reduce
def multiplica(a,b):
    return a*b

salida=map(multiplica,[1,2,3,4],[5,6,7,8])
print(type(salida))
lista=list(salida)
print(lista)


def cuadrado(a):
    return a**2

sal=map(cuadrado,[1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
lis=list(sal)
print(lis)

prueba=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def buscar(valor=0):
    return valor>3

bus=filter(buscar,prueba)
print(list(bus))

print(list(filter(lambda  num:num>3,prueba)))

resultado=reduce(lambda acum=0,elemento=0: acum+elemento,prueba)
print(resultado)

