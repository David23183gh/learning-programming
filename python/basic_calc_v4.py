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
if (opt ==1):
    add = n1 + n2
    print(f"addition is: {add}")
else:
    if (opt==2):
        subs=n1-n2
        print(f"substracttion is: {subs}")
    else:
        if (opt==3):
            mult= n1 *n2
            print (f"mult is: {mult}")
        else:
            if (opt==4):
                div= n1 /n2
                print (f"divition is: {div}")
            else:
                if (opt==5):
                    avg= (n1+n2)/2 
                    print (f"average is: {avg}")
                else:
                    if (opt==6):
                         add = n1 + n2
                         subs=n1-n2
                         mult= n1 *n2
                         div= n1 /n2
                         avg= (n1+n2)/2 
                         print(f"addition is: {add}")
                         print(f"substracttion is: {subs}")
                         print (f"mult is: {mult}")
                         print (f"divition is: {div}")
                         print (f"average is: {avg}")