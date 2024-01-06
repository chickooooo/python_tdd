"""Injection of all the required dependencies."""


from core.services.sql_service.sql_service import SQLService
from core.services.sql_service.mysql_service import MySQLService

from features.product.models.product import Product


# product sql service
product_sql_service: SQLService = MySQLService[Product]()
