"""Test Cases

- SQLException is of type Exception
- SQLException shows correct message

"""


import pytest
from core.services.sql_service.sql_exception import SQLException


def test_sql_exception_type():
    """SQLException is of type Exception."""

    # verify Exception raised
    with pytest.raises(Exception):
        raise SQLException()


def test_sql_exception_message():
    """SQLException should show correct message."""

    # verify Exception raised
    with pytest.raises(Exception) as exc_info:
        raise SQLException("This is custom error message")

    # verify error message
    assert "This is custom error message" in str(exc_info.value)
