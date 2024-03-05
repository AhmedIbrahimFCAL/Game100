# Author: Ahmad_ibrahim_AbuDanckash
# Under the supervision of the assistant professor: Dr. Mohammed_El_Ramly
# Purpose: The player who reaches 100 wins. the main purpose make the players make sure of the idea of reaching the win and to ensure success from the start.




# Functions Definition
def chick_input(count,sel):

    # We will detect from the input of the user if it is number or no
    if sel!="1" and sel!="2" and sel!="3" and sel!="4" and sel!="5" and sel!="6" and sel!="7" and sel!="8" and sel!="9" and sel!="10" or sel=="":
        print("Your input is not valid.")
        return True

    sel=int(sel)

    # We will detect from if the summation is greater than 100 or no
    if count+sel > 100:
        print("You can not exceed 100.\nYou can enter",100-count,"to be successful. 'If you want so!'")
        return True


# The main program
# we will print welcome message to users and instruct them how play.
print("\n\t\t\t\t\t\t**********************\n\t\t\t\t\t\t Welcome to 100_Game!\
\n\t\t\t\t\t\t**********************\n\nTwo players start from 0 and alternatively\
 add a number 1 to 10 to the sum.\nThe player who reaches 100 wins.")
input("\nAre you ready, Friends?\nLet's press Enter to start! ")

# we made count for two players to store their points earned.
count = 0

# We will get the names of the two players
p1=input("\nThe first player,\nPlease, enter your name: ").strip().title()
if p1=="":
    p1="The first player"
p2=input("\nThe second player,\nPlease, enter your name: ").strip().title()
if p2=="":
    p2="The second player"
elif p1==p2:
    p2=p2+"_2"


while True:

    # we made sel to input from users and we select one variable to save the memory area.
    sel=input(f"\nWe have {count}\n{p1},\nPlease, enter a number from 1 to 10: ").strip()
    # We will detect from the input and till there is not existing crush.
    while chick_input(count,sel):
        sel=input(f"{p1},\nPlease, enter a number from 1 to 10: ").strip()
    count+=int(sel)

    # we set if condition to make sure from winning the player1.
    if count==100:
        print(f"\nNow, we have {count}\n\n\n\t\t\t\t\t\t\t\t******************\n\t\t\t\t\t\t\t\t Congratulations!\n\t\t\t\t\t\t\t\t******************\n\n\t{p1} is winner.\n\nThanks for using my program. See You Soon!")
        break

    # We will take number from the second player
    sel = input(f"\nWe have {count}\n{p2},\nPlease, enter a number from 1 to 10: ").strip()
    # We will detect from the input and till there is not existing crush.
    while chick_input(count,sel):
            sel = input(f"{p2},\nPlease, enter a number from 1 to 10: ").strip()

    count += int(sel)
    #we set if condition to make sure from winning the player2.
    if count == 100:
        print(f"\nNow we have {count}\n\n\n\t\t\t\t\t\t\t\t******************\n\t\t\t\t\t\t\t\t Congratulations!\n\t\t\t\t\t\t\t\t******************\n\n\t{p2} is winner.\n\nThanks for using my program. See You Soon!")
        break

# Thanks for reading my code. See You Soon!