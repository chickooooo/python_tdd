"""This file will include
MySQL implementation of SQLService."""


from core.services.sql_service.sql_service import SQLService


class MySQLService[T](SQLService):
    def create(self, record: T) -> None:
        raise NotImplementedError("Method hasn't been implemented yet.")

    def read_single(self, query_data: dict) -> T | None:
        raise NotImplementedError("Method hasn't been implemented yet.")

    def read_multiple(self, query_data: dict) -> list[T]:
        raise NotImplementedError("Method hasn't been implemented yet.")

    def update(self, query_data: dict, updated_data: dict) -> None:
        raise NotImplementedError("Method hasn't been implemented yet.")

    def delete(self, query_data: dict) -> None:
        raise NotImplementedError("Method hasn't been implemented yet.")
