"""Test Cases

- Verify imports
"""


from core.services.sql_service.sql_service import SQLService
from core.services.sql_service.mysql_service import MySQLService
from features.product.models.product import Product
from core import dependency_injection as di


def test_imports():
    """Test imports."""

    # verify imports
    assert di.Product is Product
    assert di.SQLService is SQLService
    assert di.MySQLService is MySQLService
