import random


while True:
 action = ("\nEnter a choice : (rock , paper or scissor.)")
 print(action)
 user_action = input("\nComputer chose : \nYou chose :")
 possible_actions= ['rock', 'paper', 'scissor']
 computer_action = random.choice(possible_actions)
 print(f"\nYou chose: {user_action} \nComputer chose: {computer_action}")


 if user_action == computer_action:
  print("The game is tie!")
 elif user_action == 'rock':
   if computer_action == 'scissor':
          print("You Win!")
   else:
          print("Computer Win!")
 elif user_action == 'paper':
     if computer_action == 'rock':
          print("You Win!")
     else:
          print("Computer Win!")  
 elif user_action == 'scissor':
     if computer_action == 'paper':
          print("You Win!")       
     else:
          print("Computer Win!")  
 
    
 play_again = input("\nYou want to play again : (yes/no) : ")
 if play_again == 'yes':
     print("Enjoy playing again!")
 else:
     print("\nThankyou for playing!")
     break