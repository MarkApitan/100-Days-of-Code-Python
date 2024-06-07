import random

cards = [11,2,3,4,5,6,7,8,9,10,10,10,10]
user_cards =[]
dealer_cards = []
def deal_card():
    
    for i in range (2):
        user_card = random.choice(cards)
        user_cards.append(user_card)
    for i in range (2):
        dealer_card = random.choice(cards)
        dealer_cards.append(dealer_card)

def calculate_score():
    user_total = sum(user_cards)
    dealer_cards_total = sum(dealer_cards)
    return user_total, dealer_cards_total


deal_card()
user_total, dealer_total = calculate_score()

print (user_cards)
print (dealer_cards)
print (user_total)
print (dealer_total)