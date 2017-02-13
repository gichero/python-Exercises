

def playAgain():

    while True:

        x = raw_input("Do you want to play again (Y or N)? ").upper()

        if x == "Y":
            return True

        elif x == "N":
            return False
            break

playAgain()
