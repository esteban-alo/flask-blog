"""
Database configuration class
"""

from sqlalchemy import create_engine
from sqlalchemy.orm import Session

from src.settings.config import Settings, get_env_path


class Database:
    """
    Database configuration
    """

    def __init__(self, config_settings: Settings):
        self.__settings = config_settings

    @property
    def db_engine(self):
        """
        Create database engine
        """
        return create_engine(self.__settings.db_url)

    @property
    def db_session(self):
        """
        Create database session
        """
        return Session(self.db_engine)


database = Database(Settings.load_configuration(get_env_path()))
