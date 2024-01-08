"""Test Cases

- SQLService shouid be an abstract class

- SQLService should have a create() method
- create() method should have parameter 'record' of type 'T'
- create() method should have return type of 'None'

- SQLService should have a read_single() method
    -- with parameter query_data of type 'dict'
    -- with return type of 'T | None'

- SQLService should have a read_multiple() method
    -- with parameter query_data of type 'dict'
    -- with return type of 'list[T]'

- SQLService should have a update() method
    -- with parameter query_data of type 'dict'
    -- with parameter updated_data of type 'dict'
    -- with return type of 'None'

- SQLService should have a delete() method
    -- with parameter query_data of type 'dict'
    -- with return type of 'None'
"""


import inspect
from abc import ABCMeta
from core.services.sql_service.sql_service import SQLService


def test_abstract_class():
    """SQLService is an abstract class."""

    # verify abstract class
    assert isinstance(SQLService, ABCMeta)


def test_create_method():
    """SQLService has a create method."""

    # verify create method
    assert hasattr(SQLService, "create")
    assert callable(getattr(SQLService, "create", None))


def test_create_method_params():
    """Create method takes a paramater called 'record'
    of type 'T'."""

    # verify create method
    create_method = getattr(SQLService, "create", None)
    assert create_method is not None

    # verify record parameter
    signature = inspect.signature(create_method)
    assert "record" in signature.parameters

    # verify record type
    assert str(signature.parameters["record"].annotation) == "T"


def test_create_method_return_type():
    """Create method has a return type of 'None'."""

    # verify create method
    create_method = getattr(SQLService, "create", None)
    assert create_method is not None

    # verify return type
    signature = inspect.signature(create_method)
    assert signature.return_annotation is None


def test_read_single_method():
    """SQLService has a read_single() method with parameters:
    query_data: dict
    and return type of 'T | None'.
    """

    # verify read single method
    read_method = getattr(SQLService, "read_single", None)
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
    """SQLService has a read_multiple() method with parameters:
    query_data: dict
    and return type of 'list[T]'.
    """

    # verify read multiple method
    read_method = getattr(SQLService, "read_multiple", None)
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
    """SQLService has an update() method with parameters:
    query_data: dict
    updated_record: dict
    and return type of 'None'.
    """

    # verify update method
    update_method = getattr(SQLService, "update", None)
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
    """SQLService has an delete() method with parameters:
    query_data: dict
    and return type of 'None'.
    """

    # verify delete method
    delete_method = getattr(SQLService, "delete", None)
    assert delete_method is not None

    # verify parameters
    signature = inspect.signature(delete_method)
    assert "query_data" in signature.parameters

    # verify parameter types
    assert signature.parameters["query_data"].annotation is dict

    # verify method return type
    signature = inspect.signature(delete_method)
    assert signature.return_annotation is None
