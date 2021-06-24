#
#
#
#                                               Examen III
#                                             José Andrés Vargas Torres
#                                               Carnet 2021453583
#
#

class VehiculoAutonomo:
    def __init__(self,ID,color,anno,modelo,piloto_automatico,rango_de_precio,autonomia):
        self.ID = ID
        self.color = color
        self.anno = anno
        self.modelo = modelo
        self.piloto_automatico = piloto_automatico
        self.rango_de_precio = rango_de_precio
        self.autonomia = autonomia

    def mostrar(self):
        print("ID del vehiculo:   {}".format(self.ID))
        print("Color del vehículo:   {}".format(self.color))
        print("Año del vehículo:   {}".format(self.anno))
        print("Modelo del vehículo:   {}".format(self.modelo))
        print("El piloto automático corresponde a:   {}".format(self.piloto_automatico))
        print("Rango de precio del vehículo es:   {}".format(self.rango_de_precio))
        print("El vehículo tiene {}km de autonomía".format(self.autonomia))

    def set_autonomia(self,rango):
        self.autonomia = rango
        #return self.autonomia

    def add_auto_pilot(self):
        self.piloto_automatico = True
        #return "Sí posee piloto automático"

    def remove_auto_pilot(self):
        self.piloto_automatico = False
        #return "No tiene piloto automático"

    def set_price(self,dolares):
        if dolares <= 20000:
            self.rango_de_precio = "economico"
            #print("economico")
        if dolares > 20000 and dolares <= 40000:
            self.rango_de_precio = "medio"
            #print("medio")
        if dolares > 40000:
            self.rango_de_precio = "premium"
            #print("premium")
vehiculo1 = VehiculoAutonomo("12345","blanco",2020,"Caviar Model",True,"economico",45)
vehiculo2 = VehiculoAutonomo("54663","rojo",2019,"Nissan",False,"economico",45)
vehiculo3 = VehiculoAutonomo("JIRT34","negro",2021,"Hyundai",True,"economico",45)
vehiculo4 = VehiculoAutonomo("JOE34","azul",2022,"Subaru",False,"economico",45)
vehiculo1.mostrar()
lista_vehiculos = [vehiculo1,vehiculo2,vehiculo3,vehiculo4]

def posibles_candidatos(lista,color,rango_precio,modelo):
    for vehiculo in lista:
        if vehiculo.color == color and vehiculo.rango_de_precio == rango_precio and \
                vehiculo.modelo == modelo:
            print("La ID del vehículo que usted desea es:   {}".format(vehiculo.ID))


posibles_candidatos(lista_vehiculos,"negro","economico","Hyundai")


