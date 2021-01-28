''' 
Se ha hecho uso del un paradigma orientado a objetos para almacenar todos los parámetros de los datos dados en el fichero
Al contener todos los datos los mismos atributos, usar POO nos ayuda a clasificarlos según sus atributos ayudando al acceso de estos datos
'''
class Titulacion:
    def __init__(self,nombre_titulacion,escuela,nivel,creditos,anyo_inicio):
        self.nombre_titulacion=nombre_titulacion
        self.escuela=escuela
        self.nivel=nivel
        self.creditos=creditos
        self.anyo_inicio=anyo_inicio

    def __str__(self):
        return self.nombre_titulacion+" "+self.escuela+" "+self.nivel+" "+str(self.creditos)+" "+str(self.anyo_inicio)

'''
Se ha usado un paradigma estructural para leer el fichero y mostrar el menú dado que son operaciones que solo se deben realizar una sola vez
'''

def leer_datos(grados):

    with open("titulaciones.txt","r",encoding="UTF-8")as fichero:
        for linea in fichero.readlines():
            valores=linea.split()
            nombre_titulacion=valores[0]
            escuela=valores[1]
            nivel=valores[2]
            creditos=valores[3]
            anyo_inicio=valores[4]
            objeto_titulacion=Titulacion(nombre_titulacion,escuela,nivel,creditos,anyo_inicio)
            grados.append(objeto_titulacion)

def menu():

    while True:
        print("1.Ver todas las titulaciones")
        print("2.Ver todas las titulaciones por escuela")
        print("3.Ver estadisticas")
        print("4.Salir")
        opcion=int(input())
        if opcion==1:
            mostrar_titulaciones(lista_grados)
        elif opcion==2:
            mostrar_titulaciones_por_escuela(lista_grados)
        elif opcion==3:
            estadisticas=verEstadisticas(lista_grados)
            print(estadisticas)
        elif opcion==4:
            break

'''
Para mostrar los datos se ha decidido usar el paradigma estructural dado que tambien son operaciones que una vez que se lea el fichero no
van a cambiar a la hora de mostrar de datos y simplemente nos deben mostrar las titulaciones de determinada forma.
'''
def mostrar_titulaciones(lista_grados):
    for i in lista_grados:
        print(i)

def mostrar_titulaciones_por_escuela(lista_grados):
    etsii=list(filter(lambda e: e.escuela.lower()=="etsii",lista_grados))
    fcjs=list(filter(lambda e: e.escuela.lower()=="fcjs",lista_grados))
    fcs=list(filter(lambda e: e.escuela.lower()=="fcs",lista_grados))
    escet=list(filter(lambda e: e.escuela.lower()=="escet",lista_grados))
    etsit=list(filter(lambda e: e.escuela.lower()=="etsit",lista_grados))
    fcc=list(filter(lambda e: e.escuela.lower()=="fcc",lista_grados))
    eid=list(filter(lambda e: e.escuela.lower()=="eid",lista_grados))
    emo=list(filter(lambda e: e.escuela.lower()=="emo",lista_grados))
    print("ETSII")
    for i in etsii:
        print(i.nombre_titulacion)
    print("FCJS")
    for i in fcjs:
        print(i.nombre_titulacion)
    print("FCS")
    for i in fcs:
        print(i.nombre_titulacion)
    print("ESCET")
    for i in escet:
        print(i.nombre_titulacion)
    print("ETSIT")
    for i in etsit:
        print(i.nombre_titulacion)
    print("FCC")
    for i in fcc:
        print(i.nombre_titulacion)
    print("EID")
    for i in eid:
        print(i.nombre_titulacion)
    print("EMO")
    for i in emo:
        print(i.nombre_titulacion)


''' 
Para las estadisticas se ha usado el paradigma funcional dado que nos tiene que devolver el valor de las operaciones realizadas.
Para ayudar a este tratamiento se ha hecho uso de la función filter para saber los datos que cumplen unas ciertas condiciones
'''
def verEstadisticas(lista_grados):
    total_titulaciones=len(lista_grados)
    cadenaTitulacion="Total titulaciones de la universidad: "+str(total_titulaciones)+"\n"

    grados=list(filter(lambda g: g.nivel.lower()=="grado",lista_grados))
    porcentaje_grados=(len(grados)*100)/total_titulaciones
    cadena_grados="Porcentaje de grados: "+str(porcentaje_grados)+"\n"

    master=list(filter(lambda m: m.nivel.lower()=="máster",lista_grados))
    porcentaje_master=(len(master)*100)/total_titulaciones
    cadena_master="Porcentaje de master: "+str(porcentaje_master)+"\n"

    doctorado=list(filter(lambda d: d.nivel.lower()=="doctorado",lista_grados))
    porcentaje_doctorado=(len(doctorado)*100)/total_titulaciones
    cadena_doctorado="Porcentaje de doctorado: "+str(porcentaje_doctorado)+"\n"

    implantadas=list(filter(lambda i: int(i.anyo_inicio)==2009,lista_grados))
    cadena_implantadas="Grados implantados en 2009: "+str(len(implantadas))+"\n"

    etsii=list(filter(lambda e: e.escuela.lower()=="etsii",lista_grados))
    cadena_etsii="Grados de la ETSII: "+str(len(etsii))+"\n"

    porcentaje_etsii=(len(etsii)*100)/total_titulaciones
    cadena_porcentaje_etsii="Porcentaje de grados de la etsii respecto a la urjc: "+str(porcentaje_etsii)

    return cadenaTitulacion+cadena_grados+cadena_master+cadena_doctorado+cadena_implantadas+cadena_etsii+cadena_porcentaje_etsii
    

    


lista_grados=[]
leer_datos(lista_grados)
menu()


