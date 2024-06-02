from clear import Clear
from art import logo

print ("Welcome to Secret Auction Program!")
# Create an empty dictionary to store the bids
bids = {}  

end_of_program = False  

while not end_of_program:  
    print(logo)  # Print the program logo

    # Prompt the user to enter their name and bid price
    name = input("What is your name? ")  
    bid_price = int(input("What is your bid? ₱"))  

    # Add the name and bid price to the bids dictionary
    bids[f"{name}"] = bid_price  

     # Prompt the user to indicate if there are other bidders
    are_there_other_bidders = input("Are there any other bidders? (y/n): ")  # Prompt the user to indicate if there are other bidders

    if are_there_other_bidders == "y":  
        Clear()  
    else:  
        Clear() 
        #Fine the highest bidder, display the result, and end the program
        highest_bidder = max(bids) 
        print(f"The winner is {highest_bidder} with a bid of ₱{bids[highest_bidder]}")
        end_of_program = True  