---
description: >-
  An API that for a given city name, collects data from the ​Open Weather API​,
  caches it for some configurable time and returns it as a JSON object. Returns
  a configurable number of last search cities.
---

# Weather Buddy API

## Getting Started

### Prerequisites

I assume you have installed Docker and it is running.

{% hint style="info" %}
 See the [Docker website](http://www.docker.io/gettingstarted/#h_installation) for installation instructions.
{% endhint %}

Steps to build a Docker image:

1. Clone this repo:

```
$ git clone https://github.com/melffagundes/weather_buddy.git
```

Now let’s start the services with `docker-compose.`

```bash
 docker build . -t deploy_flask  
```

 To check if the services are running enter the following command:

```bash
docker run -p 5000:5000 -t -i deploy_flask:latest 
```

You can now access [here](http://localhost:5000/weather/) the Flask application. 

Also, you can now access it [here](http://localhost:5000/api/swagger), and let’s go to Swagger and do the request on the weather endpoint.

{% api-method method="get" host="http://localhost:5000" path="/weather/" %}
{% api-method-summary %}
Weather 
{% endapi-method-summary %}

{% api-method-description %}

{% endapi-method-description %}

{% api-method-spec %}
{% api-method-request %}
{% api-method-query-parameters %}
{% api-method-parameter name="max" type="string" required=true %}
configurable number of last searched cities
{% endapi-method-parameter %}

{% api-method-parameter name="city\_name" type="string" required=false %}
name of the city for weather search
{% endapi-method-parameter %}
{% endapi-method-query-parameters %}
{% endapi-method-request %}

{% api-method-response %}
{% api-method-response-example httpCode=200 %}
{% api-method-response-example-description %}
Success
{% endapi-method-response-example-description %}

```
[
  {
    "base": "stations",
    "clouds": {
      "all": 75
    },
    "cod": 200,
    "coord": {
      "lat": 48.2085,
      "lon": 16.3721
    },
    "dt": 1629677997,
    "id": 2761369,
    "main": {
      "feels_like": 290.44,
      "humidity": 90,
      "pressure": 1018,
      "temp": 290.32,
      "temp_max": 292.07,
      "temp_min": 288.88
    },
    "name": "Vienna",
    "rain": {
      "1h": 5.62
    },
    "sys": {
      "country": "AT",
      "id": 2037452,
      "sunrise": 1629691200,
      "sunset": 1629741280,
      "type": 2
    },
    "timezone": 7200,
    "visibility": 10000,
    "weather": [
      {
        "description": "shower rain",
        "icon": "09n",
        "id": 521,
        "main": "Rain"
      }
    ],
    "wind": {
      "deg": 322,
      "gust": 0.89,
      "speed": 0.45
    }
  }
]
```
{% endapi-method-response-example %}
{% endapi-method-response %}
{% endapi-method-spec %}
{% endapi-method %}



### Run tests

You can also run tests Weather API:

I assume you have installed pytest.

{% hint style="info" %}
See the pytest documentation for installation instructions
{% endhint %}



