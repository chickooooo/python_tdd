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

        Returns:
            Product: Created product.
        """

        # create product object
        product: Product = Product.model_validate(product_data)
        # create record in database
        self.__sql_service.create(product)

        return product
