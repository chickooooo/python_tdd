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

- create() method should raise TypeError if 'record' is
  not a valid model object.
- create() method should raise SQLException if 'record' with 'id'
  is already present in database.
- create() method should insert record in database if 'record' with 'id'
  is not present in database.
- create() method should return None after insertion.

- read_single() method should raise TypeError if 'query_data' is
  not of type dict.
- read_single() method should return None if no record found
  matching the 'query_data'.
- read_single() method should return object 'T' if record
  found in the database.
- read_single() method should return first record found
  in the database.

- read_multiple() method should raise TypeError if 'query_data' is
  not of type dict.
- read_multiple() method should return '[]' if no record found
  matching the 'query_data'.
- read_multiple() method should return list of object 'T' if records
  found in the database.

- update() method should raise TypeError if 'updated_record' is
  not a valid model object.
- update() method should update nothing in database if record with
  'query_data' is not present in database.
- update() method should update record in database with
  'updated_record'.
- update() method should return None after successful updation.

- delete() method should raise TypeError if 'query_data' is
  not of type dict.
- delete() method should delete nothing from database if record with
  'query_data' is not present in database.
- delete() method should delete records from database if records with
  'query_data' are present in database.
- delete() method should return None after successful deletion.
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
    updated_record: T
    and return type of 'None'.
    """

    # verify update method
    update_method = getattr(MySQLService, "update", None)
    assert update_method is not None

    # verify parameters
    signature = inspect.signature(update_method)
    assert "updated_record" in signature.parameters

    # verify parameter types
    assert str(signature.parameters["updated_record"].annotation) == "T"

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

    # add a record in database
    DATABASE.append({"id": 1, "name": "orange", "price": 4.99})

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

    # remove record from database
    DATABASE.pop()


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

    # remove record from database
    DATABASE.pop()


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

    # remove record from database
    DATABASE.pop()


def test_read_single_invalid_data():
    """read_single() method should raise TypeError if 'query_data' is
    not of type dict."""

    # verify TypeError raised
    with pytest.raises(TypeError) as exc_info:
        sql_service.read_single("str")  # type: ignore

    # verify error message
    assert "'query_data' should be a valid dict." in str(exc_info.value)


def test_read_single_return_none():
    """read_single() method should return None if no record found
    matching the 'query_data'."""

    # add a record in database
    DATABASE.append({"id": 1, "name": "orange", "price": 4.99})

    # read product from database
    result = sql_service.read_single(
        query_data={
            "name": "banana",
        }
    )

    # verify result
    assert result is None

    # remove record from database
    DATABASE.pop()


def test_read_single_return_object():
    """read_single() method should return object 'T' if record
    found in the database."""

    # add a record in database
    DATABASE.append({"id": 1, "name": "orange", "price": 4.99})

    # read product from database
    result = sql_service.read_single(
        query_data={
            "name": "orange",
        }
    )

    # verify result type
    assert isinstance(result, Product)
    # verify result data
    assert result.id == 1
    assert result.name == "orange"
    assert result.price == 4.99

    # remove record from database
    DATABASE.pop()


def test_read_single_return_first_object():
    """read_single() method should return first record found
    in the database."""

    # add a records in database
    DATABASE.append({"id": 10, "name": "orange", "price": 4.99})
    DATABASE.append({"id": 20, "name": "orange", "price": 4.99})

    # read product from database
    result = sql_service.read_single(
        query_data={
            "name": "orange",
            "price": 4.99,
        }
    )

    # verify result type
    assert isinstance(result, Product)
    # verify result data
    assert result.id == 10
    assert result.name == "orange"
    assert result.price == 4.99

    # remove record from database
    DATABASE.pop()
    DATABASE.pop()


def test_read_multiple_invalid_data():
    """read_multiple() method should raise TypeError if 'query_data' is
    not of type dict."""

    # verify TypeError raised
    with pytest.raises(TypeError) as exc_info:
        sql_service.read_multiple(1234)  # type: ignore

    # verify error message
    assert "'query_data' should be a valid dict." in str(exc_info.value)


def test_read_multiple_return_empty_list():
    """read_multiple() method should return '[]' if no record found
    matching the 'query_data'."""

    # add a record in database
    DATABASE.append({"id": 1, "name": "orange", "price": 4.99})

    # read product from database
    result = sql_service.read_multiple(
        query_data={
            "name": "banana",
        }
    )

    # verify result
    assert result == []

    # remove record from database
    DATABASE.pop()


def test_read_multiple_return_object_list():
    """read_multiple() method should return list of object 'T' if records
    found in the database."""

    # create 2 records
    item_1: dict = {"id": 10, "name": "orange", "price": 4.99}
    item_2: dict = {"id": 20, "name": "orange", "price": 4.99}

    # add a records in database
    DATABASE.append(item_1)
    DATABASE.append(item_2)

    # read products from database
    result = sql_service.read_multiple(
        query_data={
            "name": "orange",
            "price": 4.99,
        }
    )

    # verify result type
    assert isinstance(result, list)
    # verify result length
    assert len(result) == 2

    # verify objects type
    assert isinstance(result[0], Product)
    assert isinstance(result[1], Product)
    # verify objects data
    assert result[0].model_dump() == item_1
    assert result[1].model_dump() == item_2

    # remove record from database
    DATABASE.pop()
    DATABASE.pop()


def test_update_invalid_data():
    """update() method should raise TypeError if 'updated_record' is
    not a valid model object."""

    # verify TypeError raised
    with pytest.raises(TypeError) as exc_info:
        sql_service.update({})  # type: ignore

    # verify error message
    assert "'updated_record' should be a valid model." in str(exc_info.value)


def test_update_nothing():
    """update() method should update nothing in database if record with
    'query_data' is not present in database."""

    # add a record in database
    DATABASE.append({"id": 1, "name": "orange", "price": 4.99})

    # create product object
    product = Product(
        id=2,
        name="banana",
        price=10.99,
    )

    # update product in database
    sql_service.update(product)

    # verify database
    assert DATABASE == [{"id": 1, "name": "orange", "price": 4.99}]

    # remove record from database
    DATABASE.pop()


def test_update_record():
    """update() method should update record in database if record with
    'query_data' is present in database."""

    # add records in database
    DATABASE.append({"id": 1, "name": "orange", "price": 4.99})
    DATABASE.append({"id": 2, "name": "banana", "price": 6.99})

    # create product object
    product = Product(
        id=1,
        name="orange",
        price=10.99,
    )

    # update product in database
    sql_service.update(product)

    # verify database
    assert DATABASE == [
        {"id": 1, "name": "orange", "price": 10.99},
        {"id": 2, "name": "banana", "price": 6.99},
    ]

    # remove records from database
    DATABASE.pop()
    DATABASE.pop()


def test_update_return_none():
    """update() method should return None after successful updation."""

    # add a record in database
    DATABASE.append({"id": 1, "name": "orange", "price": 4.99})

    # create product object
    product = Product(
        id=1,
        name="orange",
        price=10.99,
    )

    # update product in database
    result = sql_service.update(product)

    # verify result
    assert result is None

    # remove record from database
    DATABASE.pop()


def test_delete_invalid_data():
    """delete() method should raise TypeError if 'query_data' is
    not of type dict."""

    # verify TypeError raised
    with pytest.raises(TypeError) as exc_info:
        sql_service.delete(True)  # type: ignore

    # verify error message
    assert "'query_data' should be a valid dict." in str(exc_info.value)


def test_delete_nothing():
    """delete() method should delete nothing from database if record with
    'query_data' is not present in database."""

    # add a record in database
    DATABASE.append({"id": 1, "name": "orange", "price": 4.99})

    # delete records from database
    sql_service.delete({"id": 2})

    # verify database
    assert DATABASE == [{"id": 1, "name": "orange", "price": 4.99}]

    # remove record from database
    DATABASE.pop()


def test_delete_record():
    """delete() method should delete records from database if records with
    'query_data' are present in database."""

    # add records in database
    DATABASE.append({"id": 1, "name": "orange", "price": 4.99})
    DATABASE.append({"id": 2, "name": "banana", "price": 6.99})
    DATABASE.append({"id": 3, "name": "papaya", "price": 4.99})
    DATABASE.append({"id": 4, "name": "melon", "price": 4.99})
    DATABASE.append({"id": 5, "name": "apple", "price": 7.99})

    # delete records from database
    sql_service.delete({"price": 4.99})

    # verify database
    assert DATABASE == [
        {"id": 2, "name": "banana", "price": 6.99},
        {"id": 5, "name": "apple", "price": 7.99},
    ]

    # remove records from database
    DATABASE.pop()
    DATABASE.pop()


def test_delete_return_none():
    """delete() method should return None after successful deletion."""

    # add a record in database
    DATABASE.append({"id": 1, "name": "orange", "price": 4.99})

    # delete records from database
    result = sql_service.delete({"id": 1})

    # verify result
    assert result is None
