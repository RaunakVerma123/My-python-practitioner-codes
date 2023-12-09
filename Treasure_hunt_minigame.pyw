print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 

vehicle=input ("Which vehicle do you want to choose?Car or Bike?")
l_vehicle=vehicle.lower()
if l_vehicle=='car':
    direction=input("Which way do you want to go?..Left or Right?")
    l_direction=direction.lower()
    if l_direction=='left':
        print("There was a huge cliff in front of you....You couldnt manage to stop the vehicle in time and fell of the cliff.\033[1mGame over!!\033[0m")
    elif l_direction=='right':
        print("As you drove through the jungle,you saw a giant monster emerge from a clump of trees shaking the ground with each step it took as it started chasing you.You started driving faster and saw the entrance to a temple on the left side.")
        decision=input("Would you enter the temple or continue forward?..(Temple)or(Forward)?")
        l_decision=decision.lower()
        if l_decision=='temple':
            print("Upon entering the temple you see a tunnel on both the sides.Debris starts falling from the roof of the temple!Looks like this place will collapse anytime,Hurry!!!Which way will you go?")
            semi_final=input("Left or Right?")
            l_semi_final=semi_final.lower()
            if l_semi_final=='left':
                print("Continuing left and seeing the exit in front,you start running towards the exit but that is when you pass by a room and see a bright light emerging from it.It's the Treasure room!This is the treasure you have been searching for all these years.But the place might collapse anytime soon!!!\033[1mWould you risk taking the treasure with you or leave immediately?!\033[0m")
                final=input("Exit or Treasure ?")
                l_final=final.lower()
                if l_final=='exit':
                    print("\033[1mCONGRATULATIONS!!!\033[0mYou have managed to survive the horrors of this place for now.Find out what awaits you in the next part.\033[1mTO BE CONTINUED.....\033[0m")
                elif l_final=='treasure':
                    print("You get captivated by the riches and try to quickly collect as many valuables as you can and escape.But before you can make it to the exit the entire place collapses causing your demise.You are dead.\033[1mGame Over!!!\033[0m")
                else:
                    print("Please start over and choose from the given option.") 
            elif l_semi_final=='right':
                print("As you take a right,the tremors intensify causing the tunnel to start collapsing!You turn around and sprint as fast as you can narrowly escaping being crushed.Looks like you have no choice but to go left.")
                no_choice=input("Type left to continue.")
                l_no_choice=no_choice.lower()
                if l_no_choice=='left':
                    print("Continuing left and seeing the exit in front,you start running towards the exit but that is when you pass by a room and see a bright light emerging from it.It's the Treasure room!This is the treasure you have been searching for all these years.But the place might collapse anytime soon!!!\033[1mWould you risk taking the treasure with you or leave immediately?!\033[0m")
                    final=input("Exit or Treasure ?")
                    l_final=final.lower()
                    if l_final=='exit':
                        print("\033[1mCONGRATULATIONS!!!\033[0mYou have managed to survive the horrors of this place for now.Find out what awaits you in the next part.\033[1mTO BE CONTINUED.....\033[0m")
                    elif l_final=='treasure':
                        print("You get captivated by the riches and try to quickly collect as many valuables as you can and escape.But before you can make it to the exit the entire place collapses.As you draw your last breath,you realise that it is not the rubble you are buried underneath that is going to cause your demise but your greed.You are dead.\033[1mGame Over!!!\033[0m")
                    else:
                        print("Please start over and choose from the given option.") 
            else:
                print("Please start over and choose from the given option.")             
        elif l_decision=='forward':
            print("You continue driving at full speed thinking that you will be able to escape from the clenches of the behemoth when suddenly another giant monster appears in front of you!!You are unable to turn the vehicle on time as the monster stomps on the vehicle crushing the car and you along with it.You are dead.\033[1mGame over!!\033[0m") 
        else:
            print("Please start over and choose from the given option.")   
elif l_vehicle=='bike':
     direction=input("Which way do you want to go?..Left or Right?")
     l_direction=direction.lower()
     if l_direction=='left':
         print("There was a huge cliff in front of you....You couldnt manage to stop the vehicle in time and fell of the cliff.\033[1mGame over!!\033[0m")
     elif l_direction=='right':
         print("As you drove through the jungle,you saw a giant monster emerge from the clump of trees shaking the ground with each step it took as it started chasing you.The sudden shaking caused you to loose balance and you fell from the bike head first breaking your neck in the process.You are dead.\033[1mGame over!!\033[0m")
else:
    print("Please start over and choose from the given option.") 