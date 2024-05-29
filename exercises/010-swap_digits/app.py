# Complete the function to return the swapped digits of a given two-digit integer
def swap_digits(num):
  num1 = num//10
  num2 = num % 10
  return int(str(num2) + str(num1))
   
# Invoke the function with any two-digit integer as its argument
print(swap_digits(30))
