##Creamos la clase Persona
class Persona:
    def __init__(self):
        self.resultadoPruebas=[]

    def lecturaFicher(self,fich):
        file=open(fich,'r',encoding='UTF-8')
        for lineas in file.readlines():
            nombre,apellido1,apellido2,edad,sexo,igm,igg=lineas.split()
            edad=int(edad)
            self.resultadoPruebas.append({'nombre':nombre,'apellido1':apellido1,'apellido2':apellido2,'edad':edad,'sexo':sexo,'igm':igm,'igg':igg})
        file.close()
        
    def leerDatos(self):
        print(self.resultadoPruebas)
    
    def obtenerDiccionarioDeDatos(self):
        datos=self.resultadoPruebas
        return datos

##menu
def menu():
    print("1.Total trabajadores")
    print("2.trabajadores con igm")
    print("3.trabajadores con igg")
    print("4.trabajadores con ambas")
    print("5.trabajadores limpios")
    print("6.Mujeres con alguna")
    print("7.Hombres con alguna")
    print("8.Salir")
    opcion=int(input())
    while True:
        if opcion==1:
           print(contarDatos(persona.obtenerDiccionarioDeDatos())) 
        elif opcion==2:
            print(trabajadoresConIgm(persona.obtenerDiccionarioDeDatos()))
        elif opcion==3:
            print(trabajadoresConIgg(persona.obtenerDiccionarioDeDatos()))
        elif opcion==4:
            print(trabajadoresConIggeIgm(persona.obtenerDiccionarioDeDatos()))
        elif opcion==5:
            print(trabajadoresSinIggeIgm(persona.obtenerDiccionarioDeDatos()))
        elif opcion==6:
            print(porcentajeMujeres(contarMujeres(persona.obtenerDiccionarioDeDatos())))
        elif opcion==7:
            print(porcentajeHombres(contarHombres(persona.obtenerDiccionarioDeDatos())))
        elif opcion==8:
            break

##metodo contar trabajadores
def contarDatos(data):
    print(len(data))
    cantidadDatos=len(data)
    return cantidadDatos

##trabajadores con igm
def trabajadoresConIgm(data):
    contador=0
    for i in data:
        if i['igm']=='Sí':
            contador=contador+1
    return contador

#Trabajadores con igm
def trabajadoresConIgg(data):
    contador=0
    for i in data:
        if i['igg']=='Sí' and i['ign']=='No':
            contador=contador+1
    return contador

#Trabajadores con ambas
def trabajadoresConIggeIgm(data):
    contador=0
    for i in data:
        if i['igm']=='Sí' and i['igg']=='Sì':
            contador=contador+1
    return contador

#Trabajadores limpios
def trabajadoresSinIggeIgm(data):
    contador=0
    for i in data:
        if i['igm']=='No' and i['igg']=='No':
            contador=contador+1
    return contador

def contarMujeres(data):
    contadorMujeres=0
    diccionarioMujeres=[]
    for i in data:
        if i['sexo']=='M':
            contadorMujeres=contadorMujeres+1
            diccionarioMujeres.append({'n':i['nombre'],'a1':i['apellido1'],'a2':i['apellido2'],'e':i['edad'],'s':i['sexo'],'im':i['igm'],'ig':i['igg']})
    return diccionarioMujeres

def contarHombres(data):
    diccionarioHombres=[]
    for i in data:
        if i['sexo']=='H':
            diccionarioHombres.append({'n':i['nombre'],'a1':i['apellido1'],'a2':i['apellido2'],'e':i['edad'],'s':i['sexo'],'im':i['igm'],'ig':i['igg']})
    return diccionarioHombres

def porcentajeMujeres(mujeres):
    totalMujeres=len(mujeres)
    contador=0
    for i in mujeres:
        if (i['im']=='Sí' or i['ig']=='Sì'):
            contador=contador+1
    return contador*100/totalMujeres

def porcentajeHombres(hombres):
    totalHombres=len(hombres)
    contador=0
    for i in hombres:
        if (i['im']=='Sí' or i['ig']=='Sì'):
            contador=contador+1
    return contador*100/totalHombres
  

persona=Persona()
persona.lecturaFicher('trabajadores.txt')
menu()
