import math
#1.Escribir una función que aplique un descuento a un precio y otra que aplique el IVA  a  un  precio.  Escribir  una  tercera  función  que  reciba  un  diccionario  con  los precios  y  porcentajes  de  una  cesta  de  la compra,  y  una  de  las  funciones anteriores, y utilice la función pasada para aplicar los descuentos o el IVA a los productos de la cesta y devolver el precio final de la cesta
def descuento(p,d):
    precioDescontado=p*((100-d)/100)
    return precioDescontado

def impuesto(p,i):
    precioImpuesto=p*(i/100)
    return precioImpuesto

def cestaCompra(t,funcion):
    total=0
    for precio,des in t.items():
        total+=funcion(precio,des)
    return total

ticketCompra={1000:30,30:43,43:29}
print(cestaCompra(ticketCompra,descuento))
print(cestaCompra(ticketCompra,impuesto))

#2.Escribir una función que simule una calculadora científica que permita calcular el  seno,  coseno,  tangente,  exponencial  y  logaritmo  neperiano.  La  función preguntará al usuario el valor y la función a aplicar, y mostrará por pantalla una tabla con los enteros de 1 al valor introducido y el resultado de aplicar la función a esos enteros.
import math
def menu():
    print("seno")
    print("coseno")
    print("tangente")
    print("exponencial")
    print("logaritmo neperiano")
    opcion=int(input())
    if opcion==1:
        print(seno(numero))
    elif opcion==2:
        print(coseno(numero))
    elif opcion==3:
        print(tangente(numero))
    elif opcion==4:
        print(exponencial(numero))
    elif opcion==5:
        print(logaritmo(numero))

def seno(numero):
    return math.sin(numero)

def coseno(numero):
    return math.cos(numero)

def tangente(numero):
    return math.tan(numero)

def exponencial(numero):
    return math.exp(numero)

def logaritmo(numero):
    return math.log(numero)

numero=45
menu()

#3.Escribir una funcion que reciba otra funcion y una lista y devuelva otra lista con el resultado de aplicar la funcion dad a cada uno de los elementos de la lista
def multiplicar(n):
    return n*n

def recibe(lista,funcion):
    l=[]
    for i in lista:
        l.append(funcion(i))
    return l
list=(3,2,1,4,3)
print(recibe(list,multiplicar))

#4.Escribir una funcion que reciba otra funcion y una lista y devuelva otra lista con los elementos de la lista que devuelven true al aplicarles la funcion booleana
def comprobarTrue(n):
    if n==True:
        return True

def recibe2(lista,funcion):
    l=[]
    for i in lista:
        if comprobarTrue(i)==True:
            l.append(i)
    return l

list2=[2,"gola",True,False,"True"]
print(recibe2(list2,comprobarTrue))

#5.Escribir una funcion que reciba una frase y deuelva un diccionario con las palabras que contiene y su longitud
def frase(f):
    
    pal=f.split()
    longitud=map(len,pal)
    return dict(zip(pal,longitud))

frasecita="hola que tal pero que tal que le vamos a hacer"
print(frase(frasecita))

#6. Escribir una función reciba una lista de notas en formato numérico y devuelva la
#lista de calificaciones (SS, AP, NT, SB, MH) correspondientes a esas notas.
def conversionNotas(notas):
    notasEscritas=[]
    for i in notas:
        if i<5:
            notasEscritas.append("Suspenso")
        elif i>=5 and i<7:
            notasEscritas.append("Aprobado")
        elif i>=7 and i<9:
            notasEscritas.append("Notable")
        elif i>=9 and i<=10:
            notasEscritas.append("Sobresaliente")
    return notasEscritas

notasNumericas=[3,1,5,7,3,1,10]
print(conversionNotas(notasNumericas))

#7.Escribir una función reciba un diccionario con las asignaturas y las notas en
#formato numérico de un alumno y devuelva otro diccionario con las asignaturas
#en mayúsculas y las calificaciones (SS, AP, NT, SB, MH) correspondientes a las
#notas
def converionNotasDiccionario(diccionario):
    diccionarioNotasConversion={}
    for asignatura,nota in diccionario.items():
        if nota<5:
            diccionarioNotasConversion[asignatura.lower()]="Suspenso"
        elif nota>=5 and nota<7:
            diccionarioNotasConversion[asignatura.lower()]="Aprobado"
        elif nota>=7 and nota<9:
            diccionarioNotasConversion[asignatura.lower()]="Notable"
        elif nota>=9 and nota<=10:
           diccionarioNotasConversion[asignatura.lower()]="Sobresaliente"
    return diccionarioNotasConversion

diccionarioNotas={"Fisica":7,"Python":10,"ED":0}
print(converionNotasDiccionario(diccionarioNotas))

#8. Escribir una función reciba un diccionario con las asignaturas y las notas en
#formato numérico de un alumno y devuelva otro diccionario con las asignaturas
#en mayúsculas y las calificaciones correspondientes a las asignaturas aprobadas.
def converionNotasDiccionarioArpobadas(diccionario):
    diccionarioNotasConversion={}
    for asignatura,nota in diccionario.items():
        if nota>=5 and nota<7:
            diccionarioNotasConversion[asignatura.lower()]="Aprobado"
        elif nota>=7 and nota<9:
            diccionarioNotasConversion[asignatura.lower()]="Notable"
        elif nota>=9 and nota<=10:
           diccionarioNotasConversion[asignatura.lower()]="Sobresaliente"
    return diccionarioNotasConversion

diccionarioNotas={"Fisica":7,"Python":10,"ED":0}
print(converionNotasDiccionarioArpobadas(diccionarioNotas))

#-9Construir una función que permita hacer búsqueda de inmuebles en función de
#un presupuesto dado. La función recibirá como entrada la lista de inmuebles y
#un precio, y devolverá otra lista con los inmuebles cuyo precio sea menor o igual
#que el dado. Los inmuebles de la lista que se devuelva deben incorporar un
#nuevo par a cada diccionario con el precio del inmueble, donde el precio de un
#inmueble se calcula con las siguientes fórmulas, en función de la zona:
#• Zona A:
#precio = (metros * 1000 + habitaciones * 5000 + garaje * 15000) * (1-antiguedad/100)
#• Zona B:
#precio = (metros * 1000 + habitaciones * 5000 + garaje * 15000) * (1-antiguedad/100)
#* 1.5
pisos = [{'año': 2000, 'metros': 100, 'habitaciones': 3, 'garaje': True, 'zona': 'A'}, {'año': 2012, 'metros': 60, 'habitaciones': 2, 'garaje': True, 'zona': 'B'}, {'año': 1980, 'metros': 120, 'habitaciones': 4, 'garaje': False, 'zona': 'A'}, {'año': 2005, 'metros': 75, 'habitaciones': 3, 'garaje': True, 'zona': 'B'}, {'año': 2015, 'metros': 90, 'habitaciones': 2, 'garaje': False, 'zona': 'A'}]

def añadir_precio(piso):
    precio = (piso['metros'] * 1000 + piso['habitaciones'] * 5000 + int(piso['garaje']) * 15000) * (1 - (2020 - piso['año']) / 100)
    if piso['zona'] == 'B':
        precio *= 1.5
    piso['precio'] = precio
    return piso

def busca_piso(pisos, presupuesto):
    def filtro(piso):
        return piso['precio'] <= presupuesto

    return pisos(filter(filtro,map(añadir_precio, pisos)))

print(busca_piso(pisos, 100000))
