from abc import ABC, abstractmethod


class FoodPackage (ABC): 
    """ Clase abstracta (interfaz) para estructurar 4 clases de tipos de paquete y material, en función del alimento."""    
        
    @abstractmethod
    def pack(self):
        """ Método abstracto que indica el empaquetado."""
        pass

    @abstractmethod
    def material(self):
        """ Método abstracto que indica el material."""
        pass
    
    def describe(self):
        """ Método que describe el empaquetato. """
        return f"Package: {self.pack()} , Material: {self.material()}"    


class Wrapping(FoodPackage):  
  """ Clase hija para alimentos envueltos. """
  def pack(self):
      return "Food Wrap Paper"
  
  def material(self):
      return "Aluminium"


class Bottle(FoodPackage): 
  """ Clase hija para alimentos embotellados. """
  def pack(self):
      return "Bottle"
  
  def material(self):
      return "Plastic"


class Glass(FoodPackage):  
  """ Clase hija para alimentos en vaso de papel. """      
  def pack(self):
      return "Glass"
  
  def material(self):
      return "Paper"


class Box(FoodPackage): 
  """ Clase hija para alimentos en caja. """
  def pack(self):
      return "Box"
  
  def material(self):
      return "Cardboard"