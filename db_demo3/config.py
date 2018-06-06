#encoding: utf-8

HOSTNAME = '127.0.0.1'
PORT = '3306'
DATABASE = 'db_demo3'
USERNAME = 'root'
PASSWORD = '123'

DB_URI = 'mysql+mysqldb://{}:{}@{}:{}/{}?charset=utf8'.format(USERNAME,PASSWORD,HOSTNAME,PORT,
DATABASE)

# SQLALCHEMY_DATABASE_URI = 'mysql://root:123@localhost:3306/db_demo3?charset=utf8'
# SQLALCHEMY_COMMIT_ON_TEARDOWN = True

SQLALCHEMY_DATABASE_URI = DB_URI
SQLALCHEMY_TRACK_MODIFICATIONS = True