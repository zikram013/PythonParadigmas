#1.Escribir un programa que pregunte al usuario su edad y muestre por pantalla si es mayor de edad o no
print("Dime tu edad")
edad=int(input())
if edad<18:
    print("menor de edad")
else:
    print("mayor de edad")

#2.Introducir variable y ver si son iguales sin tener en cuenta mayusculas y minisculas
contrasenia="contraseña"
print("dime tu contraseña")
contraseniaIntroducida=input()
if (contrasenia.lower()==contraseniaIntroducida.lower()):
    print("Iguales")
else:
    print("no iguales")

#3.Escribir un programa que pida al usuario dos numeros y muestre por pantalla su division. Si el divisor es cero debe mostrar un error
print("Dime el dividendo")
dividendo=int(input())
print("Dime el divisor")
divisor=int(input())
if divisor==0:
    print("no se puede dividir por cero")
else:
    print("El resultado de la division es ",divmod(dividendo,divisor))

#4.Escribir un programa que pregunte la edad y sus ingresos y muestre por pantalla si tiene que tributar o no
print("Dime la edad")
edad=int(input())
print("Dime los ingresos")
ingresos=int(input())
if edad >=16 and ingresos >=1000:
    print("tributa")
else:
    print("no tributa")

#5. Los alumnos de un curso se han dividido en dos grupos de acuerdo al sexo y al nombre
#El grupo A esta formado por mujeres con un nombre anterior a la M y los hombres con un
#nombre posterior a la N y el grupo B el resto
#Preguntar nombre y sexo y muestre a que grupo pertenece
print("Dime el sexo")
sexo=input()
print("Nombre")
nombre=input()
if(sexo.lower()=="mujer" and nombre[0].lower()<"m")or(sexo.lower()=="hombre" and nombre[0].lower()>"n"):
    print("Grupo A")
else:
    print ("Grupo B")

#6.Escribir un programa que pregunte al usuario su rente anual y le diga que tipo le corresponde
print("dime tu renta")
renta=int(input())
if(renta<10000):
    print("Tipo del 5%")
elif (renta>=10000 and renta<20000):
    print("Tipo del 15%")
elif (renta>=20000 and renta<35000):
    print("Tipo del 20%")
elif (renta>=35000 and renta<60000):
    print("Tipo del 30%")
else:
    print ("Tipo del 45%")

#7.Escribir un programa que pregunte al usuario por una cantidad a invertir,el interes anual y el numero de años  y muestre su capuital obtenido
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

#Sin bucle
print("Dime el capital a invertir")
capital=int(input())
print("Dime el interes")
interes=float(input())
print("Dime los años")
anyo=int(input())

if(anyo==0 or interes==0.0):
    print("Ha ganado ",capital)
else:
    print (round(capital*(1+interes/100)**anyo,2))