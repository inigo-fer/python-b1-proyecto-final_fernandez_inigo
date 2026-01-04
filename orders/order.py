from users.user import Cashier,Customer
from products.product import Product


class Order:
  '''Clase que representa el pedido que está siendo procesado'''

  def __init__(self, cashier:Cashier, customer:Customer):
    self.cashier = cashier
    self.customer = customer
    self.products = []

  
  def add(self, product : Product):
    '''Función para añadir un producto al pedido'''
    self.products.append(product)

  def calculateTotal(self) -> float:
    '''Función para calcular el precio total del pedido'''
    total=0.0
    for product in self.products:
            total += product.price
    return total
  
  def show(self):    
    print("\nHello : \n"+self.customer.describe()+"\n")
    print("Was attended by : \n"+self.cashier.describe()+"\n")
    print("You ordered : \n")
    for product in self.products:
      print(product.describe()+"\n")
    print(f"Total price : {self.calculateTotal()}"+"\n")
    print("Enjoy your meal!\n")
