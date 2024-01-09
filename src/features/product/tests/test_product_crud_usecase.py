"""Test Cases

- ProductCrudUsecase depends on SQLService
    -- no object provided
    -- incorrect object provided
    -- correct object provided and private instance created

- ProductCrudUsecase has a create_product() method
    -- with parameter product_data of type 'dict'
    -- with return type of 'Product'

- ProductCrudUsecase has a get_product() method
    -- with parameter query_data of type 'dict'
    -- with return type of 'Product | None'

- ProductCrudUsecase has a get_products() method
    -- with parameter query_data of type 'dict'
    -- with return type of 'list[Product]'

- ProductCrudUsecase has a update_product() method
    -- with parameter updated_product of type 'Product'
    -- with return type of 'None'

- ProductCrudUsecase has a delete_product() method
    -- with parameter query_data of type 'dict'
    -- with return type of 'None'

- When create_product() method is called with incorrect product_data
  it should raise ValueError.
- When create_product() method is called with correct product_data
  it should call create() method of 'sql_service'.
- create_product() method should raise SQLException if create() method
  of 'sql_service' raises SQLException.
- create_product() method should return Product if create() method
  of 'sql_service' return None.
- create_product() method should return correct Product.

- When get_product() method is called with incorrect query_data
  it should raise TypeError.
- When get_product() method is called with correct query_data
  it should call read_single() method of 'sql_service'.
- get_product() method should raise SQLException if read_single() method
  of 'sql_service' raises SQLException.
- get_product() method should return None if read_single() method
  of 'sql_service' returns None.
- get_product() method should return the Product if read_single() method
  of 'sql_service' returns a Product.

- When get_products() method is called with incorrect query_data
  it should raise TypeError.
- When get_products() method is called with correct query_data
  it should call read_multiple() method of 'sql_service'.
- get_products() method should raise SQLException if read_multiple() method
  of 'sql_service' raises SQLException.
- get_products() method should return [] if read_multiple() method
  of 'sql_service' returns [].
- get_products() method should return the list[Product] if read_multiple()
  method of 'sql_service' returns a list[Product].

- When update_product() method is called with incorrect updated_product
  it should raise TypeError.
- When update_product() method is called with correct updated_product
  it should call update() method of 'sql_service'.
- update_product() method should raise SQLException if update() method
  of 'sql_service' raises SQLException.
- update_product() method should return None if update() method
  of 'sql_service' returns None.

- When delete_product() method is called with incorrect query_data
  it should raise TypeError.
- When delete_product() method is called with correct query_data
  it should call delete() method of 'sql_service'.
- delete_product() method should raise SQLException if delete() method
  of 'sql_service' raises SQLException.
- delete_product() method should return None if delete() method
  of 'sql_service' returns None.
"""


import inspect
import pytest
from unittest.mock import Mock
from core.services.sql_service.sql_exception import SQLException
from core.services.sql_service.sql_service import SQLService
from features.product.models.product import Product
from features.product.usecases.product_crud_usecase import ProductCrudUsecase


def test_sql_service_dependency():
    """Raises Exception if sql_service not provided
    in constructor."""

    # verify TypeError raised
    with pytest.raises(TypeError) as exc_info:
        ProductCrudUsecase()  # type: ignore

    # verify error message
    assert (
        "ProductCrudUsecase.__init__() missing 1 required positional argument: 'sql_service'"  # noqa: E501
        in str(exc_info.value)
    )


def test_sql_service_incorrect():
    """Raises Exception if incorrect object is provided
    for sql_service."""

    # verify TypeError raised
    with pytest.raises(TypeError) as exc_info:
        ProductCrudUsecase("abcd")  # type: ignore

    # verify error message
    assert "'sql_service' should be of type 'SQLService'" in str(  # noqa: E501
        exc_info.value
    )


def test_sql_service_private_instance():
    """Private instance should be created for sql_service."""

    # verify __sql_service is not present
    assert not hasattr(ProductCrudUsecase, "_ProductCrudUsecase__sql_service")

    # create mock sql service
    mock = Mock(spec=SQLService)
    # create usecase
    usecase = ProductCrudUsecase(mock)

    # verify __sql_service is present
    assert hasattr(usecase, "_ProductCrudUsecase__sql_service")


def test_create_product_present():
    """ProductCrudUsecase has a create_product() method with parameters:
    product_data: dict
    and return type of 'Product'.
    """

    # verify create product method
    create_method = getattr(ProductCrudUsecase, "create_product", None)
    assert create_method is not None

    # verify product_data parameter
    signature = inspect.signature(create_method)
    assert "product_data" in signature.parameters

    # verify product_data type
    assert signature.parameters["product_data"].annotation is dict

    # verify method return type
    signature = inspect.signature(create_method)
    assert signature.return_annotation is Product


def test_get_product_present():
    """ProductCrudUsecase has a get_product() method with parameters:
    query_data: dict
    and return type of 'Product | None'.
    """

    # verify get product method
    get_method = getattr(ProductCrudUsecase, "get_product", None)
    assert get_method is not None

    # verify product_data parameter
    signature = inspect.signature(get_method)
    assert "query_data" in signature.parameters

    # verify product_data type
    assert signature.parameters["query_data"].annotation is dict

    # verify method return type
    signature = inspect.signature(get_method)
    assert str(signature.return_annotation).endswith("Product | None")


def test_get_products_present():
    """ProductCrudUsecase has a get_products() method with parameters:
    query_data: dict
    and return type of list[Product].
    """

    # verify get product method
    get_method = getattr(ProductCrudUsecase, "get_products", None)
    assert get_method is not None

    # verify product_data parameter
    signature = inspect.signature(get_method)
    assert "query_data" in signature.parameters

    # verify product_data type
    assert signature.parameters["query_data"].annotation is dict

    # verify method return type
    signature = inspect.signature(get_method)
    assert (
        str(signature.return_annotation)
        == "list[features.product.models.product.Product]"
    )


def test_update_product_present():
    """ProductCrudUsecase has a update_product() method with parameters:
    updated_product: Product
    and return type of None.
    """

    # verify update product method
    update_method = getattr(ProductCrudUsecase, "update_product", None)
    assert update_method is not None

    # verify updated_product parameter
    signature = inspect.signature(update_method)
    assert "updated_product" in signature.parameters

    # verify product_data type
    assert signature.parameters["updated_product"].annotation is Product

    # verify method return type
    signature = inspect.signature(update_method)
    assert signature.return_annotation is None


def test_delete_product_present():
    """ProductCrudUsecase has a delete_product() method with parameters:
    query_data: dict
    and return type of None.
    """

    # verify delete product method
    delete_method = getattr(ProductCrudUsecase, "delete_product", None)
    assert delete_method is not None

    # verify query_data parameter
    signature = inspect.signature(delete_method)
    assert "query_data" in signature.parameters

    # verify product_data type
    assert signature.parameters["query_data"].annotation is dict

    # verify method return type
    signature = inspect.signature(delete_method)
    assert signature.return_annotation is None


def test_create_product_incorrect_data():
    """When create_product() method is called with incorrect product_data
    it should raise ValueError."""

    # create mock sql service
    mock = Mock(spec=SQLService)
    # create product crud usecase
    product_crud_usecase = ProductCrudUsecase(mock)

    # verify ValueError raised
    with pytest.raises(ValueError):
        product_crud_usecase.create_product({})


def test_create_product_sql_service_create():
    """When create_product() method is called with correct product_data
    it should call create() method of 'sql_service'."""

    # create mock sql service
    mock = Mock(spec=SQLService)
    # create product crud usecase
    product_crud_usecase = ProductCrudUsecase(mock)

    # call create_product with correct data
    product_crud_usecase.create_product(
        {
            "id": 1,
            "name": "banana",
            "price": 5.99,
        }
    )

    # verify create method called once
    mock.create.assert_called_once()


def test_create_product_sql_exception():
    """create_product() method should raise SQLException if create() method
    of 'sql_service' raises SQLException."""

    # create mock sql service
    mock = Mock(spec=SQLService)
    # create product crud usecase
    product_crud_usecase = ProductCrudUsecase(mock)

    # create a dummy exception
    dummy_exception = SQLException("Some database exception")

    # raise exception when create method called
    mock.create.side_effect = dummy_exception

    # verify SQLException raised
    with pytest.raises(SQLException) as exc_info:
        # call create_product with correct data
        product_crud_usecase.create_product(
            {
                "id": 1,
                "name": "banana",
                "price": 5.99,
            }
        )

    # verify exception
    assert exc_info.value == dummy_exception


def test_create_product_return_product():
    """create_product() method should return Product if create() method
    of 'sql_service' return None."""

    # create mock sql service
    mock = Mock(spec=SQLService)
    # create product crud usecase
    product_crud_usecase = ProductCrudUsecase(mock)

    # return None when create method called
    mock.create.return_value = None

    # call create_product with correct data
    result = product_crud_usecase.create_product(
        {
            "id": 1,
            "name": "banana",
            "price": 5.99,
        }
    )

    # verify result
    assert type(result) is Product


def test_create_product_return_correct_product():
    """create_product() method should return correct Product."""

    # create mock sql service
    mock = Mock(spec=SQLService)
    # create product crud usecase
    product_crud_usecase = ProductCrudUsecase(mock)

    # return None when create method called
    mock.create.return_value = None

    # call create_product with correct data
    result = product_crud_usecase.create_product(
        {
            "id": 1,
            "name": "banana",
            "price": 5.99,
        }
    )

    # verify product data
    assert result.id == 1
    assert result.name == "banana"
    assert result.price == 5.99


# constant error message
QUERY_DATA_VALID_DICT = "'query_data' should be a valid dict."


def test_get_product_incorrect_data():
    """When get_product() method is called with incorrect query_data
    it should raise ValueError."""

    # create mock sql service
    mock = Mock(spec=SQLService)
    # create product crud usecase
    product_crud_usecase = ProductCrudUsecase(mock)

    # verify TypeError raised
    with pytest.raises(TypeError) as exc_info:
        product_crud_usecase.get_product("get")  # type: ignore

    # verify error message
    assert QUERY_DATA_VALID_DICT in str(exc_info.value)


def test_get_product_sql_service_read():
    """When get_product() method is called with correct query_data
    it should call read_single() method of 'sql_service'."""

    # create mock sql service
    mock = Mock(spec=SQLService)
    # create product crud usecase
    product_crud_usecase = ProductCrudUsecase(mock)

    # call get_product with correct data
    product_crud_usecase.get_product({"name": "banana"})

    # verify read_single method called once
    mock.read_single.assert_called_once_with({"name": "banana"})


def test_get_product_sql_exception():
    """get_product() method should raise SQLException if read_single() method
    of 'sql_service' raises SQLException."""

    # create mock sql service
    mock = Mock(spec=SQLService)
    # create product crud usecase
    product_crud_usecase = ProductCrudUsecase(mock)

    # create a dummy exception
    dummy_exception = SQLException("Some database exception")

    # raise exception when read_single method called
    mock.read_single.side_effect = dummy_exception

    # verify SQLException raised
    with pytest.raises(SQLException) as exc_info:
        # call get_product with correct data
        product_crud_usecase.get_product({"name": "banana"})

    # verify exception
    assert exc_info.value == dummy_exception


def test_get_product_return_none():
    """get_product() method should return None if read_single() method
    of 'sql_service' returns None."""

    # create mock sql service
    mock = Mock(spec=SQLService)
    # create product crud usecase
    product_crud_usecase = ProductCrudUsecase(mock)

    # return None when read_single method called
    mock.read_single.return_value = None

    # call get_product with correct data
    result = product_crud_usecase.get_product({"name": "banana"})

    # verify result
    assert result is None


def test_get_product_return_product():
    """get_product() method should return the Product if read_single() method
    of 'sql_service' returns a Product."""

    # create mock sql service
    mock = Mock(spec=SQLService)
    # create product crud usecase
    product_crud_usecase = ProductCrudUsecase(mock)

    # create product
    product = Product(id=1, name="banana", price=4.99)

    # return product when read_single method called
    mock.read_single.return_value = product

    # call get_product with correct data
    result = product_crud_usecase.get_product({"name": "banana"})

    # verify result
    assert result is product
    # verify product
    assert product.id == 1
    assert product.name == "banana"
    assert product.price == 4.99


def test_get_products_incorrect_data():
    """When get_products() method is called with incorrect query_data
    it should raise ValueError."""

    # create mock sql service
    mock = Mock(spec=SQLService)
    # create product crud usecase
    product_crud_usecase = ProductCrudUsecase(mock)

    # verify TypeError raised
    with pytest.raises(TypeError) as exc_info:
        product_crud_usecase.get_products("get")  # type: ignore

    # verify error message
    assert QUERY_DATA_VALID_DICT in str(exc_info.value)


def test_get_products_sql_service_read():
    """When get_products() method is called with correct query_data
    it should call read_multiple() method of 'sql_service'."""

    # create mock sql service
    mock = Mock(spec=SQLService)
    # create product crud usecase
    product_crud_usecase = ProductCrudUsecase(mock)

    # call get_products with correct data
    product_crud_usecase.get_products({"name": "banana"})

    # verify read_multiple method called once
    mock.read_multiple.assert_called_once_with({"name": "banana"})


def test_get_products_sql_exception():
    """get_products() method should raise SQLException if read_multiple()
    method of 'sql_service' raises SQLException."""

    # create mock sql service
    mock = Mock(spec=SQLService)
    # create product crud usecase
    product_crud_usecase = ProductCrudUsecase(mock)

    # create a dummy exception
    dummy_exception = SQLException("Some database exception")

    # raise exception when read_multiple method called
    mock.read_multiple.side_effect = dummy_exception

    # verify SQLException raised
    with pytest.raises(SQLException) as exc_info:
        # call get_products with correct data
        product_crud_usecase.get_products({"name": "banana"})

    # verify exception
    assert exc_info.value == dummy_exception


def test_get_products_return_empty():
    """get_products() method should return None if read_multiple() method
    of 'sql_service' returns None."""

    # create mock sql service
    mock = Mock(spec=SQLService)
    # create product crud usecase
    product_crud_usecase = ProductCrudUsecase(mock)

    # return [] when read_multiple method called
    mock.read_multiple.return_value = []

    # call get_products with correct data
    result = product_crud_usecase.get_products({"name": "banana"})

    # verify result
    assert result == []


def test_get_products_return_products():
    """get_products() method should return the Product if read_multiple()
    method of 'sql_service' returns a Product."""

    # create mock sql service
    mock = Mock(spec=SQLService)
    # create product crud usecase
    product_crud_usecase = ProductCrudUsecase(mock)

    # create products
    product_1 = Product(id=1, name="banana", price=4.99)
    product_2 = Product(id=2, name="apple", price=6.99)

    # return product when read_multiple method called
    mock.read_multiple.return_value = [product_1, product_2]

    # call get_products with correct data
    result = product_crud_usecase.get_products({"name": "banana"})

    # verify result type
    assert isinstance(result, list)
    # verify result
    assert result == [product_1, product_2]


def test_update_product_incorrect_data():
    """When update_product() method is called with incorrect updated_product
    it should raise TypeError."""

    # create mock sql service
    mock = Mock(spec=SQLService)
    # create product crud usecase
    product_crud_usecase = ProductCrudUsecase(mock)

    # verify TypeError raised
    with pytest.raises(TypeError) as exc_info:
        product_crud_usecase.update_product([])  # type: ignore

    # verify error message
    assert "'updated_product' should be a valid model." in str(exc_info.value)


def test_update_product_sql_service_update():
    """When update_product() method is called with correct updated_product
    it should call update() method of 'sql_service'."""

    # create mock sql service
    mock = Mock(spec=SQLService)
    # create product crud usecase
    product_crud_usecase = ProductCrudUsecase(mock)

    # create product
    product = Product(id=1, name="banana", price=4.99)

    # call update_product with correct data
    product_crud_usecase.update_product(product)

    # verify update method called once
    mock.update.assert_called_once_with(product)


def test_update_product_sql_exception():
    """update_product() method should raise SQLException if update() method
    of 'sql_service' raises SQLException."""

    # create mock sql service
    mock = Mock(spec=SQLService)
    # create product crud usecase
    product_crud_usecase = ProductCrudUsecase(mock)

    # create a dummy exception
    dummy_exception = SQLException("Some database exception")

    # raise exception when update method called
    mock.update.side_effect = dummy_exception

    # create product
    product = Product(id=1, name="banana", price=4.99)

    # verify SQLException raised
    with pytest.raises(SQLException) as exc_info:
        # call update_product with correct data
        product_crud_usecase.update_product(product)

    # verify exception
    assert exc_info.value == dummy_exception


def test_update_product_return_none():
    """update_product() method should return None if update() method
    of 'sql_service' returns None."""

    # create mock sql service
    mock = Mock(spec=SQLService)
    # create product crud usecase
    product_crud_usecase = ProductCrudUsecase(mock)

    # return None when update method called
    mock.update.return_value = None

    # create product
    product = Product(id=1, name="banana", price=4.99)

    # call update_product with correct data
    result = product_crud_usecase.update_product(product)

    # verify result
    assert result is None


def test_delete_product_incorrect_data():
    """When delete_product() method is called with incorrect query_data
    it should raise TypeError."""

    # create mock sql service
    mock = Mock(spec=SQLService)
    # create product crud usecase
    product_crud_usecase = ProductCrudUsecase(mock)

    # verify TypeError raised
    with pytest.raises(TypeError) as exc_info:
        product_crud_usecase.delete_product(-99)  # type: ignore

    # verify error message
    assert QUERY_DATA_VALID_DICT in str(exc_info.value)


def test_delete_product_sql_service_update():
    """When delete_product() method is called with correct query_data
    it should call delete() method of 'sql_service'."""

    # create mock sql service
    mock = Mock(spec=SQLService)
    # create product crud usecase
    product_crud_usecase = ProductCrudUsecase(mock)

    # call delete_product with correct data
    product_crud_usecase.delete_product({"name": "apple"})

    # verify delete method called once
    mock.delete.assert_called_once_with({"name": "apple"})


def test_delete_product_sql_exception():
    """delete_product() method should raise SQLException if delete() method
    of 'sql_service' raises SQLException."""

    # create mock sql service
    mock = Mock(spec=SQLService)
    # create product crud usecase
    product_crud_usecase = ProductCrudUsecase(mock)

    # create a dummy exception
    dummy_exception = SQLException("Some database exception")

    # raise exception when delete method called
    mock.delete.side_effect = dummy_exception

    # verify SQLException raised
    with pytest.raises(SQLException) as exc_info:
        # call delete_product with correct data
        product_crud_usecase.delete_product({"name": "apple"})

    # verify exception
    assert exc_info.value == dummy_exception


def test_delete_product_return_none():
    """delete_product() method should return None if delete() method
    of 'sql_service' returns None."""

    # create mock sql service
    mock = Mock(spec=SQLService)
    # create product crud usecase
    product_crud_usecase = ProductCrudUsecase(mock)

    # return None when delete method called
    mock.delete.return_value = None

    # call delete_product with correct data
    result = product_crud_usecase.delete_product({"name": "apple"})

    # verify result
    assert result is None
