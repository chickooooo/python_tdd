from pydantic import BaseModel, field_validator


class Product(BaseModel):
    # product id
    id: int
    # product name
    name: str
    # product price
    price: float

    @field_validator("id")
    @classmethod
    def validate_id(cls, value: int):
        """Validate 'id' field."""

        # if non positive value
        if value <= 0:
            raise ValueError("'id' must be a positive integer")

        return value

    @field_validator("name")
    @classmethod
    def validate_name(cls, value: str):
        """Validate 'name' field."""

        # strip value
        value = value.strip()

        # if value is empty
        if value == "":
            raise ValueError("'name' cannot be empty")
        # else if value has less than 5 characters
        elif len(value) < 5:
            raise ValueError("'name' should be atleat 5 characters long.")

        return value

    @field_validator("price")
    @classmethod
    def validate_price(cls, value: float):
        """Validate 'price' field."""

        # if non positive value
        if value <= 0.0:
            raise ValueError("'price' must be a positive number")

        return value
