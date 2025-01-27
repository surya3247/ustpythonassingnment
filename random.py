import random

def guess_Game():

  lucky = int(input("Enter your lucky number between 1 and 10: "))

  while True:
    rand = random.randint(1, 10)
    print("Generated random number:",rand)
    if rand == lucky:
      print("Congratulations!")
      break

guess_Game()
