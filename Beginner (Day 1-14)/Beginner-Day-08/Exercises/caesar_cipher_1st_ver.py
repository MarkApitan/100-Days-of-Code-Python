alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
border = ("-"*85)
#Define the encrypt function
def encrypt(text, shift):
    cipher_text = ""
    for letter in text:
        if letter in alphabet:
            position = alphabet.index(letter)
            new_position = position + shift
            new_letter = alphabet[new_position]
            cipher_text += new_letter
        else:
            cipher_text += letter

    print(f"Encoded text: {cipher_text}")
    print(border)

#Define the decrypt function
def decrypt (text, shift):
    plain_text = ""
    for letter in text:
        if letter in alphabet:
            position = alphabet.index(letter)
            new_position = position - shift
            new_letter = alphabet[new_position]
            plain_text += new_letter
        else:
            plain_text += letter
    
    print(f"Decoded text: {plain_text}")
    print(border)

#Define the main part of the code
def main ():
    print(border)
    text = input("Type your message: ").lower()
    shift = int(input("Type the shift number: "))
    print (border)
    print ("Type a number from 1 to 2 to choose an operation: \n[1] Encrypt\n[2] Decrypt")
    operator = input("\nEnter the number corresponding to the operation you want to perform: ")
    print(border)
    if operator == '1':
        encrypt(text, shift)
    elif operator == '2':
        decrypt (text, shift)
    else:
        print("Invalid Input!")
        
main()