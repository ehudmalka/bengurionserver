import flask
from flask import request
from flask_sqlalchemy import SQLAlchemy #import sqlalchemy
from flask_cors import CORS #import the cors class

app = flask.Flask(__name__)
app.config["DEBUG"] = True

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db' #set the config to use the database (which I called database.db)
db = SQLAlchemy(app) #create an SQLAlchemy instance
cors = CORS(app) #allow every website to access this api (CORS - cross origin resource sharing, a security protocol which limits the origins (domains) which can call this api, we can limit only to the our website once we have one)

@app.route('/search', methods=['GET'])
def search():
    #lets say this function will search by name (just to test the db)
    name = request.args.get("name")
    students = Student.query.filter_by(name=name).all() #get all students with the given name, this is the syntax
    respDictionary = list(map(Student.toDictionary, students)) #run to dictionary in order to let flask know what is this object so it can return it as json on each object and convert the result to list (of student's dictionaries)
    return str(respDictionary)

@app.route('/register', methods=['GET'])
def register():
    studentName = request.args.get("name")
    studentAge = request.args.get("age")
    st = Student(name=studentName, age=studentAge) #no need to create an id, sqlite does it to us automatically
    db.session.add(st) #add the student to the database (will automatically add it to specifically the student table)
    db.session.commit() #commit the changes, needed after every change to actually save it in the database
    return "success"

if __name__ == "__main__":
    from student import Student #import the student class from the student file (since the student file also imports the db from this file, put the import later to avoid errors)
    db.create_all() #automatically create all the tables, since we configured the student class as a table, it will automatically create it if neede
    app.run()
#install the flask-sqlalchemy and flask-cors addons in File->Settings->Project: bengurionserver->Project Interpreter->+
#I already installed sqlite and everything needed here
#I already created a database called database.db
#db table is made out of rows and columns - each row is a student, while each column is its property. right now I created id, name and age (each table needs an id column)
