import random
import hangman_art

border = ("\033[0;32m-----------------------------------------------------\033[0m")

end_of_game = False
lives = 6
word_list = ["elephant", "rainbow", "computer", "sunshine", "guitar", "butterfly", "adventure", "chocolate", "library", "universe", "python", "jazz", "flower", "mountain", "mystery", "penguin", "paradox", "infinity", "dragon","dolphin"]
chosen_word = random.choice(word_list)
word_length = len(chosen_word)
    
print (border,"\033[0;36m")
print (hangman_art.logo)
print ("\033[0m")
print (border)

display = []
guessed_letters = []
for _ in range(word_length):
    display += "_"

while not end_of_game:
    print("\033[1;33mThe word is: \n")
    print(f"{' '.join(display)}\n")
    guess = input("\033[1;35mGuess a letter:\033[0m ").lower()
    print (border)

    #If the user has entered a letter they've already guessed, print the letter and let them know.

    if guess.isalpha()==False:
        print("\033[0;31mERROR!\033[0m Please enter a letter!")
        print(border)
    elif len(guess) == 1:
        if guess in display:
            print (f"You've already guess the letter {guess}")
        #Check guessed letter
        for position in range(word_length):
            letter = chosen_word[position]
            if letter == guess:
                display[position] = letter

        #Check if user is wrong.
        if guess in guessed_letters:
                print ("You already guessed that letter. Try Again")
        elif guess not in chosen_word:
            print (f"You guess {guess}, that's not in the word. \033[0;31mYou lose a life\033[0m")
            
            guessed_letters.append(guess)
            lives -= 1
            if lives == 0:
                end_of_game = True
                
                print(f"The word is \033[0;36m{chosen_word}\033[0m")
                print("\033[0;31mYou lose.\033[0m")
                
            #Join all the elements in the list and turn it into a String.
    

            #Check if user has got all letters.
        if "_" not in display:
            end_of_game = True
            print(f"The word is \033[0;36m{chosen_word}\033[0m")
            print("\033[0;32mYou win.\033[0m")

        
        print("\033[0;36m"+hangman_art.stages[lives])
        print(border)
    else:
        print("\033[0;31mERROR!\033[0m Please enter only one letter!")
        print(border)