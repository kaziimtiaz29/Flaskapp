#import re
from flask import Flask,url_for,redirect
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
def index():
    all_todos= todos.query.all()
    todos_1= ""
    for c in all_todos:
        todos_1+="<br>"+str(c.id)+" " +c.Task+" "+str(c.Completed)
    return  f'this is a to-do list <br> {todos_1}'
    
 
@app.route('/addtodos')
def to_do1():
    Task_3 = todos(Task = 'new todo', Completed = False)
    db.session.add(Task_3)
    db.session.commit()
    return "added new task"

@app.route('/complete/<int:n>')
def is_complete(n):
    task_4= todos.query.get(n)
    task_4.Completed = True
    db.session.commit()
    return 'its completed'


@app.route('/incomplete/<int:n>')
def is_incomplete(n):
    task_5= todos.query.get(n)
    task_5.Completed = False
    db.session.commit()
    return 'its incompleted'

@app.route('/delete/<int:n>')
def is_delete(n):
    task_6 = todos.query.get(n)
    db.session.delete(task_6)
    db.session.commit()
   # return 'deleted'
    return  redirect (url_for("index"))


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')