from abc import ABC, abstractmethod
from users import Cashier,Customer
from products import Hamburger,Soda,Drink,HappyMeal

class Converter(ABC):
  @abstractmethod
  def convert(self,dataFrame,*args):
      pass  
  def print(self, objects):
    for item in objects:
      print(item.describe())

class CashierConverter(Converter):
  """Conversión de cada linea del dataframe  en un item de una lista de objetos de la clase user.cashier."""
  def convert(self,dataFrame):    
      cashier_list=[]
      for _, row in dataFrame.iterrows(): # _ para indicar que no el index del dataframe no se utilizará
        cashier = Cashier(                # mapeo de cada columna del dataframe con los atributos de la clase
            dni=row['dni'],
            name=row['name'],
            age=int(row['age']),
            timeTable=row['timetable'],
            salary=float(row['salary'])
        )
        cashier_list.append(cashier)
      return cashier_list

class CustomerConverter(Converter):
    """Conversión de cada linea del dataframe en un item de una lista de objetos de la clase user.customer."""
    def convert(self,dataFrame):    
      customer_list=[]
      for _, row in dataFrame.iterrows():
        customer = Customer(
            dni=row['dni'],
            name=row['name'],
            age=int(row['age']),
            email=row['email'],
            postalCode=row['postalcode']
        )
        customer_list.append(customer)
      return customer_list

class ProductConverter(Converter):
  """Conversión de cada linea del dataframe en un item de una lista de objetos de subclase product 
  en función del tipo de producto."""
  def convert(self,dataFrame,product_type):    
      product_list=[]
      for _, row in dataFrame.iterrows():
        if product_type == 'Hamburger':
            product = Hamburger(
               id=row['id'], 
               name=row['name'], 
               price=float(row['price'])
               )
        elif product_type == 'Soda':
            product = Soda(               
               id=row['id'], 
               name=row['name'], 
               price=float(row['price'])
               )
        elif product_type == 'Drink':
            product = Drink(
               id=row['id'], 
               name=row['name'], 
               price=float(row['price'])
               )
        elif product_type == 'HappyMeal':
            product = HappyMeal(
               id=row['id'], 
               name=row['name'], 
               price=float(row['price'])
               )
        else:
            continue
        product_list.append(product)
      return product_list