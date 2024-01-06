"""Test Cases

- ProductCrudUsecase depends on SQLService
    -- no object provided
    -- incorrect object provided
    -- correct object provided and private instance created
"""


import pytest
from unittest.mock import Mock
from core.services.sql_service.sql_service import SQLService
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
    assert (
        "'sql_service' should be of type 'SQLService'"  # noqa: E501
        in str(exc_info.value)
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
