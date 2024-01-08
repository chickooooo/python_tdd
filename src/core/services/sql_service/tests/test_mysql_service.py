"""Test Cases

- MySQLService shouid be of type SQLService

- MySQLService should have a create() method
    -- with parameter record of type 'T'
    -- with return type of 'None'

- MySQLService should have a read_single() method
    -- with parameter query_data of type 'dict'
    -- with return type of 'T | None'

- MySQLService should have a read_multiple() method
    -- with parameter query_data of type 'dict'
    -- with return type of 'list[T]'

- MySQLService should have a update() method
    -- with parameter query_data of type 'dict'
    -- with parameter updated_data of type 'dict'
    -- with return type of 'None'

- MySQLService should have a delete() method
    -- with parameter query_data of type 'dict'
    -- with return type of 'None'

- MySQLService methods are not implemented

- create() method should raise TypeError if record is
  not a valid model object.
- create() method should raise SQLException if record with 'id'
  is already present in database.
- create() method should insert record in database if record with 'id'
  is not present in database.
- create() method should return None after insertion.
"""


import inspect
import pytest
from core.services.sql_service.sql_exception import SQLException
from core.services.sql_service.sql_service import SQLService
from core.services.sql_service.mysql_service import MySQLService, DATABASE
from features.product.models.product import Product


def test_mysql_service_type():
    """MySQLService is of type SQLService."""

    # verify type
    assert isinstance(MySQLService(), SQLService)


def test_create_method():
    """MySQLService has an create() method with parameters:
    record: T
    and return type of 'None'.
    """

    # verify create method
    create_method = getattr(MySQLService, "create", None)
    assert create_method is not None

    # verify parameters
    signature = inspect.signature(create_method)
    assert "record" in signature.parameters

    # verify parameter types
    assert str(signature.parameters["record"].annotation) == "T"

    # verify method return type
    signature = inspect.signature(create_method)
    assert signature.return_annotation is None


def test_read_single_method():
    """MySQLService has a read_single() method with parameters:
    query_data: dict
    and return type of 'T | None'.
    """

    # verify read single method
    read_method = getattr(MySQLService, "read_single", None)
    assert read_method is not None

    # verify query_data parameter
    signature = inspect.signature(read_method)
    assert "query_data" in signature.parameters

    # verify query_data type
    assert signature.parameters["query_data"].annotation is dict

    # verify method return type
    signature = inspect.signature(read_method)
    assert str(signature.return_annotation) == "typing.Optional[T]"


def test_read_multiple_method():
    """MySQLService has a read_multiple() method with parameters:
    query_data: dict
    and return type of 'list[T]'.
    """

    # verify read multiple method
    read_method = getattr(MySQLService, "read_multiple", None)
    assert read_method is not None

    # verify query_data parameter
    signature = inspect.signature(read_method)
    assert "query_data" in signature.parameters

    # verify query_data type
    assert signature.parameters["query_data"].annotation is dict

    # verify method return type
    signature = inspect.signature(read_method)
    assert str(signature.return_annotation) == "list[T]"


def test_update_method():
    """MySQLService has an update() method with parameters:
    query_data: dict
    updated_data: dict
    and return type of 'None'.
    """

    # verify update method
    update_method = getattr(MySQLService, "update", None)
    assert update_method is not None

    # verify parameters
    signature = inspect.signature(update_method)
    assert "query_data" in signature.parameters
    assert "updated_data" in signature.parameters

    # verify parameter types
    assert signature.parameters["query_data"].annotation is dict
    assert signature.parameters["updated_data"].annotation is dict

    # verify method return type
    signature = inspect.signature(update_method)
    assert signature.return_annotation is None


def test_delete_method():
    """MySQLService has an delete() method with parameters:
    query_data: dict
    and return type of 'None'.
    """

    # verify delete method
    delete_method = getattr(MySQLService, "delete", None)
    assert delete_method is not None

    # verify parameters
    signature = inspect.signature(delete_method)
    assert "query_data" in signature.parameters

    # verify parameter types
    assert signature.parameters["query_data"].annotation is dict

    # verify method return type
    signature = inspect.signature(delete_method)
    assert signature.return_annotation is None


def test_not_implemented():
    """Raise NotImplementedError on all methods of MySQLService."""

    # exception message
    EXC_MESSAGE: str = "Method hasn't been implemented yet."

    # verify exception raised for read_single method
    with pytest.raises(NotImplementedError) as exc_info:
        MySQLService().read_single({})
    # verify error message
    assert EXC_MESSAGE == str(exc_info.value)

    # verify exception raised for read_multiple method
    with pytest.raises(NotImplementedError) as exc_info:
        MySQLService().read_multiple({})
    # verify error message
    assert EXC_MESSAGE == str(exc_info.value)

    # verify exception raised for update method
    with pytest.raises(NotImplementedError) as exc_info:
        MySQLService().update({}, {})
    # verify error message
    assert EXC_MESSAGE == str(exc_info.value)

    # verify exception raised for delete method
    with pytest.raises(NotImplementedError) as exc_info:
        MySQLService().delete({})
    # verify error message
    assert EXC_MESSAGE == str(exc_info.value)


# sql service object
sql_service = MySQLService[Product]()


def test_create_invalid_record():
    """create() method should raise TypeError if record is
    not a valid model object."""

    # verify TypeError raised
    with pytest.raises(TypeError) as exc_info:
        sql_service.create("str")  # type: ignore

    # verify error message
    assert "'record' should be a valid model." in str(exc_info.value)


def test_create_duplicate_id():
    """create() method should raise SQLException if record with 'id'
    is already present in database."""

    # create product object
    product = Product(
        id=1,
        name="apple",
        price=7.99,
    )

    # verify SQLException raised
    with pytest.raises(SQLException) as exc_info:
        sql_service.create(product)

    # verify error message
    assert "duplicate id: 1" in str(exc_info.value)


def test_create_insert_database():
    """create() method should insert record in database if record with 'id'
    is not present in database."""

    # verify record not in database
    assert {"id": 2, "name": "apple", "price": 8.99} not in DATABASE

    # create product object
    product = Product(
        id=2,
        name="apple",
        price=8.99,
    )

    # add product to database
    sql_service.create(product)

    # verify record added in database
    assert {"id": 2, "name": "apple", "price": 8.99} in DATABASE


def test_create_return_none():
    """create() method should return None after insertion."""

    # create product object
    product = Product(
        id=3,
        name="papaya",
        price=12.99,
    )

    # add product to database
    result = sql_service.create(product)

    # verify result
    assert result is None
