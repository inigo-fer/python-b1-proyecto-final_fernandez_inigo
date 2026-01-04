from util.file_manager import CSVFileManager
from util.converter import CashierConverter, CustomerConverter, ProductConverter
from orders import Order

class PrepareOrder:
    '''Clase principal que permita integrar los módulos y preparar los pedidos'''
    
    def __init__(self,data_dir='data/'):
        '''Método __init__ para que la lectura y conversión ocurra al lanzar PrepareOrder'''
        self.data_dir = data_dir

        # --- Cashiers ---
        df_cashiers = CSVFileManager(f"{data_dir}cashiers.csv").read()
        '''lectura de CSV y conversión a dataframe'''
        self.cashiers = CashierConverter().convert(df_cashiers)
        '''Almacenamiento en un atributo de instancia (en lugar de variable) 
        para que otros métodos puedan acceder a los datos cargados'''
        
        # --- Customers ---
        df_customers = CSVFileManager(f"{data_dir}customers.csv").read()
        self.customers = CustomerConverter().convert(df_customers)

        # --- Products por tipo ---
        df_hamburgers = CSVFileManager(f"{data_dir}hamburgers.csv").read()
        df_sodas      = CSVFileManager(f"{data_dir}sodas.csv").read()
        df_drinks     = CSVFileManager(f"{data_dir}drinks.csv").read()
        df_happy      = CSVFileManager(f"{data_dir}happyMeal.csv").read()

        self.hamburgers = ProductConverter().convert(df_hamburgers,"Hamburger")
        self.sodas      = ProductConverter().convert(df_sodas,"Soda")
        self.drinks     = ProductConverter().convert(df_drinks,"Drink")
        self.happy_meals = ProductConverter().convert(df_happy,"HappyMeal")

    # --- FUNCIONES ACCESORIAS ---
    def list_cashiers(self):
        '''Muestra cajeros: nombre y DNI.'''
        print("\nSelect the cashier using the dni:")
        for c in self.cashiers:
            print(f"- {c.name} (DNI: {c.dni})")

    def list_customers(self):
        '''Muestra clientes: nombre y DNI.'''
        print("\nSelect the customer using the dni:")
        for u in self.customers:
            print(f"- {u.name} (DNI: {u.dni})")

    def list_products_of_type(self, type_str):
        '''Muestra productos del tipo elegido por el usuario.'''
        products = self._pick_products_list_by_type(type_str)
        print(f"\nSelect a {type_str} using the id:")
        for p in products:
            print(f"- {p.id} | {p.name} | {p.price}")

    def find_cashier(self, dni: str):
        '''Busca cajeros'''
        dni = dni.strip()
        for c in self.cashiers:
            if str(c.dni).strip() == dni:
                return c
        return None

    def find_customer(self, dni: str):
        '''Busca clientes'''
        for u in self.customers:
            if str(u.dni) == dni:
                return u
        return None

    def find_product_by_id_in_type(self, product_id: str, type_str: str):
        '''Busca un producto por id dentro de la lista del tipo seleccionado.'''
        product_id = product_id.strip().upper()
        products = self._pick_products_list_by_type(type_str)
        for p in products:
            if str(p.id) .strip().upper()== product_id:
                return p
        return None

    def _pick_products_list_by_type(self, type_str: str):
        '''Devuelve la lista según el tipo.'''
        if type_str == "Hamburger":   return self.hamburgers
        if type_str == "Soda":        return self.sodas
        if type_str == "Drink":       return self.drinks
        if type_str == "HappyMeal":   return self.happy_meals
        return []

    def _map_type_number(self, n: str):
        '''1–4 → nombre de tipo; devuelve None si inválido.'''
        mapping = {
            "1": "Hamburger",
            "2": "Soda",
            "3": "Drink",
            "4": "HappyMeal",
        }
        return mapping.get(n)

    # ----------------- MENU / Flujo interactivo -----------------

    def prepare_order_flow(self):
        print("\n--- Welcome to McPython, your favorite restaurant! ---")
        '''Flujo: listar y elegir cajero/cliente, seleccionar tipo y productos, crear y mostrar el pedido.'''

        # 1) Mostrar cajeros y seleccionar por dni
        self.list_cashiers()
        dni_cajero = input("\nInsert the dni: ").strip()
        cashier = self.find_cashier(dni_cajero)
        if not cashier:
            print("Cashier not found.")
            return
        print("\n" + cashier.describe())

        # 2) Mostrar clientes y seleccionar por dni
        self.list_customers()
        dni_cliente = input("\nInsert the dni: ").strip()
        customer = self.find_customer(dni_cliente)
        if not customer:
            print("Customer not found.")
            return
        print("\n" + customer.describe())

        # 3) Inicializar orden
        order = Order(cashier, customer)

        # 4) Bucle de selección de productos:
        while True:
            # Mostrar tipos 1–4
            print("\nSelect product type:")
            print("1) Hamburger")
            print("2) Soda")
            print("3) Drink")
            print("4) Happy Meal")

            type_number = input("Type number: ").strip()
            type_str = self._map_type_number(type_number)
            if not type_str:
                print("Type number incorrect.")
                continue

            # Listar productos del tipo y seleccionar por id
            self.list_products_of_type(type_str)
            pid = input("Insert product id: ").strip().upper()
            product = self.find_product_by_id_in_type(pid, type_str)
            if not product:
                print("Product not found.")
            else:
                print(product.describe())
                order.add(product)

            # ¿Añadir otro producto?
            another = input("Do you want to add another product? (Yes/No): ").strip().lower()
            if another in ("no", "n"):
                break

        # 5) Mostrar ticket final
        print("\n--- ORDER ---")
        order.show()

if __name__ == "__main__":
    '''ENTRY POINT'''
    app = PrepareOrder(data_dir="data/")
    app.prepare_order_flow()

