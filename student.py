class Student:
   def __init__(self,name,age):
       self._name=name
       self._age=age
   def display(self):
       print(self._name,self._age)
stu1=""
stu2=""
stu3=""
student=[stu1,stu2,stu3]
for i in student:


  i= Student(input("enther your name:"),input("enter your age:"))

  i.display()


