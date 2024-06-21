# Your code here
def remove_duplicate_words(words):
    split_list = words.split(' ')
    split_list = set(split_list)
    return sorted(split_list)

print(remove_duplicate_words("hi and how are you and I am here and etc and poop"))