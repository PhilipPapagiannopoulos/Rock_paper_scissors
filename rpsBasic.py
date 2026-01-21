import random

y=int(input("Enter the number of rounds you want to play"))

name1 = input("enter your name")
name2 = input("enter your name")
score = 0

win = (name1,"you win")
lose = (name2,"you lose")
draw = ("it's a draw")


for i in range(y):
   choose1 = input("Choose between rock_paper_scissors")
   choose2 = input("Choose between rock_paper_scissors")
   if  choose1 == "rock" and choose2 == "scissors":
    print(win)
   elif choose1 == "rock" and choose2 == "paper":
    print(lose)
   elif choose1 == "scissors" and choose2 == "rock":
    print(lose)
   elif choose1 == "paper" and choose2 == "scissors":
    print(lose)
   elif choose1 == "rock" and choose2 == "rock":
    print(draw)
   elif choose1 == "scissors" and choose2 == "paper":
    print(win)
   elif choose1 == "scissors" and choose2 == "scissors":
    print(draw)
   elif choose1 == "paper" and choose2 == "rock":
    print(win)
   elif choose1 == "paper" and choose2 == "paper":
    print(draw)
   else :
    print("You can only write rock_paper_scissor")







