# Rock - Paper - Scissor Game

# Rules: Pick between Rock, Paper, or Scissors
# Rock beats Scissors, Scissors beats Paper, and Paper beats Rock

player1 = ""
player2 = ""
choice_1 = ""
choice_2 = ""
score_1 = 0
score_2 = 0
answer_1 = "Y", "y", "N", "n"

print("Welcome to Rock-Paper-Scissors. First one to win", 3, "games will win. Good Luck and Have Fun!")
player1 = input("Player 1,  please enter your name: ")
player2 = input("Player 2, please enter your name: ")

while True:
    if score_1 != 3 or score_2 != 3:
        print("Score: " + player1 + " = ", score_1)
        print("Score: " + player2 + " = ", score_2)
        choice_1 = input(player1 + " Please choose between: Rock, Paper, or Scissor. ")
        choice_2 = input(player2 + " Please choose between: Rock, Paper, or Scissor. ")
        if choice_1 == "Rock" and choice_2 == "Scissor":
            score_1 += 1
            print("Rock smashes Scissor, Point goes to " + player1)
        elif choice_1 == "Paper" and choice_2 == "Rock":
            score_1 += 1
            print("Paper wraps Rock , Point goes to " + player1)
        elif choice_1 == "Scissor" and choice_2 == "Paper":
            score_1 += 1
            print("Scissor cut Paper, Point goes to " + player1)
        elif choice_2 == "Rock" and choice_1 == "Scissor":
            score_2 += 1
            print("Rock smashes Scissor, Point goes to " + player2)
        elif choice_2 == "Paper" and choice_1 == "Rock":
            score_2 += 1
            print("Paper wraps Rock , Point goes to " + player2)
        elif choice_2 == "Scissor" and choice_1 == "Paper":
            score_2 += 1
            print("Scissor cut Paper, Point goes to " + player2)
        elif choice_1 == choice_2:
            print("Its a Tie, No One is awarded a point. Next Round. ")
        else:
            print("Please choose only between Rock, Paper, or Scissor. ")
    if score_1 == 3:
        print(player1 + " won 3 games first and therefore is the WINNER!!! ")
        break
    elif score_2 == 3:
        print(player2 + " won 3 games first and therefore is the WINNER!!! ")
        break
input("Would you like to play again? ")
if answer_1 == "Y" or "y":
    print("Too Bad.. Go Play something else.. HAHA!!")
else:
    print("Well.... Have fun playing something else!!")








