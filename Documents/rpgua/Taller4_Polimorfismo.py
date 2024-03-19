class vehiculo:
    
    def __init__(self, matricula):
        self.matricula = matricula
        self.velocidad = 0
        
    def __str__(self):
        print("Matricula: ", self.matricula)
        print("Velocidad: ", self.velocidad)

    def acelerar(self, cantidad):
        self.velocidad += cantidad

class coche(vehiculo):

    def __init__(self, matricula, puertas):
        super().__init__(matricula)
        self.puertas = puertas

    def cantPuertas(self):
        print("puertas: ", self.puertas)

class camion(vehiculo):

    def __init__(self, matricula,):
        super().__init__(matricula)
        self.remolque = None

    def ponRemolque(self, remolque):
        self.remolque = remolque
    
    def quitaRemolque(self):
        self.remolque = None    
    
    def __str__(self):
        vehiculo.__str__(self)
        if self.remolque:
            print("Remolque: ", self.remolque)
        else:
            return  
           
    def acelerar(self, cantidad,):
        super().acelerar(cantidad)
        if self.remolque != None and self.velocidad + self.cantidad > 100 :
            return print("DemasiadoRapidoException")

class remolque:

    def __init__(self, peso):
        self.peso = peso

    def toString(self):
        print("Informacion remolque: ", self.peso)

class DemasiadoRapidoException(Exception):

    def acelerar(self, cantidad):
        if isinstance(self, camion) and self.remolque and self.velocidad + cantidad > 100:
            return DemasiadoRapidoException("Demasiado rapido")
        else:
            super().acelerar(cantidad)

asd = camion("asd293")
asd.acelerar(50)
asd.ponRemolque("carga grande")
asd.__str__()


class empleado:
    
    def __init__(self, nombre, apellidos, Dni, direccion, salario, telefono, supervisor,añosDeAntiguedad):
        
        self.nombre = nombre
        self.apellidos = apellidos
        self.Dni = Dni
        self.direccion = direccion
        self.añosDeAntiguedad = añosDeAntiguedad
        self.telefono = telefono
        self.salario = salario
        self.supervisor = supervisor
        
    def imprimir(self):
        print("Nombre:", self.nombre)
        print("Apellidos:", self.apellidos)
        print("DNI:", self.Dni)
        print("Direccion:", self.direccion)
        print("Años en la empresa:", self.añosDeAntiguedad)
        print("Telefono:", self.telefono)
        print("Salario:", self.salario)
        print("supervisor:", self.supervisor)
        
    def incrementarSalario(self, salario):
        self.salario = salario
    
    def cambiarSupervisor(self, supervisor):
        self.supervisor = supervisor     

class secretario(empleado):
    
    def __init__(self, nombre, apellidos, Dni, direccion, salario, telefono, supervisor, añosDeAntiguedad, despacho, fax):
        super().__init__(nombre, apellidos, Dni, direccion, salario, telefono, supervisor, añosDeAntiguedad)
        self.despacho = despacho
        self.fax = fax
        
    def imprimir(self):
        self.salario = self.salario+((5/100)*self.salario)
        super().imprimir()
        
        if isinstance(self,secretario):
            print("despacho:", self.despacho)
            print("Fax:", self.fax)
            print("Puesto en la empresa: Secretario")

class vendedor(empleado):
    
    def __init__(self, nombre, apellidos, Dni, direccion, salario, telefono, supervisor, añosDeAntiguedad, matricula, marca, modelo, areaDeventa, ):
        super().__init__(nombre, apellidos, Dni, direccion, salario, telefono, supervisor, añosDeAntiguedad)
        self.matricula = matricula
        self.marca = marca
        self.modelo = modelo
        self.areaDeventa = areaDeventa
            
    def imprimir(self):
        self.salario = self.salario+((10/100)*self.salario)
        super().imprimir()
        
        if isinstance(self,vendedor):
            print(" marca ", self.marca)
            print("modelo: ", self.modelo)
            print("Area de venta: ", self.areaDeventa)
            print("Puesto en la empresa: Vendedor")
            
class jefeDeZona(empleado):
    
    def __init__(self, nombre, apellidos, Dni, direccion, salario, telefono, supervisor, añosDeAntiguedad, despacho, secretario, vendedores):
        super().__init__(nombre, apellidos, Dni, direccion, salario, telefono, supervisor, añosDeAntiguedad)
        self.despacho = despacho
        self.secretario = secretario
        self.vendedores = vendedores
        
    def imprimir(self):
        self.salario = self.salario+((20/100)*self.salario)
        super().imprimir()
        
        if isinstance(self,jefeDeZona):
            print(" despacho ", self.despacho)
            print("secretario: ", self.secretario)
            print("num de vendedores: ", self.vendedores)
            print("Puesto en la empresa: Jefe de zona")

    
asd = secretario("dacid","wall",100,"s 23",100,321343,"sas",12,23,22)
asd.imprimir()

asd1 = vendedor("clow","soft",2,"a 23",100,321343,"blum",12,233,"bmw",233,1)
asd1.imprimir()

asd2 = jefeDeZona("mafd","clink",3,"sd 23",100,321343,"dsa",12,233,2,233)
asd2.imprimir()







