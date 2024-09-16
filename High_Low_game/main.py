import random 
import os
from art import logo
from art import vs
from game_data import data

SCORE=0

def clear_console():
  os.system('cls' if os.name=='nt' else 'clear')

def assign_dictionary(data):
  '''Returns a random dictionary from the list.'''
  return random.choice(data)

def game_structure(a,b):
  '''Prints the basic structure of the game.'''
  print(f"Compare A: {a['name']}, {a['description']}, {a['country']}")
  print(vs)
  print(f"Against B: {b['name']}, {b['description']}, {b['country']}")

def check_answer(a,b):
  '''Checks the greater value and returns 'A' and 'B' accordingly.'''
  if a>b:
    return 'A'
  else:
    return 'B'

def high_low(A,B,score):
  end_of_game=False
  while not end_of_game:
     game_structure(A,B)
     answer=check_answer(A['follower_count'],B['follower_count'])
     user_guess=input("Who has more followers? Type 'A' OR 'B': ").upper()
     clear_console()
     print(logo)

     if answer==user_guess:
      score+=1
      print(f"You got it right! Current score: {score}")
      A=B
      B=assign_dictionary(data)
      while B['follower_count']==A['follower_count']:
        B=assign_dictionary(data)
      high_low(A,B,score)

     else:
        print(f"You lose! Final score: {score}")
        exit()
    
print(logo)
A=assign_dictionary(data)
B=assign_dictionary(data)
while B['follower_count']==A['follower_count']:
  B=assign_dictionary(data)

high_low(A,B,SCORE)