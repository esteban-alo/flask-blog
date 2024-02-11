"""
Config class tests cases
"""

from src.settings.config import Settings, get_env_path


def test_get_env_path():
    """
    Test get_env_path finds .env file
    """
    assert get_env_path() is not None


def test_load_settings_class():
    """
    Test load configuration
    """
    env_file = get_env_path()
    settings = Settings.load_configuration(env_file)

    assert settings.db_name is not None
