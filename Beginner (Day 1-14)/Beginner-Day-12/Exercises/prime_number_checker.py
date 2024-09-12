num = 1
def is_prime(num):
    counter = 0
    if num <= 1:
        return False
    else:
        for i in range (2, num):
            if num % i == 0:
                counter += 1
        if counter > 0:
            return False
        else:
            return True

print (is_prime(num))