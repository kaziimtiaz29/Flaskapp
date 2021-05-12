#import re
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

#app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///data.db"
#app.config["SQLALCHEMY_DATABASE_URI"] = 'mysql+pymysql://mysql_user:mysql_password>@mysql_instance_ip>:3306/<mysql_db>'
app.config["SQLALCHEMY_DATABASE_URI"] = 'mysql+pymysql://root:1234@35.189.79.75:3306/TESTDB'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)


class todos(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    Task = db.Column(db.String(30), nullable=False)
    Completed = db.Column(db.Boolean,nullable=False)
    #country_id = db.Column(db.Integer, db.ForeignKey('countries.id'), nullable=False)


@app.route('/')
def home():
    return 'This is a to do list'
@app.route('/todos')
def to_dos():
    game_with_id_1 = todos.query.get(1)
    return str(game_with_id_1)
    '''all_todos = todos.query.all()
    return all_todos'''
'''
list_of_todos = ""
    for task in all_todos:
        list_of_todos += "<br>"+ task.name
    return list_of_todos'''

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')