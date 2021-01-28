import pytest
from flask_app import app as test_app

@pytest.fixture
def app():
    yield test_app.app


@pytest.fixture
def client(app):
    return app.test_client()
