from random import randint

print("Welcome to Python Casino")
pc_choice = randint(1, 100)

playing = True

while playing:
  user_choice = int(input("Choose number (1-100):"))
  if user_choice == pc_choice:
    print("You won!")
    playing = False
  elif user_choice > pc_choice:
    print("Lower! Computer chose")
  elif user_choice < pc_choice:
    print("Higher! Computer chose")