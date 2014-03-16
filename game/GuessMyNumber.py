from sys import exit
from random import randint

n = randint(1, 10)
maxChances = 5
print "I'm thinking of a number between 1 and 10. You have", maxChances, "chances to guess what it is!"
#print "Answer: %d" %n

guess = int(raw_input("> "))

tries = 1

check = False

""" TODO: Set check for all guesses 

def userInput(self):
        userInput = raw_input("> ")
        return userInput

def getInt(self):
    guess = int(userInput())
    return guess

while check is False:
    if guess <= 1 or guess >= 10:
        print "Oops! I didn't quite catch that. Make sure you choose a number between 1 and 10"
        userInput = raw_input("> ")
        guess = int(userInput)
    if guess >= 1 or guess <= 10:
        check = True
"""

while tries <= maxChances:# and check is True:
    if guess == n:
        print "Correct! :D"
        break
    elif tries == maxChances:
        print "Okay, you suck. I was thinking of %d" % n
        break
    else:
        print "Nope! Try again"
        guess = int(raw_input("> "))
          
    tries += 1
    
#if tries == maxChances:
#    print "Ok, you suck. I was thinking of %d" %n
        
# print "End."