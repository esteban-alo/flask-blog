"""
Permissions repository class
"""

from typing import Any, List, Optional, Type

from sqlalchemy import delete, select, update

from src.orm.mapper import Permission, permissions
from src.orm.unit_of_work import SQLAlchemyUnitOfWork
from src.repository.base import AbstractRepository


class PermissionRepository(AbstractRepository):
    """
    Permissions query management class
    """

    def __init__(self, unit_of_work: SQLAlchemyUnitOfWork):
        """
        Unit of Work initialization
        :param unit_of_work:
        """
        self._unit_of_work = unit_of_work

    def add(self, model_class: Permission) -> Permission:
        """
        Store a new object
        :param model_class:
        :return:
        """
        self._unit_of_work.session.add(model_class)
        self._unit_of_work.session.flush()

        return model_class

    def all(self, limit: int, offset: int) -> List[Type[Permission]]:
        """
        List permissions items
        :param limit:
        :param offset:
        :return:
        """

        stmt = select(permissions).limit(limit).offset(limit * offset)

        return self._unit_of_work.session.query(Permission).from_statement(stmt).all()

    def delete(self, _id: int) -> None:
        """
        Delete an object by id
        :param _id:
        :return:
        """

        stmt = delete(permissions).where(permissions.c.id == _id)

        self._unit_of_work.session.execute(stmt)

    def get(self, _id: int) -> Optional[Permission]:
        """
        Retrieves an object by id
        :param _id:
        :return:
        """

        stmt = select(permissions).where(permissions.c.id == _id)

        return (
            self._unit_of_work.session.query(Permission)
            .from_statement(stmt)
            .one_or_none()
        )

    def update(self, _id: int, **kwargs: Any) -> None:
        """
        Update object information
        :param _id:
        :param kwargs:
        :return:
        """

        stmt = update(permissions).where(permissions.c.id == _id).values(**kwargs)

        self._unit_of_work.session.execute(stmt)
