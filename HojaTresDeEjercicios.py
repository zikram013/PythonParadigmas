#1.Escribir un programa que pida al usuario una palabra y la muestre 10 veces
print("Dime la palabra a repetir")
repetir=input()
for i in range(10):
    print(i," repetir")

#2.Escribir un programa que pregunte al usuario su edad y muestr por pantalla todos los años que ha cumplido
print("Dime tu edad")
cumpleaños=int(input())
for i in range(cumpleaños):
    print("Años cumplidos ",i+1)

#3.Escribir un programa que pida al usuario un numero entero positivo y muestre todos los impares
print("Dime un numero")
numero=int(input())
for i in range(numero+1):
    if i%2 != 0:
        print(i, end=", ")

#4.Escribir un programa que pida al usuario un numero entero positivo y muestre por pantalla su cuenta atras
print("dime un numero")
temporizador=int(input())
for i in range(temporizador,-1,-1):
    print(i, end=",")

#5.inversiones por año
print("Dime el capital a invertir")
capital=int(input())
print("Dime el interes")
interes=float(input())
print("Dime los años")
anyo=int(input())

if(anyo==0 or interes==0.0):
    print("Ha ganado ",capital)
else:
    for i in range (anyo):
        capital=capital*(1+interes/100)
        print("En el año ",i+1," ha ganado: ",round(capital,2))

#6.Escribir un programa que puda un numero entero y muestre un triangulo rectangulo
print("dame altura")
altura=int(input())
for i in range (altura):
    for j in range(i+1):
        print("*",end="")
    print("")
#7.Escribir un programa que muestre por pantalla la tabla de multiplicar del 1 al 10
multiplicador=10
print("Dime la tabla")
tabla=int(input())
for i in range (multiplicador):
    print( tabla," * ",i+1," = ",(i+1)*tabla)

#8.Escribir un programa que pida al usuario un numero entero por pantalla y cree un triangulo con impares
n = int(input("Introduce la altura del triángulo (entero positivo): "))
for i in range(1, n+1, 2):
    for j in range(i, 0, -2):
        print(j, end=" ")
    print("")