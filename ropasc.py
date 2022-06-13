#####This is a game of Rock, Paper and Scissors#####
###This game will be played between the user(Player) and the computer(CPU).

###This will import the 'random' library.
###This 'random' library will help the computer make a random choice from the list in line 9.
print("  This is a game of ROCK, PAPER, SCISSORS!!!")
print("  R stands for ROCK.\n  P stands for PAPER.\n  S stands for SCISSORS.\n")
print("  ENJOY!!!!\n")
import random

while True:
    choices = ["R", "P", "S"]
    CPU = random.choice(choices)
    Player = None

###To loop through the list if the player's choice is not there.
###If not present, the user will be asked to enter a valid input.
    while Player not in choices:
        Player = input("What's your choice? 'R' for rock, 'P' for paper or 'S' for scissors: ").upper()


######To check if the game is a tie######
    if Player == CPU:
        print(f"CPU ({CPU}) : Player ({Player})")
        print("It's a Tie!!!!!")

######To test for ROCK against PAPER and SCISSORS######
######The test will determine whether the player has won or lost if ROCK is chosen######
    elif Player == "R":
        if CPU == "P":
            print(f"CPU ({CPU}) : Player ({Player})")
            print("You lose...")
        if  CPU == "S":
            print(f"CPU ({CPU}) : Player ({Player})")
            print("Yayyy, You win!!!")

    ######To test for PAPER against ROCK and SCISSORS######
    ######The test will determine whether the player has won or lost if PAPER is chosen######
    elif Player == "paper":
        if CPU == "R":
            print(f"CPU ({CPU}) : Player ({Player})")
            print("Yayyy, You win!!!")
        if CPU == "S":
            print(f"CPU ({CPU}) : Player ({Player})")
            print("You lose")

######To test for SCISSORS against PAPER and ROCK######
######The test will determine whether the player has won or lost if SCISSORS is chosen######
    elif Player == "S":
        if CPU == "P":
            print(f"CPU ({CPU}) : Player ({Player})")
            print("Yayyy, You win!!!")
        if CPU == "R":
            print(f"CPU ({CPU}) : Player ({Player})")
            print("You lose")

######To know if the user still wants to play the game.######
###And if the user will no longer play the game, on inputting 'NO' the game will end automatically.
    play_again = input("Will you like to play again? (YES/NO): ").upper()
    if play_again == "NO":
        print("     GAME OVER...    ")
        break

######End of the game###########

