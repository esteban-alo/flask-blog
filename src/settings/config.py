"""System settings class"""

import os
from dataclasses import dataclass

from dotenv import load_dotenv


@dataclass
class Settings:
    """System settings"""

    db_driver: str
    db_host: str
    db_name: str
    db_password: str
    db_port: str
    db_user: str

    @classmethod
    def load_configuration(cls, env_file=".env"):
        """
        Load system settings from .env
        :param env_file: .env file path
        """

        load_dotenv(dotenv_path=env_file)
        return cls(
            db_driver=os.getenv("DB_DRIVER"),
            db_host=os.getenv("DB_HOST"),
            db_name=os.getenv("DB_NAME"),
            db_password=os.getenv("DB_PASSWORD"),
            db_port=os.getenv("DB_PORT"),
            db_user=os.getenv("DB_USER"),
        )
