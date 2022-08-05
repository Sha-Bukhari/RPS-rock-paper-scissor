# CODED BY SHA

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


list = [rock,paper,scissors]

### USER CODE
input = input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors: ")
user_input =int(input)
you_chose = list[user_input]


## COMPUTER CODE
out_comes = len(list)-1

random_out_comes = int(random.randint(0,out_comes ))
compu_chose = list[random_out_comes]
print(compu_chose)
print('\ncomputer chose')
print(you_chose)
print('\nyou chose')

# contidiond

# rock = 0
# paper = 1
# scissor = 2

# Rock wins against scissors.
# Scissors win against paper.
# Paper wins against rock.

if random_out_comes == 0 and user_input == 2:
  print('\ncomputer wins')
elif random_out_comes == 2 and user_input == 1:
  print('\ncomputer wins')
elif random_out_comes == 1 and user_input == 0:
  print('\ncomputer wins')
elif random_out_comes == user_input:
  print('\nDraw! Lets play again')
else:
  print('\nYou win!!')
  
