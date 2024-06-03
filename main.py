import rock_paper_scissors_art
import random

computer_choice = random.randint(0, 2)
user_choice = int(input('Enter your choice: 0 for Rock, 1 for Paper, 2 for Scissors: \n'))
print(f'Computer chose: {rock_paper_scissors_art.games_image[computer_choice]}') 
print(f'You chose: {rock_paper_scissors_art.games_image[user_choice]}')
if user_choice==0 and computer_choice==2:
    print('You win')
elif user_choice>2:
    print('Invalid choice. Restart the game')
elif user_choice==2 and computer_choice==0:
    print('You lose')
elif user_choice>computer_choice:
    print('You win')
elif user_choice<computer_choice:
    print('You lose')
elif user_choice==computer_choice:
    print('Its a draw')
                  