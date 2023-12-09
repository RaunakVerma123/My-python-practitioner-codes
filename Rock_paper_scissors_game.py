rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

import random

rps_game=[rock,paper,scissors]
game=int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors."))
print(rps_game[game])
print("Computer chose:")
computer=random.randint(0,2)
print(rps_game[computer])
if (game==0 and computer==0)or(game==1 and computer==1)or(game==1 and computer==1):
  print("It's a tie")
elif (game==0 and computer==1)or(game==1 and computer==2)or(game==2 and computer==0):
  print("You lose")
else:
  print("You win")