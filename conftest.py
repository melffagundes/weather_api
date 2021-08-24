import pytest
import application as serv


# Creates a fixture whose name is "app"
# and returns our flask server instance
@pytest.fixture
def app():
    app = serv.app
    return app
