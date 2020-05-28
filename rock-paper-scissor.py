from random import randint
from flask import Flask
import sys

app = Flask(__name__)

@app.route('/')
loop = True
player_score = 0
computer_score = 0


def scoreboard():
    print("-----Scores-----")
    print("Player:", player_score)
    print("Computer:", computer_score)
    print("----------------")


def options():
    print("Enter 1 to select Stone")
    print("Enter 2 to select Paper")
    print("Enter 3 to select Scissor")


def point(x, y):
    global player_score
    global computer_score

    if x == 1 and y == 1:
        print("=> Round Draw")
    elif x == 1 and y == 2:
        print("=> Computer wins this round")
        computer_score += 1
    elif x == 1 and y == 3:
        print("=> Player wins this round")
        player_score += 1
    elif x == 2 and y == 1:
        print("=> Player wins this round")
        player_score += 1
    elif x == 2 and y == 2:
        print("=> Round Draw")
    elif x == 2 and y == 3:
        print("=> Computer wins this round")
        computer_score += 1
    elif x == 3 and y == 1:
        print("=> Computer wins this round")
        computer_score += 1
    elif x == 3 and y == 2:
        print("=> Player wins this round")
        player_score += 1
    elif x == 3 and y == 3:
        print("=> Round Draw")


print("Welcome to Stone|Paper|Scissor")
ip = input("Enter 1 to Play: ")
if ip != "1":
    print("1 not Entered. Exiting Game....")
    sys.exit()
print("----------------")
print("First to reach 3 points wins")
print("----------------")
while loop:
    options()

    try:
        a = int(input())
    except:
        print("Please enter a value from: 1,2,3!")
        continue
    print("----------------")
    if a == 1:
        print("Player has chosen Stone")
    elif a == 2:
        print("Player has chosen Paper")
    elif a == 3:
        print("Player has chosen Scissor")
    else:
        print("Please enter a value from: 1,2,3!")
        continue
    b = randint(1, 3)
    if b == 1:
        print("Computer has chosen Stone")
    elif b == 2:
        print("Computer has chosen Paper")
    elif b == 3:
        print("Computer has chosen Scissor")

    point(a, b)
    scoreboard()
    if player_score > 2 or computer_score > 2:
        loop = False

if player_score > computer_score:
    print("Congratulations! You win the Game! :)")
else:
    print("Computer wins the Game. Better luck next time :(")

if __name__ == '__main__':
    app.run(debug=True)
