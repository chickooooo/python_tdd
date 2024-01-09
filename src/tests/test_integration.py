"""Integration Test Cases

- create new product in database
- get no product from database
- get product from database
- get multiple products from database
- update product in database
- delete product from database
"""

from core.dependency_injection import product_crud_usecase
from core.services.sql_service.mysql_service import DATABASE
from features.product.models.product import Product


def test_create_product_in_database():
    """Create new product in database."""

    # verify empty database
    assert DATABASE == []

    # create product in database
    product_crud_usecase.create_product(
        {
            "id": 1,
            "name": "apple",
            "price": 2.99,
        }
    )

    # verify product present in database
    assert DATABASE == [{"id": 1, "name": "apple", "price": 2.99}]

    # remove product from database
    DATABASE.pop()


def test_get_no_product_from_database():
    """Get no product from database."""

    # add a record in database
    DATABASE.append({"id": 1, "name": "apple", "price": 2.99})

    # verify single record in database
    assert DATABASE == [{"id": 1, "name": "apple", "price": 2.99}]

    # get product from database
    product = product_crud_usecase.get_product({"name": "orange"})

    # verify product
    assert product is None

    # remove product from database
    DATABASE.pop()


def test_get_product_from_database():
    """Get product from database."""

    # add a record in database
    DATABASE.append({"id": 1, "name": "apple", "price": 2.99})

    # verify single record in database
    assert DATABASE == [{"id": 1, "name": "apple", "price": 2.99}]

    # get product from database
    product = product_crud_usecase.get_product({"name": "apple"})

    # verify product type
    assert type(product) is Product
    # verify product data
    assert product.id == 1
    assert product.name == "apple"
    assert product.price == 2.99

    # remove product from database
    DATABASE.pop()


def test_get_multiple_products_from_database():
    """Get multiple products from database."""

    # add records in database
    DATABASE.append({"id": 1, "name": "apple", "price": 2.99})
    DATABASE.append({"id": 2, "name": "orange", "price": 3.99})
    DATABASE.append({"id": 3, "name": "banana", "price": 2.99})

    # verify database initial state
    assert DATABASE == [
        {"id": 1, "name": "apple", "price": 2.99},
        {"id": 2, "name": "orange", "price": 3.99},
        {"id": 3, "name": "banana", "price": 2.99},
    ]

    # get products from database
    products = product_crud_usecase.get_products({"price": 2.99})

    # verify products type
    assert type(products) is list
    assert type(products[0]) is Product
    assert type(products[1]) is Product

    # verify product data
    assert products[0].id == 1
    assert products[0].name == "apple"
    assert products[0].price == 2.99
    assert products[1].id == 3
    assert products[1].name == "banana"
    assert products[1].price == 2.99

    # remove products from database
    DATABASE.pop()
    DATABASE.pop()
    DATABASE.pop()


def test_update_product_in_database():
    """Update product in database."""

    # product data
    item = {"id": 1, "name": "apple", "price": 2.99}

    # add data in database
    DATABASE.append(item)

    # verify single record in database
    assert DATABASE == [item]

    # create a product
    product = Product(**item)
    # update product price
    product.price = 8.99

    # update product in database
    result = product_crud_usecase.update_product(product)

    # verify result
    assert result is None

    # verify record updated in database
    assert DATABASE == [{"id": 1, "name": "apple", "price": 8.99}]

    # remove product from database
    DATABASE.pop()


def test_delete_product_in_database():
    """Delete product from database."""

    # add a record in database
    DATABASE.append({"id": 1, "name": "apple", "price": 2.99})

    # verify single record in database
    assert DATABASE == [{"id": 1, "name": "apple", "price": 2.99}]

    # delete product from database
    result = product_crud_usecase.delete_product({"id": 1})

    # verify result
    assert result is None

    # verify empty database
    assert DATABASE == []
