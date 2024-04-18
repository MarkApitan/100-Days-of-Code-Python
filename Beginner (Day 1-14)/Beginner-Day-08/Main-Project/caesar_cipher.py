#Defining Variables
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
border = ("-"*85)

#Define caesar
def caesar (text, shift, operator):
    final_text = ""
    if operator == '2':
        shift *= -1
    for letter in text:
        if letter in alphabet:
            position = alphabet.index(letter)
            new_position = position + shift
            new_letter = alphabet[new_position]
            final_text += new_letter
        else:
            final_text += letter

    if operator == '2':
        print(f"{border}\nDecoded text: {final_text}")
    else:
        
        print(f"{border}\nEncoded text: {final_text}")

#Define the main part of the code
def main ():
    end_of_program = False
    while end_of_program == False:
        print(f"{border}\n\t\t\t\tWelcome to Caesar Cipher!\n{border}")
        print("Enter your message and shift number")
        text = input("\nType your message: ").lower()
        shift = int(input("Type the shift number: "))
        shift = shift%26

        print (border)
        print ("Type a number from 1 to 2 to choose an operation: \n[1] Encrypt\n[2] Decrypt")
        operator = input("\nEnter the number corresponding to the operation you want to perform: ")
        if operator == '1' or operator == '2':
            caesar(text, shift, operator)
        else:
            print(f"{border}\nInvalid Input!")

        print(border)
        use_again = input("Do you want to use the program again? (y/n): ")
        if use_again == 'n':
            print(border)
            print("Thank you!")
            end_of_program = True
        
main()