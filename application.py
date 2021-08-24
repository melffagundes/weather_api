from flask import Flask, jsonify
from flask_restx import Resource
import flask
import requests as req
from cachetools import cached, TTLCache
from threading import Lock
from flask_restx import Api
import conf
import instance


app, api = instance.server.app, instance.server.api

# Variables

API_KEY = conf.Config.OPENW_KEY
API_URL = conf.Config.API_URL
ns = api.namespace('weather', description='Weather API')

# Initialize TTLCache, lock and create Swagger namespace
cache = TTLCache(maxsize=5, ttl=300)
lock = Lock()


# Handles GET to /weather/:city_name
@cached(cache, lock=lock)
@api.route('/weather/<city_name>', methods=['GET'])
@api.doc(params={'city_name': 'name of city for weather search'})
class City(Resource):
    def get(self, city_name):
        try:
            result = cache.get(city_name)
            if result is None:
                url = f"{API_URL}{city_name}"
                params = {'appid': API_KEY}
                result = req.get(url, params).json()
                if result is not None:
                    if result["cod"] == 200:
                        cache[city_name] = result

            return jsonify(result)
        except KeyError as e:
            ns.abort(500, e.__doc__, status="Internal server error", statusCode="500")

        except Exception as e:
            ns.abort(400, e.__doc__, status="Bad Request", statusCode="400")


# Handles GET to /weather/:max
@api.route('/weather/<int:max>', methods=['GET'])
@api.doc(params={'max': 'configurable number of last searched cities'})
class CitiesList(Resource):
    def get(self, max):
        try:
            max_cities = 5
            result = []
            with lock:
                if max is None or max > max_cities:
                    max = max_cities
                for x in list(reversed(list(cache)))[0:max]:
                    result.append(cache[x])

            return jsonify(result)

        except KeyError as e:
            ns.abort(500, e.__doc__, status="Intern server error", statusCode="500")


if __name__ == "__main__":
    app.run(port=5000, debug=True)