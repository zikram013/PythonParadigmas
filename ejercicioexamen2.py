#Cargar datos de fichero de todos los tenistas hecho
#Cargar datos de fichero de todos los equipos y sus jugadores hecho
#Cargar datos de encuentros
class Pais:
    listadoJugadores=[]
    def __init__(self,nombrePais,listadoJugadores=[]):
        self.nombrePais=nombrePais
        self.listadoJugadores=listadoJugadores

    def __str__(self):  
        cadena=self.nombrePais
        for ele in self.listadoJugadores:
            tenista=Jugadores(ele.nombre,ele.apellido1,ele.edad,ele.mano)
            cadena=cadena+" "+tenista.__str__()
        return cadena


class Jugadores:
    def __init__(self,nombre,apellido1,edad,mano):
        self.nombre=nombre
        self.apellido1=apellido1
        self.edad=edad
        self.mano=mano  

    def __str__(self):
        return self.nombre+" "+self.apellido1+" "+str(self.edad)+" "+self.mano 
 

class Partido:
    def __init__(self,grupo,equipoA,puntosA,equipoB,puntosB):
        self.grupo=grupo
        self.equipoA=equipoA
        self.puntosA=puntosA
        self.equipoB=equipoB
        self.puntosB=puntosB

    def __str__(self):
        return self.grupo+" "+self.equipoA+" "+self.puntosA+" "+self.equipoB+" "+self.puntosB

def leer_datos(listaPaises,listaJugadoresPorPais,listaJugadoresTotal):
    
    with open("datos.txt","r",encoding="UTF-8")as fichero:
        for linea in fichero.readlines():
            valores=linea.split(" ")
            pais=valores[0]
            for i in range(1,20,4):
                contador=i
                nombre=valores[contador]
                apellido1=valores[contador+1]
                edad=valores[contador+2]
                mano=valores[contador+3]
                objetoJugador=Jugadores(nombre,apellido1,edad,mano)
                listaJugadoresTotal.append(objetoJugador)
                listaJugadoresPorPais.append(objetoJugador)

            objetoPais=Pais(pais,listadoJugadores=listaJugadoresPorPais)
            listaPaises.append(objetoPais)
            listaJugadoresPorPais=[]
        fichero.close()

def leer_datos_partidos(listaEncuentros):
    with open("resultados.txt","r",encoding="UTF-8")as fichero:
        for linea in fichero.readlines():
            valores=linea.split(" ")
            grupo=valores[0]
            equipoA=valores[1]
            puntosA=valores[2]
            equipoB=valores[3]
            puntosB=valores[4]
            objetoResultado=Partido(grupo,equipoA,puntosA,equipoB,puntosB)
            listaEncuentros.append(objetoResultado)





listaJugadoresTotal=[]
listaJugadoresPorPais=[]
listaPaises=[]
listaEncuentros=[]
leer_datos(listaPaises,listaJugadoresPorPais,listaJugadoresTotal)
leer_datos_partidos(listaEncuentros)


#Clasificacion
listaPartidosA=[]
listaPartidosB=[]
listaPartidosC=[]
listaPartidosD=[]
listaPartidosE=[]
listaPartidosF=[]
for ele in listaEncuentros:
    if ele.grupo.lower()=="a":
        listaPartidosA.append(ele)
    if ele.grupo.lower()=="b":
        listaPartidosB.append(ele)
    if ele.grupo.lower()=="c":
        listaPartidosC.append(ele)
    if ele.grupo.lower()=="d":
        listaPartidosD.append(ele)
    if ele.grupo.lower()=="e":
        listaPartidosE.append(ele)
    if ele.grupo.lower()=="f":
        listaPartidosF.append(ele)

clasiA=[]
clasiB=[]
clasiC=[]
clasiD=[]
clasiE=[]
clasiF=[]

#Grupo A
for i in listaPartidosA:
    estaA=True
    estaB=True
    if len(clasiA)==0:
            clasiA.append({'equipo':i.equipoB,'jugados':0,'ganados':0,'perdidos':0})
           
    else:
        for dataA in clasiA:
            if dataA['equipo']!=i.equipoA:
                estaA=False
                break
            elif dataA['equipo']!=i.equipoB:
                estaB=False
                break

        if estaA==False:
            clasiA.append({'equipo':i.equipoA,'jugados':0,'ganados':0,'perdidos':0})
        elif estaB==False:
            clasiA.append({'equipo':i.equipoB,'jugados':0,'ganados':0,'perdidos':0})
 

for iss in listaPartidosA:
    if iss.puntosA > iss.puntosB:
        for datA in clasiA:
            if datA['equipo']==iss.equipoA:
                datA['jugados']=datA['jugados']+1
                datA['ganados']=datA['ganados']+1
            if datA['equipo']==iss.equipoB:
                datA['jugados']=datA['jugados']+1
                datA['perdidos']=datA['perdidos']+1
    elif iss.puntosB > iss.puntosA:
        for datA in clasiA:
            if datA['equipo']==iss.equipoB:
                datA['jugados']=datA['jugados']+1
                datA['ganados']=datA['ganados']+1
            if datA['equipo']==iss.equipoA:
                datA['jugados']=datA['jugados']+1
                datA['perdidos']=datA['perdidos']+1
clasiA.sort(key=lambda p:p['perdidos'])
#GrupoB
for i in listaPartidosB:
    estaA=True
    estaB=True
    if len(clasiB)==0:
            clasiB.append({'equipo':i.equipoB,'jugados':0,'ganados':0,'perdidos':0})
           
    else:
        for dataA in clasiB:
            if dataA['equipo']!=i.equipoA:
                estaA=False
                break
            elif dataA['equipo']!=i.equipoB:
                estaB=False
                break

        if estaA==False:
            clasiB.append({'equipo':i.equipoA,'jugados':0,'ganados':0,'perdidos':0})
        elif estaB==False:
            clasiB.append({'equipo':i.equipoB,'jugados':0,'ganados':0,'perdidos':0})
 

for iss in listaPartidosB:
    if iss.puntosA > iss.puntosB:
        for datA in clasiB:
            if datA['equipo']==iss.equipoA:
                datA['jugados']=datA['jugados']+1
                datA['ganados']=datA['ganados']+1
            if datA['equipo']==iss.equipoB:
                datA['jugados']=datA['jugados']+1
                datA['perdidos']=datA['perdidos']+1
    elif iss.puntosB > iss.puntosA:
        for datA in clasiB:
            if datA['equipo']==iss.equipoB:
                datA['jugados']=datA['jugados']+1
                datA['ganados']=datA['ganados']+1
            if datA['equipo']==iss.equipoA:
                datA['jugados']=datA['jugados']+1
                datA['perdidos']=datA['perdidos']+1
clasiB.sort(key=lambda p:p['perdidos'])
#GrupoC
for i in listaPartidosC:
    estaA=True
    estaB=True
    if len(clasiC)==0:
            clasiC.append({'equipo':i.equipoB,'jugados':0,'ganados':0,'perdidos':0})
           
    else:
        for dataA in clasiC:
            if dataA['equipo']!=i.equipoA:
                estaA=False
                break
            elif dataA['equipo']!=i.equipoB:
                estaB=False
                break

        if estaA==False:
            clasiC.append({'equipo':i.equipoA,'jugados':0,'ganados':0,'perdidos':0})
        elif estaB==False:
            clasiC.append({'equipo':i.equipoB,'jugados':0,'ganados':0,'perdidos':0})
 

for iss in listaPartidosC:
    if iss.puntosA > iss.puntosB:
        for datA in clasiC:
            if datA['equipo']==iss.equipoA:
                datA['jugados']=datA['jugados']+1
                datA['ganados']=datA['ganados']+1
            if datA['equipo']==iss.equipoB:
                datA['jugados']=datA['jugados']+1
                datA['perdidos']=datA['perdidos']+1
    elif iss.puntosB > iss.puntosA:
        for datA in clasiC:
            if datA['equipo']==iss.equipoB:
                datA['jugados']=datA['jugados']+1
                datA['ganados']=datA['ganados']+1
            if datA['equipo']==iss.equipoA:
                datA['jugados']=datA['jugados']+1
                datA['perdidos']=datA['perdidos']+1
clasiC.sort(key=lambda p:p['perdidos'])

#GrupoD
for i in listaPartidosD:
    estaA=True
    estaB=True
    if len(clasiD)==0:
            clasiD.append({'equipo':i.equipoB,'jugados':0,'ganados':0,'perdidos':0})
           
    else:
        for dataA in clasiD:
            if dataA['equipo']!=i.equipoA:
                estaA=False
                break
            elif dataA['equipo']!=i.equipoB:
                estaB=False
                break

        if estaA==False:
            clasiD.append({'equipo':i.equipoA,'jugados':0,'ganados':0,'perdidos':0})
        elif estaB==False:
            clasiD.append({'equipo':i.equipoB,'jugados':0,'ganados':0,'perdidos':0})
 

for iss in listaPartidosD:
    if iss.puntosA > iss.puntosB:
        for datA in clasiD:
            if datA['equipo']==iss.equipoA:
                datA['jugados']=datA['jugados']+1
                datA['ganados']=datA['ganados']+1
            if datA['equipo']==iss.equipoB:
                datA['jugados']=datA['jugados']+1
                datA['perdidos']=datA['perdidos']+1
    elif iss.puntosB > iss.puntosA:
        for datA in clasiD:
            if datA['equipo']==iss.equipoB:
                datA['jugados']=datA['jugados']+1
                datA['ganados']=datA['ganados']+1
            if datA['equipo']==iss.equipoA:
                datA['jugados']=datA['jugados']+1
                datA['perdidos']=datA['perdidos']+1
clasiD.sort(key=lambda p:p['perdidos'])

#GrupoE
for i in listaPartidosE:
    estaA=True
    estaB=True
    if len(clasiE)==0:
            clasiE.append({'equipo':i.equipoB,'jugados':0,'ganados':0,'perdidos':0})
           
    else:
        for dataA in clasiE:
            if dataA['equipo']!=i.equipoA:
                estaA=False
                break
            elif dataA['equipo']!=i.equipoB:
                estaB=False
                break

        if estaA==False:
            clasiE.append({'equipo':i.equipoA,'jugados':0,'ganados':0,'perdidos':0})
        elif estaB==False:
            clasiE.append({'equipo':i.equipoB,'jugados':0,'ganados':0,'perdidos':0})
 

for iss in listaPartidosE:
    if iss.puntosA > iss.puntosB:
        for datA in clasiE:
            if datA['equipo']==iss.equipoA:
                datA['jugados']=datA['jugados']+1
                datA['ganados']=datA['ganados']+1
            if datA['equipo']==iss.equipoB:
                datA['jugados']=datA['jugados']+1
                datA['perdidos']=datA['perdidos']+1
    elif iss.puntosB > iss.puntosA:
        for datA in clasiE:
            if datA['equipo']==iss.equipoB:
                datA['jugados']=datA['jugados']+1
                datA['ganados']=datA['ganados']+1
            if datA['equipo']==iss.equipoA:
                datA['jugados']=datA['jugados']+1
                datA['perdidos']=datA['perdidos']+1
clasiE.sort(key=lambda p:p['perdidos'])

#GrupoF
for i in listaPartidosF:
    estaA=True
    estaB=True
    if len(clasiF)==0:
            clasiF.append({'equipo':i.equipoB,'jugados':0,'ganados':0,'perdidos':0})
            #clasiF.append({'equipo':i.equipoB,'jugados':0,'ganados':0,'perdidos':0})
    else:
        for dataA in clasiF:
            if dataA['equipo']!=i.equipoA:
                #print(i.equipoA)
                estaA=False
                break
            elif dataA['equipo']!=i.equipoB:
                #print(i.equipoB)
                estaB=False
                break

        if estaA==False:
            clasiF.append({'equipo':i.equipoA,'jugados':0,'ganados':0,'perdidos':0})
        elif estaB==False:
            clasiF.append({'equipo':i.equipoB,'jugados':0,'ganados':0,'perdidos':0})

for iss in listaPartidosF:
    if iss.puntosA > iss.puntosB:
        for datA in clasiF:
            if datA['equipo']==iss.equipoA:
                datA['jugados']=datA['jugados']+1
                datA['ganados']=datA['ganados']+1
            if datA['equipo']==iss.equipoB:
                datA['jugados']=datA['jugados']+1
                datA['perdidos']=datA['perdidos']+1
    elif iss.puntosB > iss.puntosA:
        for datA in clasiF:
            if datA['equipo']==iss.equipoB:
                datA['jugados']=datA['jugados']+1
                datA['ganados']=datA['ganados']+1
            if datA['equipo']==iss.equipoA:
                datA['jugados']=datA['jugados']+1
                datA['perdidos']=datA['perdidos']+1
clasiF.sort(key=lambda p:p['perdidos'])

#Cuartos de final
def cuartosDeFinal(clasiA,clasiB,clasiC,clasiD,clasiE,clasiF):
    print("1º cuartos de final :",clasiA[0].get("equipo")," contra ",clasiB[1].get("equipo"))
    print("2º cuartos de final :",clasiD[0].get("equipo")," contra ",clasiF[0].get("equipo"))
    print("3º cuartos de final :",clasiE[0].get("equipo")," contra ",clasiC[0].get("equipo"))
    print("4º cuartos de final :",clasiC[1].get("equipo")," contra ",clasiB[0].get("equipo"))

#Añadir a la tabla de clasificion balance ganados perdidos
def ayadir(clasi):
    vic=0
    der=0
    for i in listaPartidosF:
        if i.puntosA > i.puntosB:
            if i.equipoA==clasi['equipo']:
                vic=vic+int(i.puntosA)
                der=der+int(i.puntosB)
            if i.equipoB==clasi['equipo']:
                vic=vic+int(i.puntosB)
                der=der+int(i.puntosA)
        elif i.puntosB>i.puntosA:
            if i.equipoA==clasi['equipo']:
                der=der+int(i.puntosB)
                vic=vic+int(i.puntosA)
            if i.equipoB==clasi['equipo']:
                vic=vic+int(i.puntosB)
                der=der+int(i.puntosA)

    bal=str(vic)+"-"+str(der)

    clasi['balance']=bal
    return clasi

clasiF=map(ayadir,clasiF)
for cl in clasiF:
    print(cl)
    

##Estadisticas
def jugadoresConMenosDe20(listaJugadoresTotal):
    jugadoresMenoresDe20=list(filter(lambda v: int(v.edad)<20,listaJugadoresTotal))
    print("Menores de 20: ",len(jugadoresMenoresDe20))
    return jugadoresMenoresDe20


def jugadoresEntre20y30(listaJugadoresTotal):
    jugadoresEntre20y30=list(filter(lambda v:int(v.edad)>=20 and int(v.edad)<=30,listaJugadoresTotal))
    print("Entre 20 y 30: ",len(jugadoresEntre20y30))

def jugadoresConMasDe30(listaJugadoresTotal):
    jugadoresMayoresDe30=list(filter(lambda v: int(v.edad)>30,listaJugadoresTotal))
    print("Mayores de 30: ",len(jugadoresMayoresDe30))

    for player30 in jugadoresMayoresDe30:
        print(player30.nombre+" "+player30.apellido1)

def paisesConJugadoresMenoresDe20Años():
    for player20 in jugadoresConMenosDe20(listaJugadoresTotal):
        for pais in listaPaises:
            for player20pais in pais.listadoJugadores:
                if (player20.nombre == player20pais.nombre) and (player20.apellido1==player20pais.apellido1):
                    print(pais.nombrePais)



