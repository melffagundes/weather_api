import pytest
import application

# client is a fixture, injected by the `pytest-flask` plugin
def test_get_last_cities_nocache(client):
    """
        GIVEN a Flask application configured for testing
        WHEN the '/weather?max' page is requested (GET) and cache is empty
        THEN check that the response is valid
        """
    response = client.get("/weather/1")
    assert response.status_code == 200


def test_get_city(client):
    """
        GIVEN a Flask application configured for testing
        WHEN the '/weather/<city_name>' page is requested (GET)
        THEN return response to validate
        """
    response = client.get("/weather/curitiba")
    assert response.status_code == 200

def test_get_last_cities(client):
    """
        GIVEN a Flask application configured for testing
        WHEN the '/weather?max' page is requested (GET)
        THEN check that the response is valid
        """

    response = client.get("/weather/1")
    print(response.data)
    assert response.status_code == 200

def test_last_cities(client):
    """
           GIVEN a Flask application configured for testing
           WHEN search for three cities
           THEN check that the last cities are in the cache
           """
    client.get("/weather/viena")
    client.get("/weather/sorocaba")
    client.get("/weather/barcelona")


    # Validate weither return two lasts cities in cache or  not
    response = client.get("/weather/1")
    print(response.data)
    assert b"Barcelona" in response.data

def test_last_max_default(client):
    """
           GIVEN a Flask application configured for testing
           WHEN the max > max_number (GET)
           THEN check that return the five cities (maximum 5 by default)
           """
    client.get("/weather/viena")
    client.get("/weather/sorocaba")
    client.get("/weather/barcelona")
    client.get("/weather/belo horizonte")
    client.get("/weather/rio de janeiro")
    client.get("/weather/recife")


    # Validate weither return two lasts cities in cache or  not
    response = client.get("/weather/6")
    print(response.data)
    assert (b"Barcelona" in response.data) & (b"Recife" in response.data) & (b"Rio de Janeiro" in response.data) & (b"Belo Horizonte" in response.data) & (b"Sorocaba" in response.data)



def test_get_city_notfound(client):
    """
        GIVEN a Flask application configured for testing
        WHEN the '/weather/<city_name>' page is requested (GET) and city not found
        THEN check that the response is 400 error
        """
    response = client.get("/weather/curitoba")
    # Validate the response
    print(response.data)
    assert b"200" not in response.data


# client is a fixture, injected by the `pytest-flask` plugin
def test_get_home(client):
    """
        GIVEN a Flask application configured for testing
        WHEN the '/weather/' page is requested (GET) and city not found
        THEN check that the response is home page
        """
    response = client.get("/weather/")
    # Validate the response
    print(response.data)
    assert b"Weather" in response.data
