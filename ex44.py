"""


#
# IMPLICIT INHERITANCE
#

class Parent(object):

	def implicit(self):
		print "PARENT implicit()"

class Child(Parent):
	pass

dad = Parent()
son = Child()

dad.implicit()
son.implicit()


"""

"""
#
# OVERRIDE EXPLICITLY
#

class Parent(object):

	def override(self):
		print "PARENT override()"

class Child(Parent):

	def override(self):
		print "CHILD override()"

dad = Parent()
son = Child()

dad.override()
son.override()

"""

#
# ALTER BEFORE OR AFTER
#

class Parent(object):
	
	def altered(self):
		print "PARENT altered()"

class Child(Parent):
	def altered(self):
		print "CHILD, BEFORE PARENT altered()"
		super(Child, self).altered()
			# gets Parent.altered()
		print "CHILD, AFTER PARENT altered()"

dad = Parent()
son = Child()

dad.altered()
son.altered()
