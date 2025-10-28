#This is like a guess the number game
import random
print("I am thinking of a number")
print("Rules Of Games: Guess the random number in less than 8 chances")
theNum=random.randint(1,21) 
# print(theNum)
i=0
while i<=7: 
    guess=input(f"Take a Guess No. {i+1}: ")
    
    try:
        guess=int(guess)
        if guess==theNum:
            print(f"You Win---Stats\n1.Number of chances you took:{i+1}\n2.Correct Int {guess}")
            i+=1
            break
        elif guess > int(theNum):
            print("Choose smaller Number")
            i=i+1
            continue
        else:
            print("Choose bigger Number")
            i=i+1
            continue
    except ValueError:
        print("You should have choosen a valid value")
if theNum!=guess:
    print("You Exhausted the number of chances")  



