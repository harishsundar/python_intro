#!/usr/bin/python
print "hello"
#variables
#integer
a = 2
print a*2
#float
a= 2.34
print a*2
#character
a = "c"
print a*2
#string
a = "hello ceglug"
print a*2
#-----------------------------------
#input
name_number = input("Enter your name: ")
print ('Hello', name_number)
name = raw_input("enter your name: ")
print ("Hello", name)
#--------------------------------------------
#input and if then else syntax
number = input("Enter the number ")
print ('Hello', number)
if number == 2:
    print ("The value of number is: ",number)
elif number == 4:
    print ("The value of number is: ",number)
else:
    print ("Neither 2, nor 4, the number is: ", number)
#-------------------------------------------------------------
#function
def add(p,q):
    return p+q
    
def subtract(p,q):
    return p-q

def multiply (p,q):
    return p*q

def divide (p,q):
    return float(p)/float(q)
a = 4
b = 6

print add (a,b)
print subtract (a,b)
print multiply (a,b)
print float(divide (a,b))
#--------------------------------------
#lists
names = ['darwin', 'krishna', 'dickens']
names[0] = "bharathiar"
number = [ 6, 7,8,9]
print names[0], number[0]
print names + number
print [names]+[number]
#-----------------------------------------
# dictionary
students = {1:"ram", 2: "govind", 3: "asura"}
print students
print students[1]
print len (students)
for i,v in students.items ():
    print i,v
#-----------------------------------------
#tuple
tuple1 = ('python', 'ruby','c','java')
list1 = ['python','ruby','c','java']
print tuple1
print list1
# Let's include windows in the list and it works!
list1[1] = "windows"
print list1
# Windows does not work here!
tuple1[1] = "windows"
print tuple1
#----------------------------------------------------------
#file reading and writing

file1 = open('test.txt')
for line in file1:
    print line    
file2 = open('test2.txt','w')
line2 = "This is a text from the program \n"
file2.write(line2)    
#---------------------------------------------------
#try and exception
inp = raw_input("Enter the temp in number ")
try:
    fahr =  float(inp)
    cel = (fahr - 32.0) *5.0/9.0
    print cel
except:
    print "You have not entered the number. Quitting........."
#------------------------------------------------------------
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