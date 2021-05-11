

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

#app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///data.db"
#app.config["SQLALCHEMY_DATABASE_URI"] = 'mysql+pymysql://mysql_user:mysql_password>@mysql_instance_ip>:3306/<mysql_db>'
app.config["SQLALCHEMY_DATABASE_URI"] = 'mysql+pymysql://root:1234@35.189.79.75:3306/TESTDB'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
class Orders(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    Date_of_purchase = db.Column(db.String(10), nullable=False)
    name_of_customer = db.Column(db.String(20),nullable=False)
    Chosen_items = db.relationship('chosen_items', backref='orders') 

class Products(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), nullable=False)
    availability = db.Column(db.String(30), nullable=False)
    Chosen_items = db.relationship('chosen_items', backref='products')

class Chosen_items(db.Model):
    id =id = db.Column(db.Integer, primary_key=True) 
    order_id= db.Column(db.Integer, db.ForeignKey('orders.id'), nullable=False)
    product_id=db.Column(db.Integer, db.ForeignKey('products.id'), nullable=False)
if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')