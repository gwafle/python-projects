#grace wafle
#1.6.2024
#Rock Paper Scissors
#INIT
import random
shoot = 0
comp = 0
wins = 0
losses = 0
ties = 0


    #FUNCTIONS

def RPS():
    while True:
        print("Welcome to Rock Papper Scisors. You VS. AI ")
        global shoot
        global comp
        global wins
        global losses
        global ties
        shoot = int(input("(Rock = 1, Paper = 2, Scissors = 3) Enter what you would like to play:"))
        if shoot == 1:
            print ("You played ROCK")
        if shoot == 2:
            print("You played PAPER")
        if shoot == 3:
            print("You played SCISSORS")
        print("""Your answer is set.
            The computer is thinking...
            ...
            ...
            ...
            ...""")
        comp = random.randint(1,3)
        if comp == 1:
            print ("The computer played ROCK")
        if comp == 2:
            print ("The computer played PAPER")
        if comp == 3:
            print ("The computer played SCISSORS")

    #def winLoss():

        if comp == shoot:
            ties = ties + 1
            print ("You have won " + str(wins) + " times, tied " + str(ties) + " and lost " + str(losses) + " times.")
            print("You tied would you like to play again?")
            pa = input("yes/no")
            if pa == "no":
                break
        elif comp == 1 and shoot == 2:
            wins = wins + 1
            print ("You have won " + str(wins) + " times, tied " + str(ties) + " and lost " + str(losses) + " times.")
            print("You won would you like to play again?")
            pa = input("yes/no")
            if pa == "no":
                break
        elif comp == 1 and shoot == 3:
            losses = losses + 1
            print ("You have won " + str(wins) + " times, tied " + str(ties) + " and lost " + str(losses) + " times.")
            print("You lost would you like to play again?")
            if pa == "no":
                break
        elif comp == 2 and shoot == 1:
            losses = losses + 1
            print ("You have won " + str(wins) + " times, tied " + str(ties) + " and lost " + str(losses) + " times.")
            print("You lost would you like to play again?")
            if pa == "no":
                break
        elif comp == 2 and shoot == 3:
            wins = wins + 1
            print ("You have won " + str(wins) + " times, tied " + str(ties) + " and lost " + str(losses) + " times.")
            print("You won would you like to play again?")
            if pa == "no":
                break



#MAIN
RPS()








