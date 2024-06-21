# Complete the function to return the first digit to the right of the decimal point
def first_digit(num):
  truncated_num = int(num)
  decimal_part = num - truncated_num
  first_digit_int = int(decimal_part*10)
  return first_digit_int


# Invoke the function with a positive real number. ex. 34.33
print(first_digit(6.25))
