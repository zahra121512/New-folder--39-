import random 
playing = True
number = str(random.randint(10,20))
print("i will genarate a number to 10 to 20, and you have to guess the number one digit at the time")
print("the game ends when you get one hero!")
while playing:
    guess = input("give me your best guess! \n")
    if number == guess:
      print("you win the game")
      print("the number was",number)
      break
    else:
       print("your guess isn't quite right try again \n")

