from features.product.models.product import Product
from core.services.sql_service.sql_service import SQLService


class ProductCrudUsecase:
    def __init__(self, sql_service: SQLService[Product]) -> None:
        # validate sql_service
        if not isinstance(sql_service, SQLService):
            raise TypeError("'sql_service' should be of type 'SQLService'")

        # create private instances
        self.__sql_service: SQLService = sql_service
