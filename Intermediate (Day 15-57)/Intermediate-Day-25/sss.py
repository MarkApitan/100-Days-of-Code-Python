transactions = [
    {'transaction_id': 'T001', 'customer_id': 'C001', 'amount': 150},
    {'transaction_id': 'T002', 'customer_id': 'C002', 'amount': 250},
    {'transaction_id': 'T003', 'customer_id': 'C001', 'amount': 300},
    {'transaction_id': 'T004', 'customer_id': 'C003', 'amount': 100}
]
# Using list comprehension
def get_transaction_id (transactions):
     # using list comprehansion, get the transaction of customers that are greater than or equal to 200
     data = [transaction["transaction_id"] for transaction in transactions if transaction["amount"] >= 200]
     # return the data
     return data 
print (get_transaction_id (transactions))
# data = []
# [expression, for loop, conditional statement]
# for transaction in transactions:
#      if transaction["amount"] > 200:
#         data.append(transaction["transaction_id"])

# print(data)