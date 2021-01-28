#1.Escribir una funcion que muestre por pantalla un saludo cada vez que es invocada
def saludar():
    print("hola funcion")

saludar()

#2.Escribir una funcion a la que se le pase una cadena y muestre por pantalla el saludo
nombre=input("Dime tu nombre: ")
def saludo(nombre):
    print("Hola ",nombre)

saludo(nombre)

#3.Escribir una funcion que reciba un numero entero positivo y devuelva su factoria
print("Dime un numero positivo")
numero=int(input())
def factorial(n):
    if n>1:
        n=n*factorial(n-1)
    else:
        n=1
    return n

calculo=factorial(numero)
print(calculo)

#4.Escribir una funcion que calcule el iva. Se debe pasar la cantidad y el iva. En caso de no pasar el iva se aplicara el 21
print("Dime el precio")
precio=int(input())
print("Dime el iva")
iva=int(input())

def calculoIva(p,i=21):
    return p + p * i/100


precioConIva=calculoIva(precio)
precioConIva2=calculoIva(precio,iva)
print(precioConIva)
print(precioConIva2)

#5.Escribir una funcion que calcule el area de un circulo y otra que calcule el volumen de un cilindro usando la primera funcion
from math import pi
print("dime el radio")
radio=int(input())
print("dime la altura")
altura=int(input())
def circulo(r):
    return pi*r**2

def cilindro(r1,a):
    return circulo(r1)*a

areaCirculo=circulo(radio)
print(areaCirculo)
volumenCilindro=cilindro(radio,altura)
print(volumenCilindro)

#6.Escribir una funcion que reciba una muestra de numero en una lista y devuelva su media
listaNumeros=[1, 2, 3, 4, 5]
def calculoMedia(lista):
    sumaLista=0
    for i in lista:
        sumaLista=sumaLista+i
    return sumaLista/len(lista)

media=calculoMedia(listaNumeros)
print("La media es: ",media)

#7.Escribir una funcion que reciba una muestra de numeros en una lista y devuelva una lista de cuadrados
listaNumeros2=[1,2,3,4,5]
def calculoCuadrado(lista):
    listar=[]
    for l in lista:
        listar.append(l**2)
    return listar
listaCuadratica=calculoCuadrado(listaNumeros2)
print(listaCuadratica)

#8. Escribir una funcion que una muestra de numeros y devielva un diccionario con media,varianza y desviacion tipica
from math import sqrt
listaNumeros3=[1,2,3,4,5]
def estadistica(lista):
    media=0
    for i in lista:
        media=media+i
    media=media/len(lista)
    varianza=0
    for j in lista:
        varianza=(j-media)**2
    varianza=varianza/len(lista)
    desviacionTipica=sqrt(media/varianza)

    diccionario = {"Media":media,"Varianza":varianza,"Desviacion Tipica":desviacionTipica}
    return diccionario

datos=estadistica(listaNumeros3)
print(datos)

#9. Escribir dos funciones. una calcula el mcd y la otra el mcm
print("dime el primer numero")
num1=int(input())
print("dime el segundo numero")
num2=int(input())

def calculoMcd(n1,n2):
    z=1
    if n1%n2==0:
        return n2
    for i in range (int(n2/2),0,1):
            if n1%i==0 and n2%i==0:
                z=i
                break
    return z

def calculoMcm(n1,n2):
    z=max(n1,n2)
    while True:
            if(z%n1==0) and (z%n2==0):
                return z
            z+=1
    return z
mcd=calculoMcd(num1,num2)
print("El mcd es: ",mcd)
mcm=calculoMcm(num1,num2)
print("El mcm es: ",mcm)

#10. Funcion que convierta de binario a decimal y viceversa
def decimalToBinario(n):
    binario=''
    while n //2!=0:
        binario=str(n%2)+binario
        n=n//2
    return str(n)+binario

def binarioToDecimal(b):
    numeroDecimal=0
    for posicion,digito_string in enumerate(b[::-1]):
        numeroDecimal+=int(digito_string)*2**posicion
    return numeroDecimal

dtb=decimalToBinario(81)
print(dtb)
btd=binarioToDecimal('111010101010011')
print(btd)

#11.Funcion con diccionario con repeticiones y tupla con la palabra mas repetida
listaPalabras=["Hola","Hola","Hola","Adios","Adios","Mundo"]
def contarPalabras(lista):
    diccionario={}
    for i in lista:
        if i in diccionario:
            diccionario[i]+=1
        else:
            diccionario[i]=1
    return diccionario
def palabraMasRepetida(diccionario):
    pal=''
    repeticiones=0
    for dicc,rep in diccionario.items():
        if rep>repeticiones:
            pal=dicc
            repeticiones=rep
    return pal,repeticiones

print(contarPalabras(listaPalabras))
print(palabraMasRepetida(contarPalabras(listaPalabras)))