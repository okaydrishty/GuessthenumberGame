import random
toprange= input("set an upperlimit: ")
if toprange.isdigit():
    toprange=int(toprange)
    randomno= random.randint(0, toprange)
    if toprange<=0:
        print("type a number more than 0")
        quit()
else:
    print("enter a number next time")
    quit()
score=0
while True:
    guess=input("guess a number: ")
    if guess.isdigit():
         guess=int(guess)
         score+=1
    else:
        print("Please type a number next time")
        continue
    if guess==randomno:
        print("You won")
        break
    elif guess>=randomno:
        print("Try smaller number")
        continue
    else:
        print("Try larger number")
        continue
print("you took",score,"chances")

