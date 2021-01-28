#1-Leer los datos de los trabajadores
#2.menu
#3.Paradigma objetos: Clase Trabajador
#4.Paradigma estructurado: Menu,lectura del fichero
#5.Paradigma funcional: Estadisticas

class Trabajador:
    """Clase que contiene los datos personales"""
    def __init__(self,nombre,apellido1,apellido2,edad,sexo,igm,igg):
        self.nombre=nombre
        self.apellido1=apellido1
        self.apellido2=apellido2
        self.edad=edad
        self.sexo=sexo
        self.igm=igm
        self.igg=igg

    def __str__(self):
        return self.nombre+" "+self.apellido1+" "+self.apellido2+" "+str(self.edad)+" "+self.sexo+" "+str(self.igm)+" "+str(self.igg)

def leer_datos(trabajadores):

    with open("trabajadores.txt","r",encoding="UTF-8")as fichero:
        for linea in fichero.readlines():
            valores=linea.split()
            nombre=valores[0]
            apellido1=valores[1]
            apellido2=valores[2]
            edad=valores[3]
            sexo=valores[4]

            if valores[5].lower()=='no':
                igm=0
            elif valores[5].lower()=='sí':
                igm=1

            if valores[6].lower()=='sí':
                igg=1
            elif valores[6].lower()=='no':
                igg=0
            #igm=valores[5]
            #igg=valores[6]
            objeto_trabajador=Trabajador(nombre,apellido1,apellido2,edad,sexo,igm,igg)
            trabajadores.append(objeto_trabajador)


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
           contar_trabajadores(lista_trabajadores)
        elif opcion==2:
            contar_trabajadores_igm(lista_trabajadores)
        elif opcion==3:
            contar_trabajadores_igg(lista_trabajadores)
        elif opcion==4:
            contar_trabajadores_ambas(lista_trabajadores)
        elif opcion==5:
            contar_trabajadores_sin_ig(lista_trabajadores)
        elif opcion==6:
            mujeres_con_alguna(lista_trabajadores)
        elif opcion==7:
            hombres_con_alguna(lista_trabajadores)
        elif opcion==8:
            break

#Contrar trabajadores
def contar_trabajadores(lista_trabajadores):
    print(len(lista_trabajadores))

#Igg positiva
def contar_trabajadores_igg(lista_trabajadores):
    iggPositiva=filter(lambda v: v.igg.lower()=='si'and v.igm.lower()=='no',lista_trabajadores)
    for posi in iggPositiva:
        print(posi)

#igm positiva
def contar_trabajadores_igm(lista_trabajadores):
    igmPositiva=list(filter(lambda v: v.igg=='No' and v.igm=='Sí',lista_trabajadores))
    print(len(igmPositiva))

#Trabajadores con ambas
def contar_trabajadores_ambas(lista_trabajadores):
    positivos=list(filter(lambda v: v.igg=='Sí' and v.igm=='Sí',lista_trabajadores))
    print(len(positivos))

#Trabajadores sin ig
def contar_trabajadores_sin_ig(lista_trabajadores):
    limpios=list(filter(lambda v: v.igg=='No' and v.igm=='Sí',lista_trabajadores))
    print(len(limpios))

#Mujeres
def mujeres_con_alguna(lista_trabajadores):
    mujeres=list(filter(lambda v: v.sexo=='M',lista_trabajadores))
    totalMujeres=len(mujeres)
    print("Mujeres: ",totalMujeres)
    positivas=list(filter(lambda w: int(w.igg)==1 or int(w.igm)==1,mujeres))
    print("El porcentaje es mujeres: ",(len(positivas)*100)/totalMujeres)

#hombres
def hombres_con_alguna(lista_trabajadores):
    hombres=list(filter(lambda v: v.sexo=="H",lista_trabajadores))
    totalHombres=len(hombres)
    print("Hombres: ",totalHombres)
    positivos=list(filter(lambda w: int(w.igg)==1 or int(w.igm)==1,hombres))
    print("El porcentaje es hombres: ",(len(positivos)*100)/totalHombres)


lista_trabajadores=[]
leer_datos(lista_trabajadores)
contar_trabajadores(lista_trabajadores)
#for i in lista_trabajadores:
 #   print(i)
contar_trabajadores(lista_trabajadores)

mujeres_con_alguna(lista_trabajadores)
hombres_con_alguna(lista_trabajadores)

#iggPositiva=list(filter(lambda v: int(v.igg)==1,lista_trabajadores))
#for posi in iggPositiva:
#   print(posi)
#print("Igg positiva",len(iggPositiva))

#igmPositiva=list(filter(lambda v: v.igm.lower()=='sí',lista_trabajadores))
#positivosSoloIgm=list(filter(lambda w: str(w.igg.lower())=='sí',igmPositiva))
#print("solo positivos igm",len(positivosSoloIgm))
#for i in positivosSoloIgm:
#    print(i)

#contador=0
#for i in lista_trabajadores:
#    if igm(i)=='Sí' and igg(i)=='No':
#        contador=contador+1

#print(contador)
#contar_trabajadores_igg(lista_trabajadores)
#contar_trabajadores_igm(lista_trabajadores)
#menu()
