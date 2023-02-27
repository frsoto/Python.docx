##################################################################################
from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def mover(self):
        pass
Animal() # No se puede instanciar las clases abstractas.

##################################################################################
#%%
from abc import ABC, abstractmethod
class Animal(ABC):
    def mover(self):
        pass
Animal() # la deja instanciar pq no tiene un metodo abstracto???




##################################################################################
#%%
from abc import ABC, abstractmethod

class Animal():
    @abstractmethod
    def mover(self):
        pass
Animal()

##################################################################################
#%%
from abc import ABC, abstractmethod

class Animal(ABC):  # le decimos a Python que es una clase abstracta.

    def __init__(self):
        __metaclass__ = ABCMeta # Metaclase

    @abstractmethod
    def mover(self):
        pass

    @abstractmethod
    def comer(self):
        print('Animal come')


class Gato(Animal):
    def mover(self):
        print('Mover gato')

    def comer(self):
        print('Gato Come')

g = Gato()  #
g.mover()
g.comer()

##################################################################################
#%%
from abc import ABC, abstractmethod



