"""This file includes MySQL implementation of SQLService."""


from pydantic import BaseModel
from core.services.sql_service.sql_exception import SQLException
from core.services.sql_service.sql_service import SQLService


# mock database
DATABASE = [
    {"id": 1, "name": "orange", "price": 4.99},
]


class MySQLService[T](SQLService):
    """MySQL implementation of SQL service."""

    def create(self, record: T) -> None:
        # verify record type
        if not isinstance(record, BaseModel):
            # raise type error
            raise TypeError("'record' should be a valid model.")

        # get record id
        record_id: int = record.id  # type: ignore

        # if record_id already present in database
        if record_id in [item["id"] for item in DATABASE]:
            # raise SQLException
            raise SQLException(f"duplicate id: {record_id}")

        # otherwise add record to database
        DATABASE.append(record.model_dump())

    def read_single(self, query_data: dict) -> T | None:
        raise NotImplementedError("Method hasn't been implemented yet.")

    def read_multiple(self, query_data: dict) -> list[T]:
        raise NotImplementedError("Method hasn't been implemented yet.")

    def update(self, query_data: dict, updated_data: dict) -> None:
        raise NotImplementedError("Method hasn't been implemented yet.")

    def delete(self, query_data: dict) -> None:
        raise NotImplementedError("Method hasn't been implemented yet.")
