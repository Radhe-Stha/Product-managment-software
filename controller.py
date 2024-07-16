from product import Product
import csv
import controller as c

all_products = []
def convert_product_to_csv(listofproduct):
    file = open("products.csv", "w")
    file.write("")
    file.close()
    for c in listofproduct:
        f = open("products.csv", "a")
        f.write(f"{c.id},{c.name},{c.price},{c.qty}\n")
        f.close()

def convert_csv_to_product_list():
    all_products = []
    with open('products.csv', 'r') as file:
        csv_reader = csv.reader(file)
        for row in csv_reader:
            c = Product(id=row[0], name=row[1], price=float(row[2]), qty=(row[2]))
            all_products.append(c)
    return all_products


def add_product():
    p = Product(id="",name="",price=0,qty=0)
    p.id = int(input("Enter product Id : "))
    p.name = input("Enter producr Name : ")
    p.price = float(input("Enter product Price : "))
    p.qty = int(input("Enter product Quantity : "))

    f = open("products.csv","a")
    f.write((f"{p.id},{p.name},{p.price},{p.qty}\n"))
    f.close()
    print(f"Product {p.name} added succesfully ")


def view_all_products():
    f = open("products.csv","r")
    print(f.read())
    print("Viewed all products")


def view_single_product():
    #print("View Single product")
    id = input("Enter product id: ")
    with open('products.csv', 'r') as file:
        csv_reader = csv.reader(file)
        for row in csv_reader:
            #print(f"{row} Hello")
            c = Product(id=row[0], name=row[1], price=float(row[2]), qty=row[3])
            all_products.append(c)

    record_found = False
    product = Product(id="", name="", price=0, qty=0)
    for c in all_products:
        if c.id == id:
            record_found = True
            product = c
            break
        else:
            record_found = False
    if record_found == True:
        print("record is found: ")
        product.display()
    else: print("Product id not found.")



def delete_product():
    #print(f"Deleting product")
    lists = c.convert_csv_to_product_list()
    updated_product = []
    idtodelete= input("Enter product id: ")
    record_found = False
    for product in lists:
        if product.id == idtodelete:
            record_found = True
        else:
            updated_product.append(product)

    if record_found:
        c.convert_product_to_csv(updated_product)
        print("Deleted Successfully")
    else:
        print("No record found")
    

