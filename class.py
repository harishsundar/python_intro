#!/usr/bin/python

class Student:
    studCount = 0#variable
    
    def __init__(self,rollnumber,name):
        self.rollnumber = rollnumber
        self.name = name
        Student.studCount += 1
        
    def totalCount(self):
        print "Total number of students ", Student.studCount
    
    def student(self):
        print "Roll number ", self.rollnumber, "Name: ", self.name
        
    
stud1 = Student(20074141,"Ram")
stud2 = Student(20083245,"Krishna")

stud1. student()
stud2.student()
stud2.totalCount()
print Student.studCount
    