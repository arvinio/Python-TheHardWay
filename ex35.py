from sys import exit

def gold_room():
	print "This room is full of gold. How much do you take?"

	next = raw_input("> ")
	if "0" in next or "1" in next:
		how_much = int(next)
	else:
		dead("Man, learn to type a number.")

	if how_much < 50:
		print "Nice, you're not too greedy, you win!"
		exit(0)
	else:
		dead("You greedy bastard!")


def bear_room():
	print "There is a bear here."
	print "The bear has a bunch of honey."
	print "The fat bear is in front of another door."
	print "How are you going to move the other bear?"
	bear_moved = False

	while True:
		next = raw_input("> ")

		if next == "take honey":
			dead("The bear kills you.")
		elif next == "taunt bear" and not bear_moved:
			print "The bear has moved. Get through the door quickly!"
		elif next == "taunt bear" and bear_moved:
			print "The bear kills you."
		elif next == "open door" and bear_moved:
			gold_room()
		else:
			print "I got no idea what that means."



def cthulhu_room():
	print "Here you see the evil monster Cthulhu."
	print "Do you flee or eat yourself to death?"

	next = raw_input("> ")

	if "flee" in next:
		start()
	elif "head" in next:
		dead("Well that was tasty!")
	else:
		cthulhu_room()

def dead(why):
	print why, "Good job!"
	exit(0)

def start():
	print "You are in a dark room."
	print "There is a door to your right and left."
	print "Which one do you take?"

	next = raw_input("> ")

	if next == "left":
		bear_room()
	elif next == "right":
		cthulhu_room()
	else:
		dead("You stumble around the room until you starve.")




start()