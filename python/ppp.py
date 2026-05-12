from random import randint
status=True
count =0
while status:
    dice1 =randint (1,6)
    dice2= randint (1,6)
    print(f"dice1: {dice1}")
    print(f"dice2: {dice2}")
    if dice1 == dice2:
        print("you win")
        status= False
    else:
        print ("Try again")
        key=input("press any key to roll dices again")