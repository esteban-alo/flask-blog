"""
Base repository abstract class
"""

from abc import ABC, abstractmethod
from typing import Any, List, Type

from src.domain.model import TableBase


class AbstractRepository(ABC):
    """
    Abstract Repository class
    """

    @abstractmethod
    def add(self, model_class: TableBase) -> TableBase:
        """
        Store a new object
        :param model_class:
        :return:
        """
        raise NotImplementedError

    @abstractmethod
    def all(self, limit: int, offset: int) -> List[Type[TableBase]]:
        """
        List roles items
        :param limit:
        :param offset:
        :return:
        """
        raise NotImplementedError

    @abstractmethod
    def delete(self, _id: int) -> None:
        """
        Delete an object by id
        :param _id:
        :return:
        """
        raise NotImplementedError

    @abstractmethod
    def get(self, _id: int) -> TableBase:
        """
        Retrieves an object by id
        :param _id:
        :return:
        """
        raise NotImplementedError

    @abstractmethod
    def update(self, _id: int, **kwargs: Any) -> TableBase:
        """
        Update object information
        :param _id:
        :param kwargs:
        :return:
        """
        raise NotImplementedError
