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


camion1 =Camion("YRQ-466","Toyota",2018,"libre",1000,3)
camion2 =Camion("324566","Suzuki",2014,"libre",10000,3)
camion3 =Camion("529729","Nissan",2017,"libre",15000,3)
camion4 =Camion("EWD-788","Hyundai",2019,"libre",500,3)
camion5 =Camion("POO-456","Subaru",2011,"libre",3000,3)

lista_camiones = [camion1,camion2,camion3,camion4,camion5]

def pedido(camiones, cap_minima):
    if not isinstance(camiones,list):
        return "Error"
    for camion in camiones:
        if camion.estado_camion == "libre":
            if camion.cap_de_carga >=cap_minima:
                camion.mostrar()

#pedido(lista_camiones,9000)



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





top(lista_articulos)





















