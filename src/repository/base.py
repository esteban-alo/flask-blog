"""
Base repository abstract class
"""

from abc import ABC, abstractmethod

from src.domain.model import TableBase


class AbstractRepository(ABC):
    """
    Abstract Repository class
    """

    model_class: TableBase

    @abstractmethod
    def add(self, model_class: TableBase) -> TableBase:
        """
        Store a new object
        :param model_class:
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
    def update(self, **kwargs) -> TableBase:
        """
        Update object information
        :param kwargs:
        :return:
        """
        raise NotImplementedError
