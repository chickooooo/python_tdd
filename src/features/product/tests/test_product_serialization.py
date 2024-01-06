"""Test Cases

- serialize product to type dictionary
- serialize product to correct dictionary

- deserialize without dictionary

- deserialize from invalid dictionary (without id)
- deserialize from invalid dictionary (non int id)
- deserialize from invalid dictionary (negative id)
- deserialize from invalid dictionary (zero id)

- deserialize from invalid dictionary (without name)
- deserialize from invalid dictionary (empty name)
- deserialize from invalid dictionary (less characters name)
- deserialize from valid dictionary with leading & trailing spaces in name

- deserialize from invalid dictionary (without price)
- deserialize from invalid dictionary (non float price)
- deserialize from invalid dictionary (negative price)
- deserialize from invalid dictionary (zero price)

- deserialize correct product from valid dictionary
"""


from typing import Any

import pytest
from pydantic import ValidationError
from features.product.models.product import Product


def test_serialize_product_to_dict():
    """Return type dict on product serialization."""

    # create a valid product
    product = Product(id=1, name="apple", price=10.50)

    # serialize product
    result: dict[str, Any] = product.model_dump()

    # verify type dict
    assert type(result) is dict


def test_serialize_product_to_correct_dict():
    """Return correct dict on product serialization."""

    # create a valid product
    product = Product(id=1, name="apple", price=10.50)

    # serialize product
    result: dict[str, Any] = product.model_dump()

    # verify id
    assert result["id"] == 1
    # verify name
    assert result["name"] == "apple"
    # verify price
    assert result["price"] == 10.5


def test_deserialize_product_from_non_dict():
    """Raise ValidationError if product is not deserialized from dict."""

    # serialized product
    product_dict = "product"

    # verify ValidationError raised
    with pytest.raises(ValidationError) as exc_info:
        Product.model_validate(
            obj=product_dict,
            strict=True,
        )

    # verify error message
    assert "Input should be a valid dictionary" in str(exc_info.value)


def test_deserialize_product_without_id():
    """Raise ValidationError if product is deserialized
    without 'id' key."""

    # serialized product
    product_dict: dict = {
        "name": "apple",
        "price": 10.5,
    }

    # verify ValidationError raised
    with pytest.raises(ValidationError) as exc_info:
        Product.model_validate(
            obj=product_dict,
            strict=True,
        )

    # verify error message
    assert "id  Field required" in str(exc_info.value).replace("\n", "")


def test_deserialize_product_non_int_id():
    """Raise ValidationError if product is deserialized
    using non integer value for 'id' key."""

    # serialized product
    product_dict: dict = {
        "id": "1",
        "name": "apple",
        "price": 10.5,
    }

    # verify ValidationError raised
    with pytest.raises(ValidationError) as exc_info:
        Product.model_validate(
            obj=product_dict,
            strict=True,
        )

    # verify error message
    assert "Input should be a valid integer" in str(exc_info.value)


def test_deserialize_product_negative_id():
    """Raise ValidationError if product is deserialized
    using negative value for 'id' key."""

    # serialized product
    product_dict: dict = {
        "id": -1,
        "name": "apple",
        "price": 10.5,
    }

    # verify ValidationError raised
    with pytest.raises(ValidationError) as exc_info:
        Product.model_validate(
            obj=product_dict,
            strict=True,
        )

    # verify error message
    assert "'id' must be a positive integer" in str(exc_info.value)


def test_deserialize_product_zero_id():
    """Raise ValidationError if product is deserialized
    using zero value for 'id' key."""

    # serialized product
    product_dict: dict = {
        "id": 0,
        "name": "apple",
        "price": 10.5,
    }

    # verify ValidationError raised
    with pytest.raises(ValidationError) as exc_info:
        Product.model_validate(
            obj=product_dict,
            strict=True,
        )

    # verify error message
    assert "'id' must be a positive integer" in str(exc_info.value)


def test_deserialize_product_without_name():
    """Raise ValidationError if product is deserialized
    without 'name' key."""

    # serialized product
    product_dict: dict = {
        "id": 1,
        "price": 10.5,
    }

    # verify ValidationError raised
    with pytest.raises(ValidationError) as exc_info:
        Product.model_validate(
            obj=product_dict,
            strict=True,
        )

    # verify error message
    assert "name  Field required" in str(exc_info.value).replace("\n", "")


def test_deserialize_product_empty_name():
    """Raise ValidationError if product is deserialized
    using empty value for 'name' key."""

    # serialized product
    product_dict: dict = {
        "id": 1,
        "name": "  ",
        "price": 10.5,
    }

    # verify ValidationError raised
    with pytest.raises(ValidationError) as exc_info:
        Product.model_validate(
            obj=product_dict,
            strict=True,
        )

    # verify error message
    assert "'name' cannot be empty" in str(exc_info.value)


def test_deserialize_product_less_char_name():
    """Raise ValidationError if product is deserialized
    using less than 5 characters for 'name' key."""

    # serialized product
    product_dict: dict = {
        "id": 1,
        "name": "abcd",
        "price": 10.5,
    }

    # verify ValidationError raised
    with pytest.raises(ValidationError) as exc_info:
        Product.model_validate(
            obj=product_dict,
            strict=True,
        )

    # verify error message
    assert "'name' should be atleat 5 characters long" in str(exc_info.value)


def test_deserialize_product_spaced_name():
    """Product should have non spaced value for 'name'
    when deserialized using spaced value for 'name' key."""

    # serialized product
    product_dict: dict = {
        "id": 1,
        "name": "  apple\n",
        "price": 10.5,
    }

    # create product object
    product = Product.model_validate(
        obj=product_dict,
        strict=True,
    )

    # verify non spaced name
    assert product.name == "apple"


def test_deserialize_product_without_price():
    """Raise ValidationError if product is deserialized
    without 'price' key."""

    # serialized product
    product_dict: dict = {
        "id": 1,
        "name": "apple",
    }

    # verify ValidationError raised
    with pytest.raises(ValidationError) as exc_info:
        Product.model_validate(
            obj=product_dict,
            strict=True,
        )

    # verify error message
    assert "price  Field required" in str(exc_info.value).replace("\n", "")


def test_deserialize_product_non_float_price():
    """Raise ValidationError if product is deserialized
    using non float value for 'price' key."""

    # serialized product
    product_dict: dict = {
        "id": 1,
        "name": "apple",
        "price": "10.5",
    }

    # verify ValidationError raised
    with pytest.raises(ValidationError) as exc_info:
        Product.model_validate(
            obj=product_dict,
            strict=True,
        )

    # verify error message
    assert "Input should be a valid number" in str(exc_info.value)


def test_deserialize_product_negative_price():
    """Raise ValidationError if product is deserialized
    using negative value for 'price' key."""

    # serialized product
    product_dict: dict = {
        "id": 1,
        "name": "apple",
        "price": -10.5,
    }

    # verify ValidationError raised
    with pytest.raises(ValidationError) as exc_info:
        Product.model_validate(
            obj=product_dict,
            strict=True,
        )

    # verify error message
    assert "'price' must be a positive number" in str(exc_info.value)


def test_deserialize_product_zero_price():
    """Raise ValidationError if product is deserialized
    using zero value for 'price' key."""

    # serialized product
    product_dict: dict = {
        "id": 1,
        "name": "apple",
        "price": 0.0,
    }

    # verify ValidationError raised
    with pytest.raises(ValidationError) as exc_info:
        Product.model_validate(
            obj=product_dict,
            strict=True,
        )

    # verify error message
    assert "'price' must be a positive number" in str(exc_info.value)


def test_deserialize_product_from_correct_dict():
    """Return correct product object from valid dict."""

    # serialized product
    product_dict: dict = {
        "id": 5,
        "name": "orange",
        "price": 50.50,
    }

    # deserialize product dict
    product = Product.model_validate(
        obj=product_dict,
        strict=True,
    )

    # verify product type
    assert type(product) is Product
    # verify id
    assert product.id == 5
    # verify name
    assert product.name == "orange"
    # verify price
    assert product.price == 50.50
