# Your code here
def list_and_tuple(*n):
    new_list = [str(n) for n in n]
    new_tuple = tuple(new_list)
    return new_list, new_tuple

print(list_and_tuple(1,2,3,4,5,6,7))