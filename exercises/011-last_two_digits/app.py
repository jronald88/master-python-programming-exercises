# Complete the function to print the last two digits of an integer greater than 9
def last_two_digits(num):
    if num > 9:
        result = num%100
    else:
        print("invalid number")
    return result

# Invoke the function with any integer greater than 9
print(last_two_digits(321))
