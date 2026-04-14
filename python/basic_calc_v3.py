import os

#main menu function
def main_menu():
    #main_menu
    print("##main menu##")
    print("[1].adition")
    print("[2]. substraction")
    print("[3].multiplication")
    print("[4].divition")
    print("[5].average")
    print("[6].all operations")
os.system('clear')
#inputs
n1 =float (input("enter fisrt number "))
n2 =float (input("enter second number "))
main_menu()
opt =int(input("enter any option:"))
if (opt==1):
    add= n1 +n2
    print (f"add is: {add}")
if (opt==2):
    subs= n1 -n2
    print (f"subs is: {subs}")
if (opt==3):
    mult= n1 *n2
    print (f"subs is: {mult}")
if (opt==4):
    div= n1 /n2
    print (f"subs is: {div}")
if (opt==5):
    avg= (n1+n2)/2 
    print (f"subs is: {avg}")
if (opt==6):
    any= n1 +n2
    print (f"subs is: {add}")