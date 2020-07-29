from random import random
num_ran=int(random()*20)
guess=False

print("""Welcome to this game,
here you must guess a number between 0 and 20""")
while not guess:
  character=input("Please type a number ")
  if not character.isdigit():
    print("invalid characters")
  else:
    number=int(character)
    if number<0 or number>20:
      print("you number must be between 0 and 20") 
    elif number==num_ran:
      guess=True;
    elif number<num_ran:
      print("your number is less")
    elif number>num_ran:
      print("your number is greater")
print("congratulations, you guessed \nPD: Orlando es puto")
  
