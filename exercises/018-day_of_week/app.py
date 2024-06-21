# Complete the function to return the number of day of the week for k'th day of year
def day_of_week(k):
  if k + 3 < 8:
    day = k + 3
  else: 
    day = (k + 3)%7

  return day


# Invoke function day_of_week with an integer between 1 and 365
print(day_of_week(321))
