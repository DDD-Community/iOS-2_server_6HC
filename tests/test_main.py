from app import create_app
import pytest


def test_fixture_app_should_work(app):
    assert app


@pytest.mark.parametrize("env", [("test"), ("dev"), ("prod")])
def test_app_with_config_should_return_env(env):
    app = create_app(env)

    assert app.config["ENV"] == env


def test_ping_should_return_success(test_client):
    res = test_client.get("/ping")
    assert res.status_code == 200