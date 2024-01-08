"""Injection of all the required dependencies."""


from core.services.sql_service.sql_service import SQLService
from core.services.sql_service.mysql_service import MySQLService

from features.product.models.product import Product
from features.product.usecases.product_crud_usecase import ProductCrudUsecase


# services
__product_sql_service: SQLService = MySQLService[Product]()


# usecases
product_crud_usecase = ProductCrudUsecase(__product_sql_service)
