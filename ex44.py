

class Parent(object):

	def override(self):
		print "PARENT override()"
		# override explicitly

	def implicit(self):
		print "PARENT implicit()"
		# implicit inheritance

	def altered(self):
		print "PARENT altered()"

class Child(Parent):

	def override(self):
		print "CHILD override()"
		# override explicitly

	def altered(self):
		print "CHILD, BEFORE PARENT altered()"
		super(Child, self).altered()
			# gets Parent.altered()
		print "CHILD, AFTER PARENT altered()"

dad = Parent()
son = Child()

dad.implicit()
	#: PARENT implicit()
son.implicit()
	#: PARENT implicit()

dad.override()
	#: PARENT override()
son.override()
	#: CHILD override()

dad.altered()
	#: PARENT altered()
son.altered()
	#: CHILD, BEFORE PARENT altered()
	#: PARENT altered()
	#: CHILD, AFTER PARENT altered()


"""
#
# OVERRIDE EXPLICITLY
#

class Parent(object):

	

class Child(Parent):

	def override(self):
		print "CHILD override()"

dad = Parent()
son = Child()

dad.override()
son.override()


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

"""
