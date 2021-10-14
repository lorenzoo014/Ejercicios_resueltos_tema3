print("estoy mayor")
class Animal:
 # variable de clase que se inicializa cuando se importa el
modulo animal
 numAnimales = 0
 def __init__(self, age = "1", name = "dog"):
 self.age = age # public attribute
 self.name = name # public attribute
 self.vivo = True
 Animal.numAnimales +=1
 def saluda(self, saludo='Hola', receptor = 'nuevo amigo'):
 print(saludo + " " + receptor)
 def mostrarNombre(self):
 print(self.age)
 def mostrarEdad(self):
 print(self.name)
 def morir(self):
 if(self.vivo):
 self.vivo = False
 Animal.numAnimales -=1
 @staticmethod
 def get_numAnimales():
 return numAnimales
 print('Hola')