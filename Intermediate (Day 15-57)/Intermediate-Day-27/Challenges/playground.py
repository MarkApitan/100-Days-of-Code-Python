# Create a function that take an unlimited number of arguments
# Use a loop to sum all the arguments inside the function
def add (*args):
    # return sum(args) (easy way)
    sum = 0
    for arg in args:
        sum += arg
    return sum

print(add(1,2,3,4))