#%%
"""
Creare una clase "Animal", la cual utilizaremos para efectuar nuestros ejemplos
La clase constara de dos metods.
setName: el cual asignara un nombre al animal
getName: el cual nos retornara el nombre del animal
"""

# Declaramos nuestra clase
class Animal(object):

    # Primer método
    def setName(self, name):
        self.name = name

    # Segundo método
    def getName(self):
        return self.name

# Ahora podemos crear una instancia de nuestra clase y utilizar sus métodos:
animal = Animal() # Instancia de nuestra clase
animal.setName("Perro") # Asignación de nombre
print(animal.getName()) # Perro

#%%
# Muy bien, ahora vemos como utilizar abc:
from abc import ABC, abstractmethod

# Declaramos nuestra clase
class Animal(ABC):
    def __init__(self):
        __metaclass__ = ABCMeta  # Metaclase

    @abstractmethod # Decorador para métodos absctractos
    def setName(self, name):
        self.name = name

    @abstractmethod # Decorador para métodos absctractos
    def getName(self):
        return self.name






























