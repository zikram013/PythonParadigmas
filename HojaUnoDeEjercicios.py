#2.Escribe un programa que muestre por pantalla la cadena ¡Hola mundo!
print("¡Hola mundo!")
#3.Escribir un programa que almacene la cadena hola mundo en una variable y luego muestro por pantalla su contenido
saludo="Hola mundo en variable"
print(saludo)
#4.Escribir un programa que pergunte el nombre del usuario y depsues de que el usuario lo introduzca muestre hola y el nombre introducido
print("¿Cual es tu nombre?")
nombre=input()
print("Hola ",nombre)
#5.Escribir un programa que pregunte el nombre de usuario en la consola, lo muestre en mayusculas y diga el numero de letras
print("Dime el nombre")
nombreLongitud=input()
print("el nombre en mayusculas es ",nombreLongitud.upper()," y tiene una longitud de ",len(nombreLongitud))
#6.Escribir un programa que pida al usuario su peso en kilos y su estatura y calcule tu indice de masa corporal
print("Dime el peso")
peso=int(input())
print("Dime la estatura")
estatura=float(input())
#estatura=estatura*estatura
imc=peso/(estatura**2)
print("El indice de msasa corporal es ",round(imc,2))
#7.Escribir un programa que pida al usuario dos numeros enteros y muestre por pantalla la division completa entre ambos
print("Dime el dividendo")
dividendo=int(input())
print("Dime el divisor")
divisor=int(input())
print("La division entre ",dividendo," y ",divisor," da de cociente ",dividendo//divisor," y de resto ",dividendo%divisor)
#8.Escribir un programa que almacene una cadena de caractares en una variable e introducir otra cadena y compararlas. No hay que tener en cuenta las mayusculas y minisculas
contrasenia="contraseña"
print("Dime la contraseña")
contraseniaIntroducida=input()
print(contrasenia.lower() == contraseniaIntroducida.lower())