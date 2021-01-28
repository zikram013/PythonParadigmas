#1.Crear una clase alumno que tenga como datos el nombre y la nota. Definir metodos para iniciar los atributos, imprimirlos y decir si ha aprobado o no
class Alumno:
    nombre=None
    nota=None

    def __init__(self):
        self.nombre="Marcos"
        self.nota=10
    
    def imprimirDatos(self):
        print("El alumno se llama: ",self.nombre," y tiene de nota: ",self.nota)
    
    def aprobado(self):
        if self.nota<5:
            print("El alumno ",self.nombre," ha suspedido")
        else:
            print("El alumno ",self.nombre," ha aprobado")

alumno=Alumno()
alumno.imprimirDatos()
alumno.aprobado()

#2.Crear la clase persona con su nombre y su edad e indicar si es mayor de edad o no
class Persona:
    nombre=None
    edad=None

    def constructor(self,nombre,edad):
        self.nombre=nombre
        self.edad=edad
    
    def imprimirDatos(self):
        print("Me llamo: ",self.nombre,"y tengo ",self.edad)
    
    def mayoria(self):
        if self.edad<18:
            print("menor de edad")
        else:
            print("mayor de edad")

persona=Persona()
persona.constructor("Marcos",25)
persona.imprimirDatos()
persona.mayoria()

#3.Clase triangulo, imprimir el lado mayor y diga el tipo
class Triangulo:
    hipotenusa:None
    cateto1:None
    cateto2:None

    def __init__(self):
        self.hipotenusa=5
        self.cateto1=10
        self.cateto2=10
    
    def tipo(self):
        if(self.hipotenusa>self.cateto1)and(self.hipotenusa>self.cateto2):
            print("El lado mas grande es la hipotenusa ",self.hipotenusa)
            print("El triangulo es obtuso")
        elif(self.hipotenusa==self.cateto1==self.cateto2):
            print("Lados iguales, el triangulo es equilatero")
        else:
            print("El triangulo es isosceles")
            print(self.cateto1)

triangulo=Triangulo()
triangulo.tipo()

#4.Clase calculadora. Dos valores enteros con el init
class Calculadora:
    n1:None
    n2:None

    def __init__(self):
        self.n1=int(input())
        self.n2=int(input())

    def calcular(self):
        print("suma = ",self.n1+self.n2)
        print("resta = ",self.n1-self.n2)
        print("multiplicacion = ",self.n1*self.n2)
        print("division = ",self.n1/self.n2)

calculadora=Calculadora()
calculadora.calcular()

#5.clase agenda. Se debe mostrar un menu con las opciones de añadir,listar,buscar,editar y cerrar

class Agenda:

	def __init__(self):
		self.contactos=[]
 
	def menu(self):
		print()
		menu=[
			['Agenda Personal'],
			['1. Añadir Contacto',"anadir"],
			['2. Lista de contactos'],
			['3. Buscar contacto'],
			['4. Editar contacto'],
			['5. Cerrar agenda']
		]
 
		for x in range(6):
			print(menu[x][0])
 
		opcion=int(input("Introduzca la opción deseada: "))
		if opcion==1:
			self.anadir()
		elif opcion==2:
			self.lista()
		elif opcion==3:
			self.buscar()
		elif opcion==4:
			self.editar()
		elif opcion==5:
			print("Saliendo de la agenda ...")
			exit()
 

		self.menu()
 
	def anadir(self):
		print("---------------------")
		print("Añadir nuevo contacto")
		print("---------------------")
		nom=input("Introduzca el nombre: ")
		telf=int(input("Introduzca el teléfono: "))
		email=input("Introduzca el email: ")
		self.contactos.append({'nombre':nom,'telf':telf,'email':email})
		
 
	def lista(self):
		print("------------------")
		print("Lista de contactos")
		print("------------------")
		if len(self.contactos) == 0:
			print("No hay ningún contacto en la agenda")
		else:
			for x in range(len(self.contactos)):
				print(self.contactos[x]['nombre'])
		
    def buscar(self):
		print("---------------------")
		print("Buscador de contactos")
		print("---------------------")
		nom=input("Introduzca el nombre del contacto: ")
		for x in range(len(self.contactos)):
			if nom == self.contactos[x]['nombre']:
				print("Datos del contacto")
				print("Nombre: ",self.contactos[x]['nombre'])
				print("Teléfono: ",self.contactos[x]['telf'])
				print("E-mail: ",self.contactos[x]['email'])
				return x
		
 
 	def editar(self):
		print("---------------")
		print("Editar contacto")
		print("---------------")
		data=self.buscar()
		condition=False
		while condition==False:
			print("Selecciona que quieres editar: ")
			print("1. Nombre")
			print("2. Teléfono")
			print("3. E-mail")
			print("4. Volver")
			option=int(input("Introduzca la opción deseada: "))
			if option==1:
				nom=input("Introduzca el nuevo nombre: ")
				self.contactos[data]['nombre']=nom
			elif option==2:
				telf=input("Introduzca el nuevo teléfono: ")
				self.contactos[data]['telf']=telf
			elif option==3:
				email=input("Introduzca el nuevo email: ")
				self.contactos[data]['email']=email
			elif option==4:
				condition=True

agenda=Agenda()
agenda.menu()

#6.En un banco tienen clientes que pueden hacer depósitos y extracciones de
#dinero. El banco requiere también al final del día calcular la cantidad de dinero
#que se ha depositado. Se deberán crear dos clases, la clase cliente y la clase
#banco. La clase cliente tendrá los atributos nombre y cantidad y los métodos
#__init__, depositar, extraer, mostrar_total. La clase banco tendrá como atributos
#3 objetos de la clase cliente y los métodos __init__, operar y deposito_total. 
class Cliente:
    nombre:None
    cantidad:None

    def __init__(self,nombre,deposito):
        self.nombre=nombre
        self.cantidad=deposito
    
    def depositar(self,depositado):
        self.cantidad=self.cantidad+depositado

    def extraer(self,sacar):
        if sacar>self.cantidad:
            print("No tiene tanto dinero")
        else:
            self.cantidad=self.cantidad-sacar

    def mostrarTotal(self):
        print("Usted tiene: ",self.cantidad)
        return self.cantidad

class Banco:
    def __init__(self):
        self.cliente1=Cliente("marcos",1200)
        self.cliente2=Cliente("cami",8000)
        self.cliente3=Cliente("Nuse",3211)

    def operacion(self):
        self.cliente1.depositar(1000)
        self.cliente2.extraer(2333)
        self.cliente3.extraer(4000)

    def totalDepositos(self):
        total=self.cliente1.mostrarTotal()+self.cliente2.mostrarTotal()+self.cliente3.mostrarTotal()
        print(total)

banco=Banco()
banco.operacion()
banco.totalDepositos()

#7.Desarrollar un programa que conste de una clase padre Cuenta y dos subclases
#PlazoFijo y CajaAhorro. Definir los atributos titular y cantidad y un método para
#imprimir los datos en la clase Cuenta. La clase CajaAhorro tendrá un método para
#heredar los datos y uno para mostrar la información. La clase PlazoFijo tendrá
#dos atributos propios, plazo e interés. Tendrá un método para obtener el
#importe del interés (cantidad*interés/100) y otro método para mostrar la
#información, datos del titular plazo, interés y total de interés
class Cuenta:
    titular:None
    cantidad:None

    def __init__(self,titular,cantidad):
        self.titular=titular
        self.cantidad=cantidad
    
    def mostrarDatos(self):
        print("Titular: ",self.titular)
        print("Cantidad: ",self.cantidad)

class CajaAhorro(Cuenta):

    def __init__(self,titular,cantidad):
        super().__init__(titular,cantidad)
    
    def mostrar(self):
        super().mostrarDatos()

class PlazoFijo(Cuenta):

    def __init__(self,titular,cantidad,plazo,interes):
        super().__init__(titular,cantidad)
        self.plazo=plazo
        self.interes=interes
    
    def importeInteres(self):
        ganancia=self.cantidad*(self.interes/100)
        print("Ganancia: ",ganancia)
    
    def información(self):
        super().mostrarDatos()
        print("Interes: ",self.interes)
        print("Total: ",self.importeInteres())

caja=CajaAhorro("Marcos",5000)
caja.mostrar()

plazo=PlazoFijo("Marcos",8000,365,1.2)
plazo.información()