# Write your code below this line 👇
def prime_checker(number):
    divisible = 0
    for x in range(1, 100+1):
        for n in range (100, 1,-1):
            if x * n == number:
                divisible += 1
    if divisible == 1:
      print("It's a prime number.")
    else:
      print("It's not a prime number.")

# Write your code above this line 👆
    
#Do NOT change any of the code below👇
n = int(input("Enter a number: ")) # Check this number
prime_checker(number=n)