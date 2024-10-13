#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

with open('Input/Names/invited_names.txt', 'r') as names:
    names_list = names.readlines()
with open("Input/Letters/starting_letter.txt", 'r') as e:
    contents = e.read()
    for name in names_list:
        name = name.strip("\n")
        new_letter = contents.replace('[name]', f'{name}')
        with open(f'Output/ReadyToSend/{name}.txt', 'w') as output:
            output.write(new_letter)