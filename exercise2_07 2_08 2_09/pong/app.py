from flask import Flask
import os
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

pg_user = os.getenv('POSTGRES_USER')
pg_passwd = os.getenv('POSTGRES_PASSWORD')
pg_svc = os.getenv('POSTGRES_SERVICE')
pg_port = os.getenv('POSTGRES_PORT')
pg_db = os.getenv('POSTGRES_DB')

DATABASE_URL = "postgresql://{pg_user}:{pg_passwd}@{pg_svc}:{pg_port}/{pg_db}".format(pg_user=pg_user, \
     pg_passwd=pg_passwd, pg_svc=pg_svc, pg_port=pg_port, pg_db=pg_db)
print("DATABASE_URL", DATABASE_URL)
app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE_URL
db = SQLAlchemy(app)