ten_things = "Apples Oranges Crows Telephone Light Sugar"
print "Here's a list of ten things: %r" %ten_things

print "Wait there's not 10 things in that list, let's fix that."

stuff = ten_things.split(" ")
more_stuff = ["Day", "Night", "Song", "Frisbee", "Corn", "Banana", "Girl", "Boy"]

while len(stuff) != 10:
	next_one = more_stuff.pop()		# .pop() cuts out last element from list
	print "Adding: ", next_one
	stuff.append(next_one)			# .append() adds param to list as last element 
	print "There's %d items now." % len(stuff)

print "There we go: ", stuff

print "Let's do some thing with this stuff."

print stuff[1]
print stuff[-1] # whoa! fancy
print stuff.pop()
print " ".join(stuff) # what? cool!
print "#".join(stuff[3:6]) # super stellar!