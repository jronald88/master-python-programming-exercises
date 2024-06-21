# Complete the function to return the tens digit and the units digit of any integer
def two_digits(number):
  tens = number//10
  units = number%10
  return tens, units
   

# Invoke the function with any two digit integer as its argument
print(two_digits(79))
