from app import db, todos

db.create_all() 

Task_2 = todos(Task = 'make another table', Completed = True)
#completed_task1 = todos(name= "True")
db.session.add(Task_2)
db.session.commit()
