"""
Ejercicios clases python
"""
""""
3. Se va a definir un objeto empleado que tenga los siguientes datos: numero de_
empleado, nombre, salario por hora. El objeto va a contener los siguientes metodos:
mostrar () que despliega los datos de una instancia
calculosalario (horas) que recibe una cantidad de horas y muestra cual
deberia ser el salario.
*Implementar esta clase en Python.
*Defina una lista de instancias de la clase empleado. Escriba una funcion que
recorra esta lista y encuentro el empleado con salario mayor.
"""


class Empleado:
    def __init__(self, numero,nombre,salario):
        self.numero = numero
        self.nombre = nombre
        self.salario = salario
        self.deuda = 100000
    def mostrar(self):
        print("Número de empleado: " + str(self.numero),"Nombre del empleado: " + str(self.nombre),"Salario del empleado: " + str(self.salario))

    def calculo_salario(self,horas):
        print("Su salario corresponde a", self.salario*horas, "si trabaja", horas, "horas")

    def aumentar_deuda(self,monto):
        self.deuda += monto
        print("La deuda es de "+ str(self.deuda))

    def reducir_deuda(self,monto):
        self.deuda -= monto
        if self.deuda == 0:
            return "Felicidades, ya pagó su cuota"



empleado1 = Empleado(12,"Juan", 10000)
empleado2 = Empleado(343,"Esteban", 134000)
empleado3 = Empleado(1,"Ramiro", 1021000)
empleado4 = Empleado(1145,"Pedro", 12000)

#empleado1.aumentar_deuda(1000)
lista_empleados = [empleado1,empleado2,empleado3,empleado4]

def salario_mayor(empleados):
    if not isinstance(empleados, list):
        return "error"
    mayor = 0
    empleado_mayor = None
    for empleado in empleados:
        if mayor < empleado.salario:
            mayor = empleado.salario
            empleado_mayor = empleado
        else:
            pass
    print("El empleado con mayor salario corresponde a: ")
    return empleado_mayor.mostrar()

#salario_mayor(lista_empleados)



"""
3. Herencia. Se desea modelar un problema para manejar objetos con un nivel de
jerarquia. Se va a definir una clase padre llamada vehiculo que va a contener: placa
(string), marca, cantidad de ruedas, kilometraje y consumo por km. Esta clase padre
va a tener varios metodos: mostrar, hacerViaje(kms) que actualiza el kilometraje del
vehiculo.

A su vez se van a definir 2 subclases, la primera llamada auto, que ademas de los
atributos definidos en la clase vehiculo, tiene marca. modelo, combustible. Esta
clase va a tener un metodo mostrar. La segunda subclase se llama moto y va a tener
ademas de los atributos heredados los siguientes: estilo, cilindraje y va tener un
metodo mostrar.

Defina las clases Vehiculo, Auto y Moto.
ii.
Defina una lista de instancias de ambos vehiculos. Muestre los
datos de los vehiculos que tengan mas de 10,000 kms.

"""

class Vehiculo:
    def __init__(self,placa,marca,c_de_ruedas,k,cporkm):
        self.placa = placa
        self.marca = marca
        self.c_de_ruedas = c_de_ruedas
        self.k = k
        self.cporkm = cporkm

    def mostrar(self):
        print("El número de placa es: {} ".format(str(self.placa)))
        print("La marca del carro es: {} ".format(self.marca))
        print("La cantidad de ruedas corresponde a: {} ".format(self.c_de_ruedas))
        print("El kilometraje corresponde a: {} ".format(self.k))
        print("El consumo por km corresponde a: {} ".format(self.cporkm))

    def hacer_viaje(self,kms):
        self.k += kms
        print(self.k)
""""
#carro5 = Vehiculo("LOL-2354", "Mitsubishi montero", 4 , 500, 1230)
#carro5.mostrar()
#carro5.hacer_viaje(20)
"""


class Auto(Vehiculo):
    def __init__(self,placa,marca,c_de_ruedas,k,cporkm,modelo,combustible):
        super().__init__(placa,marca,c_de_ruedas,k,cporkm)
        self.modelo = modelo
        self.combustible = combustible

    def mostrar(self):
        print("Datos de la moto placa  " + str(self.placa))
        print("Marca: " + str(self.marca), "# de ruedas: " + str(self.c_de_ruedas), "kilometraje: " + str(self.k),"consumo por km: "+  str(self.cporkm), "modelo año: " + str(self.modelo), "tipo de combustible: " + str(self.combustible))

class Moto(Vehiculo):
    def __init__(self,placa,marca,c_de_ruedas,k,cporkm,estilo,cilindraje):
        super().__init__(placa,marca,c_de_ruedas,k,cporkm)
        self.estilo = estilo
        self.cilindraje = cilindraje

    def mostrar(self):
        print("Datos de la moto placa  " + str(self.placa))
        print("Marca: " + str(self.marca), "# de ruedas: " + str(self.c_de_ruedas), "kilometraje: " + str(self.k), "consumo por km: " +str(self.cporkm),"estilo: "+ str(self.estilo), "cilindraje: " + str(self.cilindraje))

carro1 = Auto("YRQ-444", "Mercedez Benz", 4 , 11000, 1000, "2010", "Regular")
carro2 = Auto("REF-233", "Toyota", 4 , 120000, 15000, "2010", "diessel")
carro3 = Auto("345678", "Subaru", 4 , 1000, 1030, "2010", "plus 91")
carro4 = Auto("LOL-2354", "Mitsubishi montero", 4 , 500, 1230, "2010", "diessel")

moto1 = Moto("ewr-566","Honda", 2,130000,140, "Chopper","100cc")
moto2 = Moto("rfi-321","Honda", 2,1300,100, "Pandillera","600cc")
moto3 = Moto("79292","Honda", 2,20000,20, "Chopper","400cc")
moto4 = Moto("455-rfe","Honda", 2,10000,30, "Pandillera","500cc")

lista_carros = [carro1,carro2,carro3,carro4,moto1,moto2,moto3,moto4]

def vehiculo_kms(vehiculos):
    if not isinstance(vehiculos,list):
        return "Error"

    for vehiculo in vehiculos:
        if vehiculo.k > 10000:

            vehiculo.mostrar()
#vehiculo_kms(lista_carros)



"""
Ejercicio 1 

Se desea construir un objeto tipo camion, conteniendo el numero de placa,
marca, año, estado camion (libre, ocupado, reparacion) capacidad de carga en
kg. y cantidad de viajes realizados. Los metodos a implementar son: mostrar (),
reset () que pone en cero la cantidad de viajes realizados, enviarReparacion ()
(actualiza el estado del camion a reparaciòn), recibir_reparacion (actualiza el estado decamion a libre)
 y actualiza Viajes (), que aumenta en 1 la cantidad de viajes
realizados.
a. Defina una clase Camion para el manejo de estos objetos, los cuales
pertenecen a una empresa de transportes. (Valor 15%)
b. Luego de tener definida la clase, se asume que se tiene la lista de
instancias y que se quiere construir una funcion llamada pedido, para saber cual o cuales camiones podran transportar una determinada
mercaderia. En este caso se recibirian como argumentos de la funcion: la
lista de instancias, la cantidad de kg a transportar y se deben mostrar los
camiones libres y con suficiente capacidad podrian cubrir
el pedido. (Valor 15%)
"""

class Camion:
    def __init__(self,placa,marca,anno,estado_camion,cap_de_carga,viajes_realizados):
        self.placa = placa
        self.marca = marca
        self.anno = anno
        self.estado_camion = estado_camion
        self.cap_de_carga = cap_de_carga
        self.viajes_realizados = viajes_realizados

    def mostrar(self):
        print("Placa:   {}".format(str(self.placa)))
        print("Marca:   {}".format(str(self.marca)))
        print("Año:   {}".format(str(self.anno)))
        print("Estado:   {}".format(str(self.estado_camion)))
        print("Capacidad de carga:   {}".format(str(self.cap_de_carga)))
        print("Viajes realizados:   {}".format(str(self.viajes_realizados)))

    def reset(self):
        self.viajes_realizados = 0

    def enviar_reparacion(self):
        self.estado_camion = "reparación"

    def recibir_reparacion(self):
        self.estado_camion = "libre"

    def actualiza_viajes(self):
        self.viajes_realizados +=1


camion1 =Camion("YRQ-466","Toyota",2018,"libre",1000,13)
camion2 =Camion("324566","Suzuki",2014,"libre",10000,6)
camion3 =Camion("529729","Nissan",2017,"libre",15000,12)
camion4 =Camion("EWD-788","Hyundai",2019,"libre",500,18)
camion5 =Camion("POO-456","Subaru",2011,"libre",3000,9)

lista_camiones = [camion1,camion2,camion3,camion4,camion5]

def pedido(camiones, cap_minima):
    if not isinstance(camiones,list):
        return "Error"
    for camion in camiones:
        if camion.estado_camion == "libre":
            if camion.cap_de_carga >=cap_minima:
                camion.mostrar()

#pedido(lista_camiones,9000)

def mayor(camiones):
    if not isinstance(camiones,list):
        return "ERROR"
    mayor = 0
    mayor_viajes = None
    for camion in camiones:
        if camion.viajes_realizados > mayor:
            mayor = camion.viajes_realizados
            mayor_viajes = camion

    print("El camión con más cantidad de viajes corresponde a:   ")
    return mayor_viajes.mostrar()

#mayor(lista_camiones)

"""

2. Un negocio vende CDs y DVDs. Cada uno de estos articulos tiene un tipo (CD o
DVD), titulo, precio, duracion en minutos, autor y ventas en unidades (inicia en cero
cuando se crea una instancia). Se desea construir un objeto Articulo con los datos
indicados. Los metodos a implementar son: mostrar, que muestra todos los datos
de un articulo, venta que recibe una cantidad y actualiza (suma) las ventas del

articulo, devolucion que recibe una cantidad y actualiza (resta) las ventas del
articulo.
a. Defina una clase Articulo para el manejo de estos objetos. (35 pts)
b. Luego de tener definida la clase, se asume que se tiene una lista de instancias

y que se quiere construir una funcion llamada top, para saber cual es el DVD
que registra mas ventas y cual es el DVD que registra mas devoluciones. En
este caso se recibiria como argumento de la funcion la lista de instancias. (30
pts)

"""
class Articulo:
    def __init__(self,tipo,titulo,precio,duracion,autor,cantidad_de_ventas):
        self.tipo = tipo
        self.titulo = titulo
        self.precio = precio
        self.duracion = duracion
        self.autor = autor
        self.cantidad_de_ventas = cantidad_de_ventas

    def mostrar(self):
        print("Tipo:   {}".format(str(self.tipo)))
        print("Tìtulo:   {}".format(str(self.titulo)))
        print("Precio:   {}".format(str(self.precio)))
        print("Duración:   {}".format(str(self.duracion)))
        print("Autor:   {}".format(str(self.autor)))
        print("Cantidad de ventas:   {}".format(str(self.cantidad_de_ventas)))

    def venta(self,cantidad):
        self.cantidad_de_ventas += cantidad
        return self.cantidad_de_ventas
    def devolucion(self,cantidad):
        self.cantidad_de_ventas -= cantidad
        return self.cantidad_de_ventas


articulo1 = Articulo("DVD", "How deep is your love", 10000, 30, "Beegees",0)
articulo1.venta(34)
articulo1.devolucion(21)

articulo2 = Articulo("DVD", "November Rain", 15000, 30, "Lez Zeppelin",0)
articulo2.venta(54)
articulo2.devolucion(34)

articulo3 = Articulo("DVD", "Dancing Queen", 1300, 30, "ABBA",0)
articulo3.venta(21)
articulo3.devolucion(12)

articulo4 = Articulo("DVD", "Imagine", 5000, 30, "John Lennon",0)
articulo4.venta(30)
articulo4.devolucion(1)


lista_articulos = [articulo1,articulo2,articulo3,articulo4]


def top(articulos):
    global devolucion
    if not isinstance(articulos,list):
        return "ERROR"
    mayor = 0

    venta_mayor = None
    for articulo in articulos:


       if articulo.tipo == "DVD":
            if mayor < articulo.cantidad_de_ventas:
                mayor = articulo.cantidad_de_ventas
                venta_mayor = articulo

    menor = venta_mayor.cantidad_de_ventas
    devolucion = None
    for articulo in articulos:
        if articulo.tipo == "DVD":
            if mayor < articulo.cantidad_de_ventas:
                pass
            else:
                mayor = articulo.cantidad_de_ventas
                devolucion = articulo
    print("El disco con más ventas corresponde a:  "),  str(venta_mayor.mostrar())
    print("El disco con más devoluciones corresponde a:  "),str(devolucion.mostrar())





#top(lista_articulos)


"""
A continuacion se presenta una serie de ejercicios que debe desarrollado forma clara,
ordenada y legible. Cualquier intento de fraude sera tratado de acuerdo al reglamento que
para tal proposito ha dispuesto el Instituto Tecnologico de Costa Rica. Adicionalmente.
durante el desarrollo de la prueba no se permite el uso de dispositivos electronicos, fuera de
los estrictamente necesarios para la realizacion de la misma. Dispone de dos horas y treinta
minutos para realizar la prueba.

La prueba debe ser desarrollado a mano, luego escaneada y convertida a un archivo PDF.
La entrega se debe realizar en la seccion de Evaluationes del TEC Digital. Finalmente,
dispone de 24 horas para copiar su examen en un archivo de Python y subir el .py al TEC
Digital
Si tuviera problemas de infraestructura durante el desarrollo de la prueba, debe comunicarlo
al profesor al correo learaya@itcr.ac.cr o al telefono 89699250 para buscar una solucion.

1. Se desea construir un objeto tipo Uber con los siguientes atributos
. Numero de placa
. Marca
. Ano
. Estado del vehiculo (libre, ocupado, reparacion)

. Tipo de vehiculo (economico, premium)
. Cantidad de viajes realizados
. Monto de viaje (el actual)
. Acumulado de monto por viajes
Calificacion (de 0 a 5 estrellas). Inicialmente, los conductores empiezan con 5
estrellas

Los metodos a implementar son:
. mostrar(), que imprime todos los atributos del objeto
. reset (), que pone en cero la cantidad de viajes realizados

. enviar reparacion(), que actualiza el estado del camion a reparacion
. recibir reparation (), que actualiza el estado del camion a libre
viaje(kilometros), que aumenta en 1 la cantidad de viajes realizados y calcula

l monto a pagar por el viaje, de acuerdo a la cantidad de kilometros de viaje.
Considere que los viajes economicos se pagan a 300 por kilometro y los premium
a 500 por kilometro
set_calificacion(calificacion), que calcula el promedio de estrellas que tiene el
objeto basado en la calificacion actual y la nueva calificacion recibida.
. Ademas, debe existir los metodos get_tipo(), get estado() y get_viajes() que retor-
nan los datos correspondientes
Utilizando el lenguaje de programacion Python, se le solicita lo siguiente:

(a) Defina una clase Uber para el manejo de este objeto. 40 puntos.
(b) Luego de tener definida la clase, se asume que se tiene la lista de instancias y que se
quiere construir una funcion llamada solicita(lista, tipo, calificacion minima), que
recibe esa lista de instancias para saber cuales vehiculos podran transportar un cliente
segun un tipo de vehiculo y la calificacion minima solicitada por el cliente. 30 puntos.

"""

class Uber:
    def __init__(self, placa,marca,anno,e_v,t_v,cdvr,m_d_v,acum_monto_de_viajes,calificacion):
        self.placa = placa
        self.marca = marca
        self.anno = anno
        self.estado_vehiculo = e_v
        self.tipo_vehiculo = t_v
        self.cantidad_viajes_realizados = cdvr
        self.monto_del_viaje = m_d_v
        self.acumulado = acum_monto_de_viajes
        self.calificacion = calificacion

    def mostrar(self):
        print("El número de placa es:  {}".format(str(self.placa)))
        print("La marca del vehículo es:  {}".format(str(self.marca)))
        print("El año del vehículo:  {}".format(str(self.anno)))
        print("El estado del vehículo es:  {}".format(str(self.estado_vehiculo)))
        print("El tipo de vehículo es:  {}".format(str(self.tipo_vehiculo)))
        print("La cantidad de viajes realizados es:  {}".format(str(self.cantidad_viajes_realizados)))
        print("El monto del viaje es:  {}".format(str(self.monto_del_viaje)))
        print("El acumulado del viaje es:  {}".format(str(self.acumulado)))
        print("La calificación del vehículo es:  {}".format(str(self.calificacion)))

    def reset(self):
        self.cantidad_viajes_realizados = 0

    def enviar_reparación(self):
        self.estado_vehiculo = "reparacion"

    def recibir_reparacion(self):
        self.estado_vehiculo = "libre"

    def viaje(self,kilometros):
        self.cantidad_viajes_realizados += 1
        if self.tipo_vehiculo == "economico":
            self.monto_del_viaje += 300 * kilometros
        else:
            self.monto_del_viaje += 500 * kilometros

    def set_calificacion(self,calificacion):
        nueva_calificacion = ((self.calificacion * self.cantidad_viajes_realizados + calificacion))/(self.cantidad_viajes_realizados+1)
        return nueva_calificacion


        print("La calificación de estrellas corresponde a ", self.calificacion)
    def get_tipo(self):
        return self.tipo_vehiculo
    def get_estado(self):
        return self.estado_vehiculo
    def get_viajes(self):
        return self.cantidad_viajes_realizados


carro1 = Uber("TRE-111","Toyota", 2009, "libre","economico", 4, 1200,5500,5)
carro2 = Uber("529874","Mitsubishi", 2019, "libre","economico", 5, 1200,5300,5)
carro3 = Uber("423434","Stepway", 2014, "libre","economico", 7, 2200,14600,5)
carro4 = Uber("ERW-EW1","Suzuki", 2004, "libre","economico", 12, 1230,14000,5)
carro5 = Uber("RET-567","Nissan", 2012, "libre","economico", 4, 1180,3600,5)
#print(carro1.set_calificacion(4))

lista_carros = [carro1,carro2,carro3,carro4,carro5]

def solicita(carros,tipo,calif_minima):
    for carro in carros:
        if carro.tipo_vehiculo == tipo and carro.calificacion >= calif_minima:
            print("El carro placa {} puede dar el servicio".format(carro.placa))

#solicita(lista_carros,"economico",3)

"""
. Para representar los datos de un estudiante del TEC, se va a manejar un objeto
Estudiante que permite almacenar: nombre, carnet, lista de cursos (va a iniciar en nulo
al crear una instancia). La lista de cursos va a ser una lista de listas, donde cada curso
se representa por un codigo de curso, semestre, ano y nota. Un ejemplo de un curso

seria [1101, 1, 2014, 60], que indicaria que el curso 1101 fue llevado por el estudiante
en el semestre 1 del ano 2014 y obtuvo una nota de 60. Los metodos serian:
get_carnet(): retorna el carnet del estudiante
get_nombre(): retorna el nombre del estudiante
get _cursos(): retorna la lista de cursos del estudiante

agregar_curso(codigo, semestre, ano, nota): verifica si el curso no existe en el
semestre y ano dados, en este caso lo incluye en la lista. En caso que el curso ya este

registrado, se debe mostrar un mensaje de error.
mostrar(): muestra el carnet, nombre y para cada curso: el codigo, semestre, ano y

nota obtenida por el estudiante

a. Defina una clase en Python para manejar el objeto Estudiante. (35 pts).
b. b. Asuma que se tiene una lista de instancias del objeto Estudiante. Defina

una funcion llamada promedio (carnet, lista) , que reciba un carnet,
a lista de instancias del objeto Estudiante y muestre los datos del estudiante,
asi como el promedio de notas. Si el carnet no existe, debe indicarse por
medio de otro mensaje. (30 pts)

"""


class Estudiante:
    def __init__(self,nombre,carnet,lista_de_cursos):
        self.nombre = nombre
        self.carnet = carnet
        self.lista_de_cursos = lista_de_cursos

    def get_carnet(self):
        return self.carnet
    def get_nombre(self):
        return self.nombre
    def get_cursos(self):
        return self.lista_de_cursos

    #def agregar_curso(self,codigo,semestre,año,nota):
     #   for i in self.lista_de_cursos:
    def agregar_curso(self,codigo,semestre,año,nota):
        for i in self.lista_de_cursos:
            if i[0] == codigo and i[1] == semestre and i[2] == año:
                return "El curso ya está registrado"

        self.lista_de_cursos += [[codigo,semestre,año,nota]]
        return self.lista_de_cursos


    def mostrar(self):
        print("El carnet del estudiante es:  {}".format(self.carnet))
        print("El nombre del estudiante es:  {}".format(self.nombre))
        for cursos in self.lista_de_cursos:
            print("El código del curso corresponde a:  {}".format(cursos[0]))
            print("El semestre en que se llevó el curso corresponde a:   {}".format(cursos[1]))
            print("El año en el que se llevó el curso corresponde a:  {}".format(cursos[2]))
            print("La nota que obtuvo el estudiante en el curso corresponde a:   {}".format(cursos[3]))
estudiante1 = Estudiante("José Andrés","2021453583", [["1130",1,2016,60],["1202",2,2014,70]])
estudiante4 = Estudiante("Fernanda", "2021342312", [["1091",1,2010,60],["2012",2,2009,70],["2122",2,2014,80]])
estudiante5 = Estudiante("Manuela", "2014097637", [["1101",1,2014,40],["1102",2,2018,50],["1230",2,2020,100]])
#estudiante4.mostrar())
lista = [estudiante1,estudiante4,estudiante5]
def promedio(carnet,lista):
    suma_notas = 0
    contador = 0
    for i in lista:
        if i.carnet == carnet :

            for j in i.lista_de_cursos :
                suma_notas += j[3]
                contador +=1
            promedio_final = suma_notas/contador
            i.mostrar()
            print("El promedio del estudiante con el carnet {} corresponde a".format(carnet))

            return promedio_final
        else:
            return "El carnet {} no existe".format(carnet)



#print(promedio("2021453583", lista))
    """"
class Nodo:
    def __init__(self,next = None, valor = None):
        self.next = next
        self.valor = valor
        
class Lista:
    def __init__(self):
        
        self.head = []
        self.largo = 0

    def crear_lista(self):
        

    def borrar(self,item):
        for i in


    """

class Animal:
    def __init__(self,pesokg,tamano,color,edad):
        self.pesokg = pesokg
        self.tamano = tamano
        self.color = color
        self.edad = edad

    def movimiento(self,tipo):
        if tipo == 1:
            print("La velocidad del animal es andando")
        elif tipo == 2:
            print("La velocidad del animal es corriendo")
        elif tipo == 3:
            print("La velocidad del animal es detenido")

    def comer(self):
        print("El animal está comiendo")

class Elefante(Animal):
    def __init__(self,pesokg,tamano,color,edad,trompa,colmillos):
        super().__init__(pesokg,tamano,color,edad)
        self.trompa = trompa
        self.colmillos = colmillos

    def jugarTrompa(self):
        print("El elefante está jugando con su trompa")
    def comer(self):
        print("El elefante está inhalando maní")



animal1 = Animal(200,"grande","blanco",10)
animal2 = Animal(400,"mediano","negro",20)
animal3 = Animal(500,"grande","rojo",5)
animal4 = Animal(100,"pequeño","verde",15)
animal5 = Animal(200,"pequeño","azul",12)

elefante1 = Elefante(300,"grande","gris",14,"corta","largos")
elefante2 = Elefante(100,"pequeño","blanco",13,"mediana","cortos")
elefante3 = Elefante(200,"mediano","negro",9,"larga","medianos")
elefante4 = Elefante(500,"grande","gris",4,"corta","cortos")

def func(obj):
    obj.comer()

obj_an = animal1
obj_elef = elefante1

#func(obj_an)
#func(obj_elef)

#elefante3.jugarTrompa()


from __future__ import print_function


class Node:  # create a Node
    def __int__(self, data):
        self.data = data  # given data
        self.next = None  # given next to None


class Linked_List:
    def insert_tail(Head, data):
        if Head.next is None:
            Head.next = Node(data)
        else:
            Head.next.insert_tail(data)

    def insert_head(Head, data):
        tamp = Head
        if tamp is None:
            newNod = Node()  # create a new Node
            newNod.data = data
            newNod.next = None
            Head = newNod  # make new node to Head
        else:
            newNod = Node()
            newNod.data = data
            newNod.next = Head  # put the Head at NewNode Next
            Head = newNod  # make a NewNode to Head
        return Head

    def printList(Head):  # print every node data
        tamp = Head
        while tamp is not None:
            print(tamp.data)
            tamp = tamp.next

    def delete_head(Head):  # delete from head
        if Head is not None:
            Head = Head.next
        return Head  # return new Head

    def delete_tail(Head):  # delete from tail
        if Head is not None:
            tamp = Node()
            tamp = Head
            while tamp.next.next is not None:  # find the 2nd last element
                tamp = tamp.next
            # delete the last element by give next None to 2nd last Element
            tamp.next = None
        return Head

    def isEmpty(Head):
        return Head is None  # Return if Head is none

    def reverse(Head):
        prev = None
        current = Head

        while current:
            # Store the current node's next node.
            next_node = current.next
            # Make the current node's next point backwards
            current.next = prev
            # Make the previous node be the current node
            prev = current
            # Make the current node the next node (to progress iteration)
            current = next_node
        # Return prev in order to put the head at the end
        Head = prev