"""Test Cases

- ProductCrudUsecase depends on SQLService
    -- no object provided
    -- incorrect object provided
    -- correct object provided and private instance created

- ProductCrudUsecase has a create_product() method
    -- with parameter product_data of type 'dict'
    -- with return type of 'Product'

- When create_product() method is called with incorrect product_data
  it should raise ValueError.
- When create_product() method is called with correct product_data
  it should call create() method of 'sql_service'.
- create_product() method should raise SQLException if create() method
  of 'sql_service' raises SQLException.
- create_product() method should return Product if create() method
  of 'sql_service' return None.
- create_product() method should return correct Product.
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
