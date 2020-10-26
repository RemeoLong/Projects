#Date: 8/19/2020
import random

dice1 = random.randint(0, 6)
dice2 = random.randint(0, 6)
player1_name = ""
player2_name = ""

player1_name = input("Player 1, please enter your name: ")
print("Roll the Dice " + player1_name)
print("Rolling Dice...")
print(int(dice1))

player2_name = input("Player 2, please enter in your name: ")
print("Roll the Dice " + player2_name)
print("Rolling Dice...")
print(int(dice2))

if dice1 == dice2:
    print("It was a TIE!")
elif dice1 < dice2:
    print(player2_name + ", you win!")
elif dice1 > dice2:
    print(player1_name + ", you win!")
