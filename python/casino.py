##import libraries or packages
from random import randint

#declare and initialize variables and/or constants
dice1=0
dice2=0
lives=3
acum_dices=0
roll_count=0
equal_counter=0
status=True
player_lives=3

#Functions 
def rollDices():
    dice1=randint(1,6)
    dice2=randint(1,6)
    return dice1, dice2

#main 
print(":::WELCOME TO CASINO:::")
press_key=input("\nPress any key to start the game :::")
while status:
    ##os.system('cls')
    dices=rollDices()
    roll_count+=1
    dices_add=0
    print("#"*20)
    print(f"Roll dices n°: {roll_count}")
    print(f"player lives: {lives}")

    if acum_dices > 14:
        dicex=dices[randint(0,1)]
        print(f"Dice: {dicex}")
    else:
        print(f"dice1: {dices[0]}")
        print(f"dice2: {dices[1]}")
        dices_add=dices[0] + dices[1]
        acum_dices += dices_add

    if acum_dices >= 20:
        print("::congratulations you ve win::")
        break

    if dices_add % 2 !=0:
        player_lives-=1
        print(f"you've lost one live, now you have {player_lives} lives")
        if player_lives==0:
            print("Game over")
            break


    if dices[0]==6 and dices [1] ==6 or dices[0]==1 and dices[1] == 1:
        player_lives+=1
        print("you 've win one live::: ")
    
    print(f"dices addition: {dices_add}")
    print(f"Dices acum: {acum_dices}")

    if player_lives==0:
        print(":::Game over:::")
        print(f"Total roll count: {roll_count}")
    
    if roll_count==5:
        break
    else:
        press_key=input("\npress any key to roll dices again")

#Counter equal dices consecutivos *3 -> you win 
#if addition [d1 and d2] is odd lose 1 live 
#if lives = 0 -> Game over
#if d1 and d2 equal six -> add 1 live 