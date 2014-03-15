# create a mapping of state to abbreviation
states = {
	"Oregon": "OR",
	"Florida": "FL",
	"California": "CA",
	"New York": "NY",
	"Michigan": "MI"
}

# create a basic set of states and some cities in them
cities = {
	"CA": "San Fransisco",
	"MI": "Detroit",
	"FL": "Jacksonville"
}

# add some more cities
cities["NY"] = "New York"
cities["OR"] = "Portland"

# print out some cities
print "-" * 10
print "NY state has: ", cities["NY"]
print "OR state has: ", cities["OR"]

# print every state abbreviation
print "-" * 10
for state, abbrev in states.items():		# since [states] requires 2 params
	print "%s is abbreviated %s" % (state, abbrev)

# safely get an abbreviation by state that might not be there
state = states.get("Texas", None)

if not state:
	print "Sorry, no Texas"



# get a city with a default value
city = cities.get("TX", "Does Not Exist")
print "The city for the state \"TX\" is: %s" %city