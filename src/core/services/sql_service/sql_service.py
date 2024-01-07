from abc import ABC, abstractmethod


class SQLService[T](ABC):
    @abstractmethod
    def create(self, record: T) -> None:
        """Create new record in database.

        Args:
            record (T): New record.

        Raises: SQLException.
        """

    @abstractmethod
    def read_single(self, query_data: dict) -> T | None:
        """Read and return a single record from database.

        Args:
            query_data (dict): SQL query data in dict format.

        Raises: SQLException.

        Returns:
            T | None: Record if found else None.
        """

    @abstractmethod
    def read_multiple(self, query_data: dict) -> list[T]:
        """Read and return multiple records from database.

        Args:
            query_data (dict): SQL query data in dict format.

        Raises: SQLException.

        Returns:
            list[T]: List of records if found else [].
        """

    @abstractmethod
    def update(self, query_data: dict, updated_data: dict) -> None:
        """Update record(s) in database.

        Args:
            query_data (dict): SQL query data in dict format.
            updated_data (dict): Updated data in dict format,
            where key represents column name & value represents updated value.

        Raises: SQLException.
        """

    @abstractmethod
    def delete(self, query_data: dict) -> None:
        """Delete record(s) in database.

        Args:
            query_data (dict): SQL query data in dict format.

        Raises: SQLException.
        """
