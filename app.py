import csv
import os

row = []
def menu(username="@mariaali", products_count=100):
    # this is a multi-line string, also using preceding `f` for string interpolation
    menu = f"""
    -----------------------------------
    INVENTORY MANAGEMENT APPLICATION
    -----------------------------------
    Welcome {username}!
    There are {products_count} products in the database.
        operation | description
        --------- | ------------------
        'List'    | Display a list of product identifiers and names.
        'Show'    | Show information about a product.
        'Create'  | Add a new product.
        'Update'  | Edit an existing product.
        'Destroy' | Delete an existing product.
    Please select an operation: """ # end of multi- line string. also using string interpolation
    return menu



def read_products_from_file(filename="products.csv"):
    filepath = os.path.join(os.path.dirname(__file__), "db", filename)
    print(f"READING PRODUCTS FROM FILE: '{filepath}'")
    products = []

    with open(filepath, "r") as csv_file:
        reader = csv.DictReader(csv_file)
        for row in reader:
            products.append(dict(row))
    return products


def write_products_to_file(filename="products.csv", products=[]):
    filepath = os.path.join(os.path.dirname(__file__), "db", filename)
    #print(f"OVERWRITING CONTENTS OF FILE: '{filepath}' \n ... WITH {len(products)} PRODUCTS")
    with open(filepath, "w") as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=["id","name","aisle","department","price"])
        writer.writeheader() # uses fieldnames set above
        for p in products:
            writer.writerow(p)




def reset_products_file(filename="products.csv", from_filename="products_default.csv"):
    print("RESETTING DEFAULTS")
    products = read_products_from_file(from_filename)
    write_products_to_file(filename, products)


def auto_incremented_id(products):
    #return int(products[-1]["id"]) + 1
    all_ids = [int(p["id"]) for p in products]
    max_id = max(all_ids)
    next_id = max_id + 1
    return next_id


def run():

    products = read_products_from_file()

    number_of_products = len(products)
    my_menu = menu(username="@some-user", products_count=number_of_products)
    operation = input(my_menu)
    #print("YOU CHOSE: " + operation)
    operation = operation.title()

    if operation == "List":
        print("LISTING PRODUCTS")
        for p in products:
            print("   " + p["id"] + " " +  p["name"])

    elif operation == "Show":
        print("SHOWING A PRODUCT")
        product_id = input("HEY, whats the identifier of the product you want to display: ")
        matching_product = [p for p in products if int(p["id"]) == int(product_id)]
        matching_product = matching_product[0]
        print(matching_product)


    elif operation == "Create":
        new_id = int(products[-1]["id"]) + 1

        new_product = {
            "id": new_id,
            "name": "New Product",
            "aisle": "new aisle",
            "department": "new dept",
            "price": 100.00
        } # todo: capture user input
        products.append(new_product)
        print("CREATING A NEW PRODUCT", new_product)






    elif operation == "Update":
        product_id = input("HEY, what's the identifier of the product you want to display: ")
        matching_product = [p for p in products if int(p["id"]) == int(product_id)]
        matching_product = matching_product[0]
#todo:prompt the user for new attributes
        new_price = 200.00
        matching_product["price"] = new_price
        print("UPDATING A PRODUCT")



    products = read_products_from_file()

    number_of_products = len(products)
    my_menu = menu(username="@some-user", products_count=number_of_products)
    operation = input(my_menu)
    #print("YOU CHOSE: " + operation)
    operation = operation.title()

    if operation == "List":
        print("LISTING PRODUCTS")
        for p in products:
            print("   " + p["id"] + " " +  p["name"])

    elif operation == "Show":
        print("SHOWING A PRODUCT")
        product_id = input("HEY, whats the identifier of the product you want to display: ")
        matching_product = [p for p in products if int(p["id"]) == int(product_id)]
        matching_product = matching_product[0]
        print(matching_product)


    elif operation == "Create":
        new_id = auto_incremented_id(products)
        new_product = {
            "id": new_id,
            "name": "New Product",
            "aisle": "new aisle",
            "department": "new dept",
            "price": 100.00
        } # todo: capture user input
        products.append(new_product)
        print("CREATING A NEW PRODUCT", new_product)






    elif operation == "Update":
        product_id = input("HEY, what's the identifier of the product you want to display: ")
        matching_product = [p for p in products if int(p["id"]) == int(product_id)]
        matching_product = matching_product[0]

    elif operation == "Destroy":
        product_id = input("HEY, what's the identifier of the product you want to display: ")
        matching_product = [p for p in products if int(p["id"]) == int(product_id)]
        matching_product = matching_product[0]
        del products[products.index(matching_product)]
        print("DELETING A PRODUCT")




    elif operation == "RESET":
        reset_products_file()
    else:
        print("OOPS, unrecognized opertion, please select one of 'List', 'Show', 'Create', 'Destroy' or 'Reset'")

    write_products_to_file(products=products)




def enlarge(my_number):
    return my_number * 100















if __name__ == "__main__":
        run()

