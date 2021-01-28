#1.Escribir un programa que almacene las asignaturas de un curso en una lista y las muestre por pantalla
asignaturas=["Mates","Fisica","Quimica"]
print(asignaturas)
#2.Escribir un programa que almacene asignaturas en una lista y la muestra en una lista
asignaturas=["Mates","Fisica","Quimica"]
for asig in asignaturas:
    print("Yo estudio ",asig)
#3.Escribir un programa que almacene asignaturas en una lista y pregunte que nota ha sacado
asignaturas=["Mates","Fisica","Quimica"]
notas=[]
for asig in asignaturas:
    print("¿Que nota has sacado? ",asig)
    calificacion=input()
    calificacion.append(notas)

for i in range(len(asignaturas)):
    print("Asignatura ",asignaturas[i]," nota ",notas[i])

#4.Escribir un programa que pregunte al uusario lo numero de la loteria, los almacene y los muestre de menor a mayor
loteria=[]
for i in range(6):
    premiados=int(input())
    loteria.append(premiados)
loteria.sort()
print("los numeros premiado son :" + str(loteria))

#5.Escribir una lista del 1 al 10 y mostrarla en orden inverso
numeros=[]
for i in range(10):
    numeros.append(i+1)
numeros.reverse()
for j in numeros:
    print(j, end=", ")

#6. Escribir un programa que pida al usuario una palabra y muestre por pantalla cuantas veces sale cada vocal
print("dime una palabra")
palabra=input()
palabra.lower()
contadorA=0
contadorE=0
contadorI=0
contadorU=0
contadorO=0

for i in palabra:
    if (i=="a"):
        contadorA=contadorA+1
    elif(i=="e"):
        contadorE=contadorE+1
    elif(i=="i"):
        contadorI=contadorI+1
    elif(i=="o"):
        contadorO=contadorO+1
    elif(i=="u"):
        contadorU=contadorU+1

print("Numero de veces que aparece a ",contadorA)
print("Numero de veces que aparece e ",contadorE)
print("Numero de veces que aparece i ",contadorI)
print("Numero de veces que aparece o ",contadorO)
print("Numero de veces que aparece u ",contadorU)

#7.Escribir un programa que almacene el abcederacio en una lista y elimine aquellas que su posicion es multiplo de 3
abcedarios=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'ñ', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
for i in range(len(abcedarios),1,-1):
    if i%3==0:
        abcedarios.pop(i-1)
print(abcedarios)