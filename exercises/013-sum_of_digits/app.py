# Complete the function "digits_sum" so that it prints the sum of a three-digit number
def digits_sum(num):
  hun = (num % 1000)//100
  ten = (num % 100)//10
  unit = num % 10
  return hun + ten + unit
  
print(digits_sum(123))
