"""
Config class tests cases
"""

import pytest

from src.settings.config import Settings, get_env_path


def test_get_env_path():
    """
    Test get_env_path finds .env file
    """
    assert get_env_path() is not None


def test_env_not_found(tmp_path, monkeypatch):
    """
    Use pytest’s tmp_path fixture together with monkeypatch to change the working directory and verify that an exception is raised when the .env file is not found
    """
    monkeypatch.chdir(tmp_path)

    with pytest.raises(FileNotFoundError, match=".env file not found"):
        get_env_path()


def test_load_settings_class():
    """
    Test load configuration
    """
    env_file = get_env_path()
    settings = Settings.load_configuration(env_file)

    assert settings.db_name is not None
