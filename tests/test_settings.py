import pytest
from pydantic import ValidationError

from settings import Settings


def test_settings_loaded_from_test_env():
    settings = Settings()
    assert settings.ENVIRONMENT == "test"
    assert settings.APP_NAME == "iris-ml-app-test"
    assert settings.API_KEY == "fake-test-api-key"


def test_settings_rejects_invalid_environment(monkeypatch):
    monkeypatch.setenv("ENVIRONMENT", "xyz")
    with pytest.raises(ValidationError):
        Settings()
