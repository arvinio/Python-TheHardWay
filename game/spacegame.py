from sys import exit
from random import randint

class Scene(object):

	def enter(this):
		print "This scene is not yet configured. Subclass it and implement enter()."
		exit(1)


class Engine(object):

	def __init__(this, scene_map):
		this.scene_map = scene_map
			# Uses var = Engine(scene_map)  

	def play(this):
		current_scene = this.scene_map.opening_scene()
			# From scene_map, get the opening_scene() function
		while True:
			print "\n--------------"
			next_scene_name = current_scene.enter()
				# go to next_scene from current_scene by calling enter() function 
			current_scene = this.scene_map.next_scene(next_scene_name)
				# update current_scene to next_scene
class Death(Scene):

	cheesyPhrases = [
		"You died. You kinda suck at this.",
		"Your mom would be proud...if she were smarter.",
		"Such a luser.",
		"I have a small puppy that's better at this."
	]

	def enter(this):
		print Death.cheesyPhrases[randint(0, len(this.cheesyPhrases)-1)]
		exit(1)

class CentralCorridor(Scene):

	def enter(this):
		print "The Gothons of Planet Percal #25 have invaded your ship and destroyed"
		print "your entire crew. You are the last surviving member and your last"
		print "mission is to get the neutron destruct bomb from the Weapons Armory,"
		print "put it in the bridge, and blow the ship up after getting into an "
		print "escape pod."
		print "\n"
		print "You're running down the central corridor to the Weapons Armory when"
		print "a Gothon jumps out, red scaly skin, dark grimy teeth, and evil clown costume"
		print "flowing around his hate filled body. He's blocking the door to the"
		print "Armory and about to pull a weapon to blast you."

		action = raw_input("> ")

		if action == "shoot":
			print "Quick on the draw you yank out your blaster and fire it at the Gothon."
			print "His clown costume is flowing and moving around his body, which throws"
			print "off your aim. Your laser hits his costume but misses him entirely. This"
			print "completely ruins his brand new costume his mother bought him, which"
			print "makes him fly into a rage and blast you repeatedly in the face until"
			print "you are dead. Then he eats you."
			return 'death'

			"""
			I don't understand how "return death" works. How does the python compiler 
			recognize the string "death" as a function?

			I would think that you had to write:

			return Map.scenes.get(death)
			"""

			# return Map.scenes.get(death)

		elif action == "dodge":
			print "Like a world class boxer you dodge, weave, slip and slide right"
			print "as the Gothon's blaster cranks a laser past your head."
			print "In the middle of your artful dodge your foot slips and you"
			print "bang your head on the metal wall and pass out."
			print "You wake up shortly after only to die as the Gothon stomps on"
			print "your head and eats you."
			return 'death'

			# return Map.scenes.get(death)

		elif action == "tell a joke":
			print "Lucky for you they made you learn Gothon insults in the academy."
			print "You tell the one Gothon joke you know:"
			print "Lbhe zbgure vf fb sng, jura fur fvgf nebhaq gur ubhfr, fur fvgf nebhaq gur ubhfr."
			print "The Gothon stops, tries not to laugh, then busts out laughing and can't move."
			print "While he's laughing you run up and shoot him square in the head"
			print "putting him down, then jump through the Weapon Armory door."
			return 'laser_weapon_armory'

			# return Map.scenes.get(laser_weapon_armory)

		else:
			print "DEOS NOT COMPUTE!"
			return "central_corridor"

			# return Map.scenes.get(central_corridor)


class LaserWeaponArmory(Scene):

	def enter(this):
		pass

class TheBridge(Scene):

	def enter(this):
		pass

class EscapePod(Scene):

	def enter(this):
		pass


class Map(object):

	scenes = {
		"central_corridor": CentralCorridor(),
		"laser_weapon_armory": LaserWeaponArmory(),
		"the_bridge": TheBridge(),
		"escape_pod": EscapePod(),
		"death": Death()
	}

	scenes2 = {"death":Death()}

	def __init__(this, start_scene):
		this.start_scene = start_scene
			# define start_scene 

	def next_scene(this, scene_name):
		return Map.scenes.get(scene_name)
			# directory Map>scenes call scene

	def opening_scene(this):
		return this.next_scene(this.start_scene)
			# call start_scene as param to next scene 


a_map = Map("central_corridor")
a_game = Engine(a_map)
a_game.play()


"""
* Map
	- next_scene
	- opening_scene
* Engine
	- play
* Scene
	- enter
		* Death
		* Central Corridor
		* Laser Weapon Armory
		* The Bridge
		* Escape Pod

Study Notes

__init__ is an example of a constructor

class Person():
	def __init__(this, name):		# 'this' has to be explicitly stated 
		this.name = name 			# e.g. this.name = name

"""

