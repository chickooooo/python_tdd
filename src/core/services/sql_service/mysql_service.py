"""This file includes MySQL implementation of SQLService."""


from pydantic import BaseModel
from core.services.sql_service.sql_exception import SQLException
from core.services.sql_service.sql_service import SQLService


# mock database
# records are stored in format: {"id": 1, "name": "orange", "price": 4.99}
DATABASE = []


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
        # verify record type
        if not isinstance(query_data, dict):
            # raise type error
            raise TypeError("'query_data' should be a valid dict.")

        # for each record in database
        for record in DATABASE:
            success = True

            # for each key-value pair in query_data
            for key, value in query_data.items():
                # if record's key does not match with value
                if record[key] != value:
                    success = False
                    break

            # if all key-value pairs matched
            if success:
                # get type of T
                type_t = self.__orig_class__.__args__[0]  # type: ignore
                # create and return model of type T
                return type_t.model_validate(obj=record, strict=True)

    def read_multiple(self, query_data: dict) -> list[T]:
        # verify record type
        if not isinstance(query_data, dict):
            # raise type error
            raise TypeError("'query_data' should be a valid dict.")

        # will hold matching objects
        result: list[T] = []

        # for each record in database
        for record in DATABASE:
            success = True

            # for each key-value pair in query_data
            for key, value in query_data.items():
                # if record's key does not match with value
                if record[key] != value:
                    success = False
                    break

            # if all key-value pairs matched
            if success:
                # get type of T
                type_t = self.__orig_class__.__args__[0]  # type: ignore
                # create and append model of type T to result
                result.append(type_t.model_validate(obj=record, strict=True))

        return result

    def update(self, updated_record: T) -> None:
        # verify updated_record type
        if not isinstance(updated_record, BaseModel):
            # raise type error
            raise TypeError("'updated_record' should be a valid model.")

        # for each record in database
        for i, record in enumerate(DATABASE):
            # if record id matches
            if record["id"] == updated_record.id:  # type: ignore
                # update the record
                DATABASE[i] = updated_record.model_dump()

                # break the loop
                break

    def delete(self, query_data: dict) -> None:
        # verify record type
        if not isinstance(query_data, dict):
            # raise type error
            raise TypeError("'query_data' should be a valid dict.")

        i: int = 0
        while i < len(DATABASE):
            success = True

            # for each key-value pair in query_data
            for key, value in query_data.items():
                # if record's key does not match with value
                if DATABASE[i][key] != value:
                    success = False
                    break

            # if all key-value pairs matched
            if success:
                DATABASE.pop(i)
            else:
                i += 1
