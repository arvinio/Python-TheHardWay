"""
from sys import argv

script, filename = argv
		# use argv to get filename
txt = open(filename)
		# opens filename
print "Here's %r..." % filename
print txt.read()
		# do the read command with no params
"""
print "Enter file to open:"

# print "Type the filename again:"
file_again = raw_input("> ")

txt_again = open(file_again)

print txt_again.read()

txt_again.close()