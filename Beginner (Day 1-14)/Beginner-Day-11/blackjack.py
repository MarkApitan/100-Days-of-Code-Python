import random
from clear import Clear
from art import logo

def deal_card(): 
    cards = [11,2,3,4,5,6,7,8,9,10,10,10,10]
    card = random.choice(cards)
    return card
    
def calculate_score(list_of_cards):
    if list_of_cards == [11,10] or list_of_cards == [10,11]:
        return 0
    if 11 in list_of_cards and sum(list_of_cards) > 21:
        list_of_cards.remove(11)
        list_of_cards.append(1)
    return sum(list_of_cards)

def play_blackjack():
    
    end_of_game = False
    user_cards =[]
    dealer_cards = []

    print(logo)

    for i in range (2):
        user_cards.append(deal_card())
        dealer_cards.append(deal_card())
    
    while not end_of_game:
        user_score = calculate_score(user_cards)
        dealer_score = calculate_score(dealer_cards)
        print(f"Your cards: {user_cards}, current score: {user_score}")
        print(f"Computer's first card: {dealer_cards[0]}")

        if user_score == 0 or dealer_score == 0 or user_score > 21:
            end_of_game = True
        else:

            if input('Do you want to get another card? (y/n): ').lower() == 'y':
                user_cards.append(deal_card())
            else:
                end_of_game = True
    while dealer_score != 0 and dealer_score < 17:
        dealer_cards.append(deal_card())
        dealer_score = calculate_score(dealer_cards)
    
    print(f"Your final hand: {user_cards}, final score: {user_score}")
    print(f"Computer's final hand: {dealer_cards}, final score: {dealer_score}")
    print(compare(user_score, dealer_score))
        
def compare (user_score, dealer_score):
    if user_score == dealer_score:
        return "\033[0;33mIt's a Draw!\033[0m"
    elif dealer_score == 0:
        return "\033[0;31mDealer has Blackjack. Dealer Wins!\033[0m"
    elif user_score == 0:
        return '\033[0;32mYou win with a Blackjack!\033[0m'
    elif user_score > 21:
        return "\033[0;31mYour score went above 21. Dealer Wins!\033[0m"
    elif dealer_score > 21:
        return "\033[0;32mDealer score went above 21. User Wins!\033[0m"
    elif user_score > dealer_score:
        return "\033[0;32mYou win!\033[0m"
    else:
        return "\033[0;31mYou lose!\033[0m"

while input("Do you want to play a game of Blackjack? (y/n): ").lower() == 'y':
    Clear()
    play_blackjack()