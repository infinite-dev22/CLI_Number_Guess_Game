#importing random module 
import random

#a random integer is chisen by the CPU and stored as guess
guess = random.randint(1, 10)

#adding counter for  the guesses of user
user_guess = 0
guess_no = 0
guess_limit = 5
print("you only have " + str(guess_limit) + " guesses")

#loop to manage user guesses by reducing them when a wrong guess is entered
while user_guess != guess:
    if guess_no != guess_limit:
        user_guess = int(input("\nenter your number guess: "))
        guess_no += 1
        
        #if user guess = guess, print win message
        if user_guess == guess:
            print("\nyou guessed right, you win")
        
        #else print loose message and guesses left
        else:
            print("\nwrong guess, try again")
            guesses_left = guess_no - guess_limit
            print("\nyou are now left with " + str(guesses_left) + " guesses")
            
    #when guess limit =guess no, print user lost, out of guesses        
    else:
        print("\nyou loose, out of guesses, you failed.")
        break
print("\ngame complete")
