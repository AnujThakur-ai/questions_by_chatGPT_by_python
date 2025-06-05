# guess number
from random import randint


# print(comp_n)


loose_count =0
win_count = 0
while True:
    comp_n = randint(1,100)# to guess a new number each time
    
    try:
        guessed_n = int(input("\n Guess a number (1-100):\t"))
        if guessed_n < 0 or guessed_n > 100:
            print("wrong input!!")
            continue
        
        if guessed_n !=comp_n:
            loose_count +=1
            print(f"you lose!, the number was {comp_n} ")
        else:
            win_count +=1
        
            print(f"you guessed it!!, you win")
            
        print("\n")
        print(f" {win_count} || {loose_count}")
        
    except ValueError:
        print("Invalid input!!, guess again")
        