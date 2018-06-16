mport csv
import os

row = []
def menu(username="@mariaali", products_count=100):
    # this is a multi-line string, also using preceding `f` for string interpolation
    menu = f"""
    -----------------------------------
    INVENTORY MANAGEMENT APPLICATION
    -----------------------------------
    Welcome {MariaALI}!
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
    return products


def auto_incremented_id(products):
    #return int(products[-1]["id"]) + 1
    all_ids = [int(p["id"]) for p in products]
    max_id = max(all_ids)
    next_id = max_id + 1
    return next_id

def find_product(products, id):
    for i, p in enumerate(products):
        if p["id"] == id:
            return i, p
    print("Sorry, product id", id, "has not been found")
    return None, None

def input_product_data():
    data = dict()
    for field in ("name", "department", "aisle", "price"):
        value = input("Please, enter " + field + ": ")
        data[field] = value
    return data


def run():

    try:
        products = read_products_from_file()
    except FileNotFoundError:
        print("Unable to open the inventory, resetting to default")
        products = reset_products_file()

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
        product_index, matching_product = find_product(products, product_id)
        #matching_product = matching_product[0]
        if matching_product is not None:
            print(matching_product)


    elif operation == "Create":
        product_data = input_product_data()
        product_data["id"] = str(auto_incremented_id(products))
        products.append(product_data)
        print("CREATING A NEW PRODUCT", product_data)
        write_products_to_file(products=products)


    elif operation == "Update":
        product_id = input("HEY, what's the identifier of the product you want to update: ")
        product_index, matching_product = find_product(products, product_id)
        if matching_product is not None:
            matching_product.update(input_product_data())
            print("UPDATING A PRODUCT", matching_product)
            write_products_to_file(products=products)



    elif operation == "Destroy":
        product_id = input("HEY, what's the identifier of the product you want to destroy: ")
        product_index, matching_product = find_product(products, product_id)
        #matching_product = [p for p in products if int(p["id"]) == int(product_id)]
        #matching_product = matching_product[0]
        if product_index is not None:
            del products[product_index]
            print("DELETING A PRODUCT", matching_product)
            write_products_to_file(products=products)


    elif operation == "Reset":
        products = reset_products_file()
    else:
        print("OOPS, unrecognized opertion, please select one of 'List', 'Show', 'Create', 'Destroy' or 'Reset'")




#def enlarge(my_number):
#    return my_number * 100















if __name__ == "__main__":
        run()
