# Your code here
def two_dimensional_list(x,y):
    new_list = []
    for i in range(x):
        row = []
        for j in range(y):
            row.append(i*j)
        new_list.append(row)
    return new_list

print(two_dimensional_list(3,4))