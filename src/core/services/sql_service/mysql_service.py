"""This file will include
MySQL implementation of SQLService."""


from core.services.sql_service.sql_service import SQLService


class MySQLService[T](SQLService):
    def create(self, _: T) -> bool:
        raise NotImplementedError("Method hasn't been implemented yet.")

    def read_single(self, _: dict) -> T | None:
        raise NotImplementedError("Method hasn't been implemented yet.")

    def read_multiple(self, _: dict) -> list[T]:
        raise NotImplementedError("Method hasn't been implemented yet.")

    def update(self, _: dict, __: dict) -> bool:
        raise NotImplementedError("Method hasn't been implemented yet.")

    def delete(self, _: dict) -> bool:
        raise NotImplementedError("Method hasn't been implemented yet.")
