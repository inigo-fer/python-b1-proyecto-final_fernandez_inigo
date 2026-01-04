"""Módulo que gestiona la preparación de pedidos en McPython, tu restaurante favorito."""

from util.file_manager import CSVFileManager
from util.converter import CashierConverter, CustomerConverter, ProductConverter
from orders import Order

class PrepareOrder:
    """Clase principal que permite integrar los módulos y preparar los pedidos."""
    
    def __init__(self, data_dir='data/'):
        """Método __init__ para que la lectura y conversión ocurra al lanzar PrepareOrder."""
        self.data_dir = data_dir

        # --- Cashiers ---
        # lectura de CSV y conversión a dataframe
        df_cashiers = CSVFileManager(f"{data_dir}cashiers.csv").read()
        # almacenamiento en un atributo de instancia
        self.cashiers = CashierConverter().convert(df_cashiers)
                
        # --- Customers ---
        df_customers = CSVFileManager(f"{data_dir}customers.csv").read()
        self.customers = CustomerConverter().convert(df_customers)

        # --- Products por tipo ---
        # Diccionario con tipos y atributos para usar en lectura y conversión del CSV
        product_info = {
            "hamburgers": ("hamburgers", "Hamburger"),
            "sodas": ("sodas", "Soda"),
            "drinks": ("drinks", "Drink"),
            "happyMeal": ("happy_meals", "HappyMeal"),
        }

        # Para cada tipo, lee el CSV correspondiente, lo convierte en data frame y lo almacena dinámicamente en el atributo
        for filename, (attr_name, type_name) in product_info.items():
            csv_path = f"{data_dir}{filename}.csv"
            df = CSVFileManager(csv_path).read()
            products = ProductConverter().convert(df, type_name)
            self.__dict__[attr_name] = products


    # --- FUNCIONES ACCESORIAS ---
    def list_cashiers(self):
        """Muestra cajeros: nombre y DNI."""
        print("\nSelect the cashier using the dni:")
        for c in self.cashiers:
            print(f"- {c.name} (DNI: {c.dni})")

    def list_customers(self):
        """Muestra clientes: nombre y DNI."""
        print("\nSelect the customer using the dni:")
        for u in self.customers:
            print(f"- {u.name} (DNI: {u.dni})")

    def list_products_of_type(self, type_str):
        """Muestra productos del tipo elegido por el usuario."""
        products = self._pick_products_list_by_type(type_str)
        print(f"\nSelect a {type_str} using the id:")
        for p in products:
            print(f"- {p.id} | {p.name} | {p.price}")

    def _find_by_dni(self, dni: str, collection):
        """Busca un objeto con atributo dni dentro de una colección."""
        dni = dni.strip()
        for obj in collection:
            if str(obj.dni).strip() == dni:
                return obj
        return None
    
    def find_cashier(self, dni: str):
        """Busca cajeros."""
        return self._find_by_dni(dni, self.cashiers)

    def find_customer(self, dni: str):
        """Busca clientes."""
        return self._find_by_dni(dni, self.customers)

    def find_product_by_id_in_type(self, product_id: str, type_str: str):
        """Busca un producto por id dentro de la lista del tipo seleccionado."""
        product_id = product_id.strip().upper()
        products = self._pick_products_list_by_type(type_str)
        for p in products:
            if str(p.id).strip().upper() == product_id:
                return p
        return None

    def _pick_products_list_by_type(self, type_str: str):
        """Devuelve la lista según el tipo."""
        if type_str == "Hamburger":return self.hamburgers
        if type_str == "Soda":return self.sodas
        if type_str == "Drink":return self.drinks
        if type_str == "HappyMeal":return self.happy_meals
        return []

    def _map_type_number(self, n: str):
        """1–4 → nombre de tipo; devuelve None si inválido."""
        mapping = {
            "1": "Hamburger",
            "2": "Soda",
            "3": "Drink",
            "4": "HappyMeal",
        }
        return mapping.get(n)

    # ----------------- MENU -----------------

    def prepare_order_flow(self):
        """Flujo: listar y elegir cajero/cliente, seleccionar tipo y productos, crear y mostrar el pedido."""
        print("\n--- Welcome to McPython, your favorite restaurant! ---\n")
        
        # Mostrar cajeros y seleccionar por dni
        self.list_cashiers()
        dni_cajero = input("\nInsert the dni: ").strip()
        cashier = self.find_cashier(dni_cajero)
        if not cashier:
            print("Cashier not found.")
            return
        print("\n" + cashier.describe())

        # Mostrar clientes y seleccionar por dni
        self.list_customers()
        dni_cliente = input("\nInsert the dni: ").strip()
        customer = self.find_customer(dni_cliente)
        if not customer:
            print("Customer not found.")
            return
        print("\n" + customer.describe())

        # Inicializar orden
        order = Order(cashier, customer)

        # Bucle de selección de productos:
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

            # Listar productos del tipo elegido y seleccionar por id
            self.list_products_of_type(type_str)
            pid = input("Insert product id: ").strip().upper()
            product = self.find_product_by_id_in_type(pid, type_str)
            if not product:
                print("Product not found.")
            else:
                print(product.describe()+"\n")
                order.add(product)

            # ¿Añadir otro producto? Si elgie no, se enseña el pedido final
            another = input("Do you want to add another product? (Yes/No): ").strip().lower()
            if another in ("no", "n"):
                break

        # Mostrar pedido final
        print("\n--- ORDER ---")
        order.show()

if __name__ == "__main__":
    """ENTRY POINT"""
    app = PrepareOrder(data_dir = "data/")
    app.prepare_order_flow()

