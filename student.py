from main import db #import the db from main.py in order to use it here

class Student(db.Model): #inherit from db.Model to connect to the database
    id = db.Column('id', db.Integer, primary_key=True, autoincrement=True) #create an id column. each row in the database needs unique id, mark its as primary key since this is the id the database will use
    name = db.Column(db.String(20), nullable=False) #mark the name as column of string with maximum 20 characters. nullable=false means it cant be null, it must be filled
    age = db.Column(db.Integer, nullable=False) #mark the age as an integer column
    def display(self):
        print(self.name,self.age)

'''
Comment this to avoid running this (because we import this file)
stu1=""
stu2=""
stu3=""
student=[stu1,stu2,stu3]
for i in student:


  i= Student(input("enther your name:"),input("enter your age:"))

  i.display()
'''

