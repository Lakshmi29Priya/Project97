import random
print("Number guessing game")
number= random.randint(1,9)
chances=5
print("Guess a number between 1 to 9")
while chances>0:
    guess=int(input("Enter your guess:"))
    if guess<number:  
        print("Your guess was too low.Guess a number higher than",guess)      
    elif guess>number:
        print("Your guess was too high.Guess a number lesser than ",guess)
    else:
        if not chances==1:
          print("You win")
          print("The number has changed.Find the new number with the remaining",chances-1,"chances") 
          number=random.randint(1,9)
        if chances==1:
            print("You win")
            print("You have no more chances to continue playing")
            break
    chances-=1
     
if not chances>0:
   print("You lose.The number is",number)
