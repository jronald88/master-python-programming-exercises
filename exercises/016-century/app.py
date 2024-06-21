# Complete the function to return the respective number of the century
import math as mt
def century(year):
  century_int = mt.ceil(year/100)
  return century_int


# Invoke the function with any given year
print(century(205))
