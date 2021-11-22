import os
from dotenv import load_dotenv

load_dotenv()

user = os.environ['MYSQL_USER']
password = os.environ['MYSQL_PASSWORD']
hotst = os.environ['MYSQL_HOST']
database = os.environ['MYSQL_DATABASE']


SECRET_KEY = os.environ['SECRET_KEY']

DATABASE_CONNECTION_URI = f'mysql://{user}:{password}@{hotst}/{database}'
