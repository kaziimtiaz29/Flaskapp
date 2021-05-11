

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

#app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///data.db"
#app.config["SQLALCHEMY_DATABASE_URI"] = 'mysql+pymysql://mysql_user:mysql_password>@mysql_instance_ip>:3306/<mysql_db>'
app.config["SQLALCHEMY_DATABASE_URI"] = 'mysql+pymysql://root:1234@35.189.79.75:3306/TESTDB'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
class Users(db.Model):
    id=db.Column(db.Integer,primary_key = True)
    first_name=db.Column(db.String(30),nullable = False)
    last_name =db.Column(db.String(30),nullable=False)

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')