from abc import ABC, abstractmethod


class SQLService[T](ABC):
    """SQL service."""

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
            T | None: First found record else None.
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
    def update(self, updated_record: T) -> None:
        """Update record in database.

        Args:
            updated_record (dict): Updated record.

        Raises: SQLException.
        """

    @abstractmethod
    def delete(self, query_data: dict) -> None:
        """Delete record(s) in database.

        Args:
            query_data (dict): SQL query data in dict format.

        Raises: SQLException.
        """
