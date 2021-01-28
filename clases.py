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

            if valores[5].lower()=='sí':
                igm=1
            elif valores[5].lower()=='no':
                igm=0

            if valores[6].lower()=='sí':
                igg=1
            elif valores[6].lower()=='no':
                igg=0
            #igg=valores[6]
            objeto_trabajador=Trabajador(nombre,apellido1,apellido2,edad,sexo,igm,igg)
            trabajadores.append(objeto_trabajador)

listaTrabajadores=[]
leer_datos(listaTrabajadores)
for i in listaTrabajadores:
    print(i)

# ggPositiva=list(filter(lambda v: int(v.igg)==1,listaTrabajadores))
# print(len(iggPositiva))
#for posi in iggPositiva:
#   print(posi)
#print("Igg positiva",len(iggPositiva))    