from abc import ABC, abstractmethod


class User(ABC):
  ''' Clase abstracta (interfaz) para estructurar 2 clases de tipos de usuarios '''
  def __init__(self,dni:str,name:str,age:int):
    self.dni = dni
    self.name = name
    self.age = age    

  
  @abstractmethod
  def describe(self):
      ''' Método abstracto que describe al usuario '''
      pass


class Cashier(User): 
  ''' Clase hija para cajeros '''
  def __init__(self,dni:str,name:str,age:int,timeTable:str,salary:float):
      super().__init__(dni, name, age)
      self.timeTable = timeTable
      self.salary = salary   
 
  
  def describe(self):
        ''' Método descripción implementado para cajeros '''
        return f"Cashier - Name: {self.name}, DNI: {self.dni} , Timetable: {self.timeTable}, Salary: {self.salary}."


class Customer(User):
  ''' Clase hija para clientes '''
  def __init__(self,dni:str,name:str,age:int,email:str,postalCode:str):
      super().__init__(dni, name, age)
      self.email = email
      self.postalCode = postalCode

  
  def describe(self):
        ''' Método descripción implementado para cajeros '''
        return f"Customer - Name: {self.name}, DNI: {self.dni} , Age: {self.age}, Email: {self.email}, Postal Code: {self.postalCode}"