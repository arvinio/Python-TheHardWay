""" 
# Assignment code #

from sys import argv		# argv = argument variable

script, first, second, third = argv		# unpack argv into these 4

print "The script is called: ", script
print "Your first variable is: ", first
print "Your second variable is: ", second
print "Your third variable is: ", third

# My code is below #
"""

from sys import argv		# argv = argument variable

first_arg, second, third, fourth = argv		# unpack argv into these 4

first_arg = raw_input("Enter name of script: ")

print
print "The script is called: ", first_arg
print "Your first variable is: ", second
print "Your second variable is: ", third
print "Your third variable is: ", fourth