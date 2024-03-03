"""
Unit of work repository
"""

from abc import ABC, abstractmethod


class AbstractUnitOfWork(ABC):
    """
    Manages the database session and provides methods to commit, rollback, and close the session
    """

    def __enter__(self):
        """
        Start a new transaction
        """

    def __exit__(self, *args):
        """
        Commit the transaction if no exceptions occurred, otherwise rollback.
        """

    @abstractmethod
    def commit(self):
        """Commit the transaction."""
        raise NotImplementedError

    @abstractmethod
    def rollback(self):
        """Rollback the transaction."""
        raise NotImplementedError
