# rock paper scissor game:
# where rock r =-1 paper p =0 and scissor s=1

import random
comp=random.choice([-1, 0, 1])
choice=input('''1. Rock
2. Paper 
3. Scissor
Enter your choice:''')
choice=choice.lower()
youDict={
    "rock":-1,
    "paper":0,
    "scissor":1
}
revDict={
    -1:"rock",
    0:"paper",
    1:"scissor"
}
if (choice!="rock" and choice!="paper" and choice!="scissor"):
    print("Please give valid input")
else:
    you=youDict[choice]
    computer=revDict[comp]
    print(f"The computer chose {computer}.")
    if(you==comp):
        print("Its Draw.")
    else:
        if(comp==-1 and you == 1):
            print("You Loose.😢")
        elif(comp == -1 and you == 0):
            print("You win.🎉")

        elif(comp==0 and you == -1):
            print("You Loose.😢")
        elif(comp == 0 and you == 1):
            print("You win.🎉")

        elif(comp==1 and you == -1):
            print("You Loose.😢")
        elif(comp == 1 and you == 0):
            print("You win.🎉")

        else:

            print("Please provide a correct input!")
