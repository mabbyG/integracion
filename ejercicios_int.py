class Persona():

    def __init__(self,nombre_apellido="", edad=0):
        self.nombre_apellido=nombre_apellido
        self.edad=edad
    @property
    def nombre_apellido(self):
        return self.__nombre_apellido
    @property
    def edad(self):
        return self.__edad
    
    @nombre_apellido.setter
    def nombre_apellido(self,nombre_apellido):
        self.__nombre_apellido=nombre_apellido
    @edad.setter
    def edad(self,edad):
        if edad < 17:
            print("Edad inválida")
            self.__edad=17
        else:
            self.__edad=edad
        
    def mostrar(self):
        return "Nombre_Apellido:"+self.nombre_apellido+" - Edad:"+str(self.edad)


    def esMayorDeEdad(self):
        return self.edad>=18



class Cuenta():

    def __init__(self,titular,cantidad=0):
        self.titular=titular
        self.__cantidad=cantidad
    
    @property
    def titular(self):
        return self.__titular
    
    @property
    def cantidad(self):
        return self.__cantidad

    @titular.setter
    def titular(self,titular):
        self.__titular=titular

    
    def mostrar(self):
        return "Cuenta\n"+"Titular:"+self.titular.mostrar()+" - Cantidad:"+str(self.cantidad)
    
    def ingresar(self,cantidad):
        if cantidad > 0:
            self.__cantidad = self.__cantidad + cantidad
    
    def retirar(self,cantidad):
        if cantidad > 0:
            self.__cantidad = self.__cantidad - cantidad
    


class CuentaJoven(Cuenta):

    def __init__(self,titular,cantidad=0,bonificacion=0):
        super().__init__(titular,cantidad)
        self.bonificacion=bonificacion
    
    @property
    def bonificacion(self):
        return self.__bonificacion
    
    @bonificacion.setter
    def bonificacion(self,bonificacion):
        self.__bonificacion=bonificacion

    def mostrar(self):
        return "Cuenta Joven\n"+"Titular:"+self.titular.mostrar()+" - Cantidad:"+str(self.cantidad)+ "- Bonificación:"+str(self.bonificacion)+"%"

    def esTitularValido(self):
        return self.titular.edad < 25 and self.titular.esMayorDeEdad()
    
    def retirar(self,cantidad):
        if not self.esTitularValido():
            print ("No puesdes retirar el dinero. titular no válido")
        elif cantidad > 0:
            super().retirar(cantidad)
            
            
#test de funcionamiento

persona1= Persona("Jorge" "perez", 16)
cuenta1= Cuenta(titular=persona1,cantidad=5000)
print(cuenta1.mostrar())
cuenta1.ingresar(2000.50)
print(cuenta1.mostrar())
cuenta1.retirar(1000.50)
print(cuenta1.mostrar())
cuenta1.retirar(6500)
print(cuenta1.mostrar())
persona2= Persona("Merlina Xammp", 45)
cuenta2= CuentaJoven(titular=persona2,cantidad=5000,bonificacion=10)
print(cuenta2.mostrar())
cuenta2.ingresar(2000.50)
print(cuenta2.mostrar())
persona1= Persona("Jorge PEREZ", 16)
cuenta1= Cuenta(titular=persona1,cantidad=5000)
print(cuenta1.mostrar())
cuenta1.ingresar(2000.50)
print(cuenta1.mostrar())
