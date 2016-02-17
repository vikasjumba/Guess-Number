# http://www.codeskulptor.org/#user40_GW7zWespRmKyHM3.py

# template for "Guess the number" mini-project
# input will come from buttons and an input field
# all output for the game will be printed in the console
try:
    import simplegui
except ImportError:
    import SimpleGUICS2Pygame.simpleguics2pygame as simplegui
import random
import math

secret = None
range = 100
remainingGuessCount = None
# helper function to start and restart the game
def new_game():
    # initialize global variables used in your code here
    global secret
    secret = random.randrange(0,range)
    global remainingGuessCount
    remainingGuessCount = int(math.ceil(math.log(range,2)))
    print "New game starts. Range is from 0 to", range
    print "Number of Guesses is", remainingGuessCount
    print ""


# define event handlers for control panel
def range100():
    # button that changes the range to [0,100) and starts a new game     
    global range
    range = 100
    new_game()


def range1000():
    # button that changes the range to [0,1000) and starts a new game     
    global range
    range = 1000
    new_game()
    
def input_guess(guess):
    # main game logic goes here
    global remainingGuessCount
    remainingGuessCount -= 1
    guess = int(guess)
    print "Guess was", guess
    print "Number of remaining guesses",remainingGuessCount
    isGameEnd = False
    if guess == secret:
        print "Correct!"
        isGameEnd = True
    elif remainingGuessCount == 0:
        print "Computer Wins! The secret number was", secret
        isGameEnd = True
    elif guess > secret:
        print "Lower!"
    else:   
        print "Higher!"
    print ""
    if isGameEnd:
       new_game() 
# create frame
frame = simplegui.create_frame("Guess the number",200,200)

# register event handlers for control elements and start frame
frame.add_button('Range: 0 - 100',range100,200)
frame.add_button('Range: 0 - 1000',range1000,200)
frame.add_input('Enter a guess',input_guess,200)

# call new_game 
new_game()
frame.start()

# always remember to check your completed program against the grading rubric

