import os

basedir = os.path.abspath(os.path.dirname(__file__))

DEBUG = os.environ.get('DEBUG') == 'True'
PORT = os.environ.get('APP_PORT')
HOST = os.environ.get('APP_HOST')
CLIENT_PORT = os.environ.get('CLIENT_PORT')
CLIENT_HOST = os.environ.get('CLIENT_HOST')

