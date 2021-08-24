from flask_restx import Api
from flask import Flask
import conf


# -Create Flask APP
# -Add config
# -Initialize app
class Server(object):
    def __init__(self):
        self.app = Flask(__name__)
        self.api = Api(self.app,
                       version='1.0',
                       title='Weather API',
                       description='A API that given city name, collects data from the Open Weather API, caches it for some configurable time and returns it as a JSON object. Also returns a configurable number of last searched cities.',
                       doc=conf.Config.SWAGGER_URL
                       )


    def run(self):
        self.app.run(
            debug=True,
            port=5000

        )


server = Server()
