class Product:
    def __init__(self,id,name,price,qty):
        self.id = id
        self.name = name
        self.price = price
        self.qty = qty


    def display(self):
        print(f"Id : {self.id}")
        print(f"Name : {self.name}")
        print(f"Price : {self.price}")
        print(f"Quantity : {self.qty}")