import os

import psycopg2

basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'

    SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:12345@localhost:5432/postgres_db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
