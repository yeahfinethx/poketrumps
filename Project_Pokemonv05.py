# Project Brief: Top Trumps

# In this project you'll create a small game where players compare stats, similar to the Top Trumps card game. The basic flow of the games is:
    # You are given a random card with different stats
    # You select one of the card's stats
    # Another random card is selected for your opponent (the computer)
    # The stats of the two cards are compared
    #The player with the stat higher than their opponent wins
# The standard project will use the Pokemon API, but you can use a different API if you want after completing the required tasks.

# Required Tasks
# These are the required tasks for this project. You should aim to complete these tasks before adding your own ideas to the project.
    # Generate a random number between 1 and 151 to use as the Pokemon ID number

# First, we import the two types of libraries we are using, random (for random integers) and requests (for accessing the PokeAPI)
import random
import requests

# As a modification to the assignment, we ask the player how many rounds they would like to play using INPUT and force it into an integer using INT.
# Additionally, we validate the response and return an error if the value returned is not an integer using a TRY function embedded in a WHILE loop. See https://www.w3schools.com/python/python_try_except.asp for more information.
while True:
    try:
        rounds = int(input("How many rounds of PokeTrumps would you like to play? "))
        print()
    except ValueError:
        print("Sorry, please enter a numerical value.\n")
        continue
    else:
        break

# We defined player scores here, outside of any functions, so we can add to these base scores later.
p1score = 0
p2score = 0
# Here we're creating the file, wiping it clean, and adding a header.
with open('pokescore.txt', 'w+') as poke_file:
    poke_file.write('Poketrumps Score Sheet\n')

# We defined a function in the form of gameround(), which allows us to call gameround() each time we want to start a new round.
def gameround():
    # We have left unfinished code intentions here. We are calling a random sample of two numbers and assigning one each to the players, but our original goal was to use this to ensure we don't repeat the same number twice.
    deck = random.sample(range(1,151),2)
    player1 = deck[0]
    # We're using global here to declare to the code that even thought p1score and p2score are in this function, they are globally referenced throughout our code.
    global p1score
    global p2score

    # Using the Pokemon API get a Pokemon based on its ID number
    url1 = 'https://pokeapi.co/api/v2/pokemon/{}/'.format(player1)
    response_p1 = requests.get(url1)
    pokemon_p1 = response_p1.json()

    # Create a dictionary that contains the returned Pokemon's name, id, height and weight (★https://pokeapi.co/)
    player1_card = {
        'name' : pokemon_p1['name'],
        'id' : pokemon_p1['id'],
        'height' : pokemon_p1['height'],
        'weight' : pokemon_p1['weight'],
        }
    # Worth calling out some fancy footwork here that Rob helped us with. The formatting below is how we've gotten the output to display so nicely for the Pokemon's stats.
    print("Your Pokemon for this round is: {}.\nID:{}\nHEIGHT:{}\nWEIGHT:{}\n".format(player1_card['name'].title(),player1_card['id'],player1_card['height'],player1_card['weight']))


    # Get a random Pokemon for the player and another for their opponent
    player2 = deck[1]

    url2 = 'https://pokeapi.co/api/v2/pokemon/{}/'.format(player2)
    response_p2 = requests.get(url2)
    pokemon_p2 = response_p2.json()
    player2_card = {
        'name' : pokemon_p2['name'],
        'id' : pokemon_p2['id'],
        'height' : pokemon_p2['height'],
        'weight' : pokemon_p2['weight'],
        }

    print("Your opponent has {}.\n".format(player2_card['name'].title()))
    # Ask the user which stat they want to use (id, height or weight)
    # Modification (unfinished) - we are in the process of trying to validate the response from the input

    global pokestat
    pokestat = input("Which stat do you want to compare? height, weight, id: ")

    while pokestat not in ('height', 'weight', 'id'):
        pokestat = input("Sorry, please enter either height, weight or id: ")


    # Here we are defining variables for comparison and assigning them to player1_card using the stat the player chose earlier in the game.
    pokestat_p1 = player1_card[pokestat]
    pokestat_p2 = player2_card[pokestat]

    # Compare the player's and opponent's Pokemon on the chosen stat to decide who wins
    if pokestat_p1 > pokestat_p2:
        print("You win round {}! Your {} stat of {} beat player two's {}.".format(round, pokestat, pokestat_p1, pokestat_p2))
        p1score = p1score+1
        print("The score is now P1: {} - P2: {}\n".format(p1score,p2score))
    elif pokestat_p1 == pokestat_p2:
        print("You tied round {}! Your {} stat of {} is the same as player two's {}.".format(round, pokestat, pokestat_p1, pokestat_p2))
        print("The score is now P1: {} - P2: {}\n".format(p1score,p2score))
    else:
        print("You lost round {}! Your {} stat of {} did not beat player two's {}.".format(round, pokestat, pokestat_p1, pokestat_p2))
        p2score = p2score+1
        print("The score is now P1: {} - P2: {}\n".format(p1score,p2score))
# This is how we're saving the scores into a file. 'a' will append the file. It will also create a file if one doesn't exist.
    with open('pokescore.txt', 'a') as poke_file:
        poke_file.write('P1: '+str(p1score)+' - P2: ')
        poke_file.write(str(p2score)+'\n')

# This bit of code is what repeats the game for the input number of times
def totalrounds():
    global round
    for round in range(rounds):
        round = round+1
        gameround()
    print("============================================")
    again = input("Would you like to play again? y/n ")

    #If the player says yes, we run another set of rounds equal to the number the player chose at the beginning.
    if again == 'y':
        totalrounds()
    else:
        print("Thanks for playing!")

totalrounds()



# Ideas for Extending the Project
# Here are a few ideas for extending the project beyond the required tasks. These ideas are just suggestions, feel free to come up with your own ideas and extend the program however you want.
    # Use different stats for the Pokemon from the API
    # Get multiple random Pokemon and let the player decide which one that they want to use
    # Play multiple rounds and record the outcome of each round. The player with most number of rounds won, wins the game
    # Allow the opponent (computer) to choose a stat that they would like to compare
    # Record high scores for players and store them in a file
    # Use a different API (see suggestions below)
