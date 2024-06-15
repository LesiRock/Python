#CREACION DE LA CLASE, se usa class
class Usuario():
    def __init__(self, nombre, telefono, correo, sexo, edad): 
        self.nombre = nombre
        self.telefono = telefono
        self.correo = correo
        self.sexo = sexo
        self.edad = edad

    def mostrar(self)
        print(f******DATOS DEL USUARIO*******)

#para instanciar. Instanciamos el objeto
usuario1 = Usuario("Isel", "5537654567", "iserl@gmail.com", "f", 34)

#accediendo a los atributos
#print(usuario1.nombre)
usuario1.mostrar()