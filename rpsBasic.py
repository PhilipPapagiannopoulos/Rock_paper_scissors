import random
import time

y=int(input("Enter the number of rounds you want to play"))

name1 = input("Enter your name:")
name2 = input("Enter the name of your imaginary friend:")
score = 0

win = (name1,"you win")
lose = (name1,"you lose")
draw = ("it's a draw")

X = ["rock", "paper", "scissors"]




for i in range(y):
   choose1 = input("Choose between rock_paper_scissors")
   choose2 = random.choice(X)
   if  choose1 == "rock" and choose2 == "scissors":
    print(name2,"chose",choose2)
    time.sleep(1)
    print(win)
    score += 1
    print(score)
   elif choose1 == "rock" and choose2 == "paper":
    print(name2,"chose",choose2)
    time.sleep(1)
    print(lose)
    score -= 1
    print(score)
   elif choose1 == "scissors" and choose2 == "rock":
    print(name2,"chose",choose2)
    time.sleep(1)
    print(lose)
    score -= 1
    print(score)
   elif choose1 == "paper" and choose2 == "scissors":
    print(name2,"chose",choose2)
    time.sleep(1)
    print(lose)
    score -= 1
    print(score)
   elif choose1 == "rock" and choose2 == "rock":
    print(name2,"chose",choose2)
    time.sleep(1)
    print(draw)
    print(score)
   elif choose1 == "scissors" and choose2 == "paper":
    print(name2,"chose",choose2)
    time.sleep(1)
    print(win)
    score += 1
    print(score)
   elif choose1 == "scissors" and choose2 == "scissors":
    print(name2,"chose",choose2)
    time.sleep(1)
    print(draw)
    print(score)
   elif choose1 == "paper" and choose2 == "rock":
    print(name2,"chose",choose2)
    time.sleep(1)
    print(win)
    score += 1
    print(score)
   elif choose1 == "paper" and choose2 == "paper":
    print(name2,"chose",choose2)
    time.sleep(1)
    print(draw)
    print(score)
   else :
    print("You can only write rock_paper_scissor")

print(name1,"your final score is",score)





