## Animal is-a object
class Animal(object):
	pass

## Dog is-a Animal
class Dog(Animal):

	def __init__(self, name):
		## Dog has-a name
		self.name = name

## Cat is-a Animal
class Cat(Animal):

	def __init__(self, name):
		## Cat has-a name
		self.name = name

## Person is-a object
class Person(object):

	def __init__(self, name):
		## Person has-a name
		self.name = name

		## Person has-a pet
		self.pet = None

## Employee is-a person
class Employee(Person):

	def __init__(self, name, salary):
		## Employee has-a name
		super(Employee, self).__init__(name)
		## Employee has-a salary
		self.salary = salary

## Fish is-a object
class Fish(object):
	pass

## Salmon is-a fish
class Salmon(Fish):
	pass

## Halibut is-a fish
class Halibut(Fish):
	pass


## rover is-a Dog
rover = Dog("Rover")

## satan is-a Cat
satan = Cat("Satan")

## mary is-a person
mary = Person("Mary")

## From Mary get the Pet attribute and name it satan
mary.pet = satan

## frank is-a employee with name Frank and salary 120000 
frank = Employee("Frank", 120000)

## Frank has pet attribute named Rover
frank.pet = rover

## flipper is-a fish
flipper = Fish()

## crouse is-a salmon
crouse = Salmon()

## harry is-a Halibut
harry = Halibut()