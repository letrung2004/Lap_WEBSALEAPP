from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from urllib.parse import quote

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://root:%s@localhost/saledb?charset=utf8mb4" % quote('Admin@123')
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False  # It's often recommended to set this to False
db = SQLAlchemy(app)
