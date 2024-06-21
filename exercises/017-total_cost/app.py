# Complete the function to return the total cost in dollars and cents of (n) cupcakes
def total_cost(d, c, n):
    cents = d*100 + c
    total = n * cents
    total_dollars = total / 100
    dollars = int(total_dollars)
    new_cents = int((total_dollars-dollars)*100)
    return dollars, new_cents


# Invoke the function with three integers: total_cost(dollars, cents, number_of_cupcakes)
print(total_cost(15,22,4))
