"""Test Cases

- product should have 'id' field
- 'id' field should be of type integer

- product should have 'name' field
- 'name' field should be of type string

- product should have 'price' field
- 'price' field should be of type float

- 'id' field cannot be negative
- 'id' field cannot be zero

- 'name' field cannot be empty
- 'name' field should have atleat 5 characters
- 'name' field cannot have leading & trailing white spaces

- 'price' field cannot be negative
- 'price' field cannot be zero

- product creation successful
"""


import pytest
from pydantic import ValidationError
from features.product.models.product import Product


def test_product_without_id():
    """Raise ValidationError if product is created without 'id' field."""

    # verify ValidationError raised
    with pytest.raises(ValidationError):
        Product()  # type: ignore


def test_product_with_wrong_id_type():
    """Raise ValidationError if product is created with
    wrong type for 'id' field."""

    # verify ValidationError raised
    with pytest.raises(ValidationError):
        Product(
            id="1",
        )  # type: ignore


def test_product_without_name():
    """Raise ValidationError if product is created without 'name' field."""

    # verify ValidationError raised
    with pytest.raises(ValidationError):
        Product(
            id=1,
        )  # type: ignore


def test_product_with_wrong_name_type():
    """Raise ValidationError if product is created with
    wrong type for 'name' field."""

    # verify ValidationError raised
    with pytest.raises(ValidationError):
        Product(
            id=1,
            name=10,
        )  # type: ignore


def test_product_without_price():
    """Raise ValidationError if product is created without 'price' field."""

    # verify ValidationError raised
    with pytest.raises(ValidationError):
        Product(
            id=1,
            name="apple",
        )  # type: ignore


def test_product_with_wrong_price_type():
    """Raise ValidationError if product is created with
    wrong type for 'price' field."""

    # verify ValidationError raised
    with pytest.raises(ValidationError):
        Product(
            id=1,
            name="apple",
            price="ten",  # type: ignore
        )


def test_product_with_negative_id():
    """Raise ValidationError if product is created with
    negative value for 'id' field."""

    # verify ValidationError raised
    with pytest.raises(ValidationError) as exc_info:
        Product(
            id=-1,
            name="apple",
            price=10.50,
        )

    # verify error message
    assert "'id' must be a positive integer" in str(exc_info.value)


def test_product_with_zero_id():
    """Raise ValidationError if product is created with
    zero value for 'id' field."""

    # verify ValidationError raised
    with pytest.raises(ValidationError) as exc_info:
        Product(
            id=0,
            name="apple",
            price=10.50,
        )

    # verify error message
    assert "'id' must be a positive integer" in str(exc_info.value)


def test_product_with_empty_name():
    """Raise ValidationError if product is created with
    empty value for 'name' field."""

    # verify ValidationError raised
    with pytest.raises(ValidationError) as exc_info:
        Product(
            id=1,
            name="  ",
            price=10.50,
        )

    # verify error message
    assert "'name' cannot be empty" in str(exc_info.value)


def test_product_with_less_char_name():
    """Raise ValidationError if product is created with
    less than 5 characters value for 'name' field."""

    # verify ValidationError raised
    with pytest.raises(ValidationError) as exc_info:
        Product(
            id=1,
            name="abcd",
            price=10.50,
        )

    # verify error message
    assert "'name' should be atleat 5 characters long." in str(exc_info.value)


def test_product_with_spaced_name():
    """Remove leading & trailing white spaces in 'name' field."""

    # create product with spaced name
    product = Product(id=1, name="  apple\n", price=10.50)

    # verify name
    assert product.name == "apple"


def test_product_with_negative_price():
    """Raise ValidationError if product is created with
    negative value for 'price' field."""

    # verify ValidationError raised
    with pytest.raises(ValidationError) as exc_info:
        Product(
            id=1,
            name="apple",
            price=-10.50,
        )

    # verify error message
    assert "'price' must be a positive number" in str(exc_info.value)


def test_product_with_zero_price():
    """Raise ValidationError if product is created with
    zero value for 'price' field."""

    # verify ValidationError raised
    with pytest.raises(ValidationError) as exc_info:
        Product(
            id=1,
            name="apple",
            price=0.0,
        )

    # verify error message
    assert "'price' must be a positive number" in str(exc_info.value)


def test_product_create_success():
    """Successfully create product with given data."""

    # create product
    product = Product(id=1, name="apple", price=10.50)

    # verify id
    assert product.id == 1
    # verify name
    assert product.name == "apple"
    # verify price
    assert product.price == 10.5
