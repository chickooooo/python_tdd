from abc import ABC, abstractmethod


class SQLService[T](ABC):
    @abstractmethod
    def create(self, record: T) -> bool:
        """Create new record in database.

        Args:
            record (T): New record.

        Raises: SQLException.

        Returns:
            bool: True on successful creation else False.
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
    def update(self, query_data: dict, updated_data: dict) -> bool:
        """Update record(s) in database.

        Args:
            query_data (dict): SQL query data in dict format.
            updated_data (dict): Updated data in dict format,
            where key represents column name & value represents updated value.

        Raises: SQLException.

        Returns:
            bool: True on successful updation else False.
                  Will return True if no record found in database
                  matching the query_data.
        """

    @abstractmethod
    def delete(self, query_data: dict) -> bool:
        """Delete record(s) in database.

        Args:
            query_data (dict): SQL query data in dict format.

        Raises: SQLException.

        Returns:
            bool: True on successful updation else False.
                  Will return True if no record found in database
                  matching the query_data.
        """
