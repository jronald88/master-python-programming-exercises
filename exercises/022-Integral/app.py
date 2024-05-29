# Your code here
def squares_dictionary(n):
    square_dict = dict()
    for i in range (1, n+1):
        square_dict[i] = i*i
    return square_dict
    
print(squares_dictionary(4))
