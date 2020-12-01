import random

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

game_images=[rock, paper, scissors]

choose = int(input("What do you choose? choose '0' for Rock, '1' for Paper and '2' for Scissors: "))
print(game_images[choose])

print("Computer choose: ")
computer_choose = random.randint(0, 2)
print(game_images[computer_choose])


if choose>=3 or choose<0:
  print("you typed an invalid number, You lose!")
elif (choose==0 and computer_choose==2):
  print("You Win!")
elif computer_choose==0 and choose==2:
  print("You loose")
elif computer_choose > choose:
  print("You lose!")
elif choose > computer_choose:
  print("You win! ")

elif choose==computer_choose:
  print("Its a Draw")




