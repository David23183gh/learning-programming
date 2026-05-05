from random import randint
status=True
count = 3
while status and count >0:
    dice1 = randint (1,6)
    dice2 = randint (1,6)
    print(f"dice1: {dice1}")
    print(f"dice2: {dice2}")
    if dice1==dice2:
        print("your win")
        status=False
    else:
        print("Try again")
        key=input("press any key to roll dices again ")
        count= (count-1)
        print(f"te quedan {count} giros restantes")
