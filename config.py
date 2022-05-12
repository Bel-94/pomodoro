import os

class Config:
    SQLALCHEMY_TRACK_MODIFICATIONS=True
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://amiani:pass2022@localhost/belinda'
    SECRET_KEY = 'MODIFY'

class ProdConfig(Config):
    pass
        

class DevConfig(Config):
    DEBUG = True


config_options = {
'development':DevConfig,
'production':ProdConfig
}