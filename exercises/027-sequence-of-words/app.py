# Your code here
def sequence_of_words(phrase):
    sorted_phrase = sorted(phrase.split(','))
    sorted_phrase = ','.join(sorted_phrase) #rejoin as string with comma separators
    return sorted_phrase

print(sequence_of_words("how, now, brown, cow"))