from pydantic import BaseModel
from features.product.models.product import Product
from core.services.sql_service.sql_service import SQLService


class ProductCrudUsecase:
    """Product usecase for database CRUD operations."""

    def __init__(self, sql_service: SQLService[Product]) -> None:
        # validate sql_service
        if not isinstance(sql_service, SQLService):
            raise TypeError("'sql_service' should be of type 'SQLService'")

        # create private instances
        self.__sql_service: SQLService = sql_service

    def create_product(self, product_data: dict) -> Product:
        """Create a new product and add it to database.

        Args:
            product_data (dict): Product data in dictionary format.

        Raises:
            ValueError: If product_data is not valid.
            SQLException: If error with database.

        Returns:
            Product: Created product.
        """

        # create product object
        product: Product = Product.model_validate(product_data)
        # create record in database
        self.__sql_service.create(product)

        return product

    def get_product(self, query_data: dict) -> Product | None:
        """Get a single product from database matching the query.

        Args:
            query_data (dict): Query in key-value format.

        Raises:
            TypeError: If query_data is invalid.
            SQLException: If error with database.

        Returns:
            Product | None: First found product else None.
        """

        # verify query_data type
        if not isinstance(query_data, dict):
            # raise type error
            raise TypeError("'query_data' should be a valid dict.")

        # read & return from sql service
        return self.__sql_service.read_single(query_data)

    def get_products(self, query_data: dict) -> list[Product]:
        """Get all the products from database matching the query.

        Args:
            query_data (dict): Query in key-value format.

        Raises:
            TypeError: If query_data is invalid.
            SQLException: If error with database.

        Returns:
            list[Product]: List of found products else [].
        """

        # verify query_data type
        if not isinstance(query_data, dict):
            # raise type error
            raise TypeError("'query_data' should be a valid dict.")

        # read & return from sql service
        return self.__sql_service.read_multiple(query_data)

    def update_product(self, updated_product: Product) -> None:
        """Update existing product in database. Will do nothing
        if product is not found.

        Args:
            updated_product (Product): Updated product object.

        Raises:
            TypeError: If updated_product is not a valid model.
            SQLException: If error with database.

        Returns: None
        """

        # verify updated_product type
        if not isinstance(updated_product, BaseModel):
            # raise type error
            raise TypeError("'updated_product' should be a valid model.")

        # update & return from sql service
        return self.__sql_service.update(updated_product)

    def delete_product(self, query_data: dict) -> None:
        """Delete product(s) from database matching the query.
        Will do nothing if no product is found.

        Args:
            query_data (dict): Query in key-value format.

        Raises:
            TypeError: If query_data is invalid.
            SQLException: If error with database.

        Returns: None
        """

        # verify query_data type
        if not isinstance(query_data, dict):
            # raise type error
            raise TypeError("'query_data' should be a valid dict.")

        # delete & return from sql service
        return self.__sql_service.delete(query_data)
