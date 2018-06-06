#from products_app.app import enlarge

#def test_enlarge():
#    result = enlarge(40)
#    assert result == 4000



from products_app.app import auto_incremented_id, read_products_from_file

def test_auto_incr_id():
    products = [
        {"id": 45, "name":"testing", "aisle":"testing", "department":"testing", "price": 100.00}
    ]
    result = auto_incremented_id(products)
    assert result == 46

def test_auto_incr_id_out_of_order_products():
    products = [
        {"id": 49, "name":"testing", "aisle":"testing", "department":"testing", "price": 100.00},
        {"id": 45, "name":"testing", "aisle":"testing", "department":"testing", "price": 100.00}
    ]
    result = auto_incremented_id(products)
    assert result == 50

def test_auto_incr_id_empty_product():
    products = read_products_from_file("products_test.csv")
    result = auto_incremented_id(products)
    assert result == 201
