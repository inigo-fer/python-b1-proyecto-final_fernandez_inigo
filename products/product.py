from abc import ABC, abstractmethod
from .food_package import Wrapping, Bottle, Glass, Box


class Product(ABC):
    """ Clase abstracta (interfaz) para estructurar 4 clases de alimento. """
    def __init__(self,id:str,name:str,price:float):
      self.id = id
      self.name = name
      self.price = price     
    
    def describe(self):
        """Método que describe el producto."""
        return f"Product - Type: {self.type()}, Name: {self.name}, Id: {self.id} , Price: {self.price} , {self.foodPackage().describe()}."   
    
    @abstractmethod
    def type(self):
        """ Método abstracto que indica el tipo de alimento. """
        pass
    
    @abstractmethod
    def foodPackage(self):
        """ Método abstracto que indica el empaquetado. """
        pass  

class Hamburger(Product):
    """ Clase hija para hamburguesas. """
    def __init__(self,id:str,name:str,price:float):
        super().__init__(id,name,price)
    def type(self):
        return "Hamburger"
    def foodPackage(self):
        return Wrapping()

class Soda(Product):
    """ Clase hija para refrescos. """      
    def __init__(self,id:str,name:str,price:float):
        super().__init__(id,name,price)
    def type(self):
        return "Soda"
    def foodPackage(self):
        return Glass()

class Drink(Product):
    """ Clase hija para bebidas."""
    def __init__(self,id:str,name:str,price:float):
        super().__init__(id,name,price)
    def type(self):
        return "Drink"
    def foodPackage(self):
        return Bottle()

class HappyMeal(Product):
    """ Clase hija para Happy Meals™ ."""
    def __init__(self,id:str,name:str,price:float):
        super().__init__(id,name,price)
    def type(self):
        return "HappyMeal"
    def foodPackage(self):
        return Box()