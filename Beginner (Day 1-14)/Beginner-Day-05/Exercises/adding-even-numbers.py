target = input("Enter a number between 0 and 1000: ")# Enter a number between 0 and 1000
target = int(target)
# 🚨 Do not change the code above ☝️

# Write your code here 👇
sum=0
for even in range (2, target+1, 2):
  sum+=even
  
print(f"The sum of all even numbers between 0 to {target} is {sum}")