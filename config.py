import os
from decouple import config

# Access the API key using .env method
api_key2 = config('API_KEY')
# Access the API key using os .env method
api_key = os.environ['API_KEY']

class Config(object):
    DEBUG = True
    TESTING = False

class DevelopmentConfig(Config):
    OPENAI_KEY = api_key

config = {
    'development': DevelopmentConfig,
    'testing': DevelopmentConfig,
    'production': DevelopmentConfig
}
