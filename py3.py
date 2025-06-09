import random
rand_1 = random.randint(1,10)
rand_2 = random.randint(1,10)
rand_3 = random.randint(1,10)

random_list = [rand_1, rand_2, rand_3]

while random_list: 
    guess = input("Guess the 3 numbers in the list(between 1 & 10)! Enter your guess: ")



    try:
        guess = int(guess)
        
        if guess == rand_1:
                            random_list.remove(guess)
                            if len(random_list)==0:
                                print("That's the last number! You have guessed all 3. Congrats!")
                            else:
                                print("You guessed a number! It has been removed.") 
        elif guess == rand_2:
                random_list.remove(guess)
                if len(random_list)==0:
                    print("That's the last number! You have guessed all 3. Congrats!")
                else:
                    print("You guessed a number! It has been removed.")
                 
        elif guess == rand_3:
                random_list.remove(guess)
                if len(random_list)==0:
                    print("That's the last number! You have guessed all 3. Congrats!")
                else:
                    print("You guessed a number! It has been removed.")
                    
        elif guess >= 11:
            print("Guess a number between 1 & 10, please.")
        elif guess <= 0:
            print("Guess a number between 1 & 10, please.")

                 
        else:
            print("Your number is not in the list. :(")
        
            
    except:
        
        print("Error! Try again. Enter a number.")
        
            
