# Complete the function to return the amount of days it will take to cover a route
import math as mt
def car_route(n,m):
  num_days = mt.ceil(m/n)
  return num_days


# Invoke the function with two integers
print(car_route(3,100))
