"""
SQLAlchemy Unit-Of-Work ORM
"""

from sqlalchemy.orm import Session

from src.database.config import database
from src.repository.unit_of_work import AbstractUnitOfWork


class SQLAlchemyUnitOfWork(AbstractUnitOfWork):
    """
    Concrete implementation of Unit of Work using SQLAlchemy.
    """

    def __init__(self, session_factory: Session = database.db_session):
        """
        Initialize the Unit of Work with the given SQLAlchemy session factory.
        :param session_factory: SQLAlchemy session factory
        """
        self.session = session_factory

    def __enter__(self):
        """Start a new transaction."""
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        """
        Commit the transaction if no exceptions occurred, otherwise rollback.
        :param exc_type: exception type
        :param exc_val: exception value
        :param exc_tb: exception traceback
        """
        self.session.close()

    def commit(self):
        """Commit the transaction."""
        self.session.commit()

    def rollback(self):
        """Rollback the transaction."""
        self.session.rollback()
