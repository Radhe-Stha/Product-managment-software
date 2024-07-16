from product import Product
import controller as c


option_text = """
What you want to do [1-4]
1. Add new product
2. View all products
3. View single product
4. Delete a product
"""

option = int(input(option_text))

if option == 1:
    print("Adding a new product : ")
    c.add_product()
elif option == 2:
    print("View all products : ")
    c.view_all_products()
elif option == 3:
    print("View single product :")
    c.view_single_product()
elif option == 4:
    print("Deleting a product : ")
    c.delete_product()
else :
    print("Invalid Option ! ")