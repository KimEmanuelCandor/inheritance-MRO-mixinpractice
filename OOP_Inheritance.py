#PARENT CLASS
class Person:
  def __init__(self,firstName,lastName):
    self.firstName = firstName
    self.lastName = lastName

  def introduce(self):
    print("Hi I'am " + self.firstName + " " + self.lastName)


#CHILD CLASS
class Student(Person):
  pass

pOne = Person("Kim", "Candor")
pOne.introduce()


sOne = Student("Emanuel","Briones")
sOne.introduce()
