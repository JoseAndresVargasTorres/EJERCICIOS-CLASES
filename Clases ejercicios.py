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

empleado1.aumentar_deuda(1000)
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

salario_mayor(lista_empleados)



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
        print("El número de placa es: ".format(self.placa))
        print("La marca del carro es: ".format(self.marca))
        print("La cantidad de ruedas corresponde a: ".format(self.c_de_ruedas))
        print("El kilometraje corresponde a: ".format(self.k))
        print("El consumo por km corresponde a: ".format(self.cporkm))

    def hacer_viaje(self,kms):
        self.k += kms

vehiculo1 = Vehiculo("YRQ-466","Toyota",4,1000,)

class Auto(Vehiculo):
    def __init__(self,placa,marca,c_de_ruedas,k,cporkm,modelo,combustible):
        super(Auto, self).__init__(placa,marca,c_de_ruedas,k,cporkm)
        self.modelo = modelo
        self.combustible = combustible

    def mostrar(self):
        print("Datos del auto" + str(self.placa))
        print(self.marca,self.c_de_ruedas,self.k,self.k,self.cporkm,self.modelo,self.combustible)

class Moto(Vehiculo):
    def __init__(self,placa,marca,c_de_ruedas,k,cporkm,estilo,cilindraje):
        super().__init__(placa,marca,c_de_ruedas,k,cporkm)
        self.estilo = estilo
        self.cilindraje = cilindraje





