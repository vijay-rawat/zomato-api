# import os
# basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    # DB connection format: //username:password@host/db_name
    SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:postgres@localhost/zomato'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
