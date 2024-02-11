"""System settings class"""

import os
from dataclasses import dataclass
from pathlib import Path
from typing import Optional

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

    @property
    def db_url(self) -> str:
        """
        Generates an url connection for database
        :return: database url connection string
        """
        return (
            f"{self.db_driver}://{self.db_user}:{self.db_password}"
            f"@{self.db_host}:{self.db_port}/{self.db_name}"
        )


def get_env_path() -> Optional[Path]:
    """
    Find .env file path
    :return: string path of .env file
    """
    cwd = Path.cwd()

    env_path = cwd / ".env"
    if env_path.is_file():
        return env_path

    env_path = cwd.parent / ".env"
    if env_path.is_file():
        return env_path

    return None
