import instance as serv
import sys, os

# Need to import all resources
# so that they register with the server
from application import *

if __name__ == '__main__':
    s = serv.server
    s.api.init_app(s.app, add_specs=False)
    s.run()