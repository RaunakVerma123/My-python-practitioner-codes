import random
import os

logo = """
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
      |  \/ K|                            _/ |                
      `------'                           |__/           
"""

def clear_console():
  os.system('cls' if os.name == 'nt' else 'clear')

def deal():
  cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
  card=random.choice(cards)
  return card

def calculate_score(list):
  total=sum(list)
  
  if total==21 and len(list)==2:
    return 0

  if 11 in list and total>21:
    list.remove(11)
    list.append(1)
    
  return sum(list)

def compare(u_score,c_score):
  if u_score==c_score:
    print("It's a draw.") 
  elif c_score==0:
    print("Lose,opponent has Blackjack")
  elif u_score==0:
    print("You have a Blackjack,you win!!")
  elif u_score>21:
    print("You went over.You lose")
  elif c_score>21:
    print("Computer went over.You win!!")
  else:
    if u_score>c_score:
      print("You win.")
    else:
      print("You lose.")

def blackjack():
  want_to_play=input("Do you want to play a game of blackjack? Type 'y' or 'n': ").lower()
  if want_to_play=='y':
    clear_console()
    print(logo)
    print("\n")
    end_game=False 
    user_cards=[]
    computer_cards=[]
        
    for add_card in range(2):
      user_cards.append(deal())
      computer_cards.append(deal())
      
    while not end_game:
      user_score=calculate_score(user_cards)
      computer_score=calculate_score(computer_cards)
          
      print(f"Your cards: {user_cards}, current score: {user_score}")
      print(f"Computer's first card: {computer_cards[0]}")
          
      if computer_score==0 or user_score==0 or user_score>21:
        end_game=True
        print(f"Your final hand: {user_cards}, final score: {user_score}")
        print(f"Computer's final hand: {computer_cards}, final score: {computer_score}")
        compare(user_score,computer_score)
        blackjack()
      else:
        user_choice=input("Type 'y' to get another card, type 'n' to pass: ").lower()
        if user_choice=='y':
          user_cards.append(deal())
        else:
          end_game=True
          while computer_score!=0 and computer_score<17:
            computer_cards.append(deal())
            computer_score=calculate_score(computer_cards)
      
          print(f"Your final hand: {user_cards}, final score: {user_score}")
          print(f"Computer's final hand: {computer_cards}, final score: {computer_score}")
          compare(user_score,computer_score)
          blackjack()

blackjack()