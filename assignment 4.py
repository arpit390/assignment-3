'''# QUESTION 1 abstract method 
from abc import ABC, abstractmethod
class Animal(ABC):
    @abstractmethod 
    def eat1(self): 
        pass
@abstractmethod
def eat2(self): 
   pass 
class Tiger(Animal):
    def eat1(self): 
        print("Tiger implementation ...") 
class lion(Tiger):
    def eat2(self): 
        print("lion implementation ...") 
t = lion()
t.eat1()
t.eat2()

#question 2 
from abc import ABC, abstractmethod
class AbstractClassExample(ABC):
    def _init_(self, value): 
        self.value = value 
        super()._init_() 
 
@abstractmethod 
def do_something(self): 
    pass 
 
class DoAdd(AbstractClassExample):
    def do_something(self): 
        return self.value + 42 

class DoMul(AbstractClassExample):
    def do_something(self): 
        return self.value * 42 
x = DoAdd(10)
y = DoMul(10)
print(x.do_something())
print(y.do_something())

#question 3 raise and finally keyword 
def status(age):
    if age < 0: 
        raise ValueError("Only positive integers are allowed") 
    if age>22: 
        print("eligible for mrg") 
    else: 
        print("not eligible for mrg try after some time") 
try:
    num = int(input("Enter your age: ")) 
    status(num) 
except ValueError:
    print("Only positive integers are allowed you ......") 
finally:
    print("finally block....")

#question 4 
class NegativeAgeException(RuntimeError):
    def _init_(self, age): 
        super()._init_() 
        self.age = age 
def status(age):
    if age < 0: 
        raise NegativeAgeException("Only positive integers are allowed") 
    if age>22: 
        print("Eligible for mrg") 
    else: 
        print("not Eligible for mrg....") 
try:
    num = int(input("Enter your age: ")) 
    status(num) 
except NegativeAgeException:
    print("Only positive integers are allowed") 
except:
    print('something is wrong')
#question 5 
class TooYoungException(Exception):
    def _init_(self,age): 
        self.age=age 
class TooOldException(Exception):
    def _init_(self,age):
        self.age=age 
try:
    age=int(input("Enter Age:"))
if age<18:
    raise YoungException("Plz wait some time ") 
elif age>65:
    raise TooOldException("Your age too old") 
else:
    print('we will find one girl soon') 
except YoungException as e:
    print("Plz wait some time ") 
except OldException as e:
    print("Your age too old ")

#question 6 
try:
    print("outer try block")
    n = int(input("enter a number"))
    print(10/n)
try:
    print("inner try")
    print("anu"+"preet")
except TypeError:
    print("Hello")
else:
    print("inner no exception")
except ArithmeticError:
    print(10/5)
else:
    print("outer no excepiton")
finally:
    print("finally block")
    
#question  7
class Person(object):
    def _init_(self, first, last): 
        self.firstname = first 
        self.lastname = last 
    def Name(self): 
        return self.firstname + " " + self.lastname 
class Employee(Person):
    def _init_(self, first, last, staffnum):
        super()._init_(first,last)
#Person._init_(self,first, last
self.staffnumber = staffnum
    def GetEmployee(self):
        return self.Name() + ", " + self.staffnumber
x = Person("komal", "addanki")
y = Employee("komal", "addanki", "111")
print(x.Name())
print(y.GetEmployee())'''
