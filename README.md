Ejercicio 1 

Se desea construir un objeto tipo camion, conteniendo el numero de placa,
marca, ano, estado camion (libre, ocupado, reparacion) capacidad de carga en
kg. y cantidad de viajes realizados. Los metodos a implementar son: mostrar (),
reset () que pone en cero la cantidad de viajes realizados, enviarReparacion ()
(actualiza el estado del camion), recibir de reparacion (actualiza el estado decamion) y actualiza Viajes (), que aumenta en 1 la cantidad de viajes
realizados.
a. Defina una clase Camion para el manejo de estos objetos, los cuales
pertenecen a una empresa de transportes. (Valor 15%)
b. Luego de tener definida la clase, se asume que se tiene la lista de
instancias y que se quiere construir una funcion llamada pedido, para saber cual o cuales camiones podran transportar una determinada
mercaderia. En este caso se recibirian como argumentos de la funcion: la
lista de instancias, la cantidad de kg a transportar y se deben mostrar los
le cuales camiones libres y con suficiente capacidad podrian cubrir
el pedido. (Valor 15%)


Ejercicio 2
3. Se desea desarrollado clase animal, la cual debe de contar con la siguiente atributos:

peso (kg), tamano, color, edad (meses). Ademas debera de contar como minimo con los
siguientes metodos: movimiento (velocidad andando=1, corriendo=2, detenido=3),comer .

Desarrolle tambien la clase elefante que hereda de la clase animal y que debera de
contar con los siguientes atributos adicionales: trompa(corta, mediana, larga),
colmillos (cortos, medianos, largos)

Esta clase elefante debera de implementar los siguientes metodos:
jugarTrompa
- comer (este metodo implementando polimorfismo al metodo original comer, para
que el elefante que inhale mani).
Para ello debera de realizar lo siguiente:

a. Desarrollo el Diagrama de Clases que describa lo solicitado en este item (Valor
15%).
. Defina el codigo que implemente lo solicitado en este item (Valor 15%)
c. Recuerde que en el envio del codigo se debe de desarrollado implementacion de
este item en python.



Ejercicio 3 

1. Asuma la definicion parcial de una clase Lista, que va a representar una lista simple:
class Nodo:
  def _init_(self, next = None, valor = None) :
  self.next = next
  self . valor = valor
class Lista:
  def _ init_(self) :
  self.head = []
  self.largo = 0

a. Escriba un metodo borrar (self, item), que elimine todas las apariciones
del item dado en la lista. En caso de requerir algun otro metodo adicional en
alguna de las dos clases, debe escribirlo. (25 puntos)

b. Escriba un metodo max ( self) , que obtiene el elemento mayor en la lista. En
caso de requerir algun otro metodo adicional en alguna de las dos clases, debe
escribirlo. (15 puntos)



Ejercicio 4

2. Para representar los datos de un estudiante del TEC, se va a manejar un objeto
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
nota obtenida por el estudiante.
a. Defina una clase en Python para manejar el objeto Estudiante. (35 pts).

b. Asuma que se tiene una lista de instancias del objeto Estudiante. Defina
una funcion llamada promedio (carnet, lista) , que reciba un carnet,
la lista de instancias del objeto Estudiante y muestre los datos del estudiante,
asi como el promedio de notas. Si el carnet no existe, debe indicarse por
medio de otro mensaje. (30 pts)


Ejercicio 5
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

mostrar(), que imprime todos los atributos del objeto
reset (), que pone en cero la cantidad de viajes realizados
enviar reparacion (), que actualiza el estado del camion a reparacion
recibir reparacion(), que actualiza el estado del camion a libre
. viaje(kilometros), que aumenta en 1 la cantidad de viajes realizados y calcula

el monto a pagar por el viaje, de acuerdo a la cantidad de kilometros de viaje.
Considere que los viajes economicos se pagan a 300 por kilometro y los premium
a 500 por kilometro
. set_calificacion(calificacion), que calcula el promedio de estrellas que tiene el
objeto basado en la calificacion actual y la nueva calificacion recibida.
Ademas, debe existir los metodos get tipo(), get estado() y get_viajes() que retor-
nan los datos correspondientes
Utilizando el lenguaje de programacion Python, se le solicita lo siguiente:
(a) Defina una clase Uber para el manejo de este objeto. 40 puntos.

(b) Luego de tener definida la clase, se asume que se tiene la lista de instancias y que se
quiere construir una funcion llamada solicita(lista, tipo, calificacion minima), que
recibe esa lista de instancias para saber cuales vehiculos podran transportar un cliente
segun un tipo de vehiculo y la calificacion minima solicitada por el cliente. 30 puntos.
