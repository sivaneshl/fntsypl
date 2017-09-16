# list comprehension

# list of even numbers
even_numbers = [i for i in range(100) if (i % 2 == 0)]
print(even_numbers)

# list of squares
squares = [i*i for i in range(10)]
print(squares)

# extract first letter of each word in a sentence
sentence = "this is a new sentence"
first_letter_of_each_word = [word[0] for word in sentence.split()]
print(first_letter_of_each_word)

# print first letter of each word in upper case from a sentence
sentence = "this is a new sentence"
first_letter_of_each_word = [word[0].upper() for word in sentence.split()]
print(first_letter_of_each_word)

# extarct numbes from a sentence
sentence = "I will be 30 years old by the 15th of this month"
numbers_from_sentence = [i for i in sentence if i.isdigit()]
print(numbers_from_sentence)

# read a file and extract all numbers
fh = open("regex_sum_42.txt").read()
get_numbers_from_file = [i for i in fh if i.isdigit()]
tot = 0
print(get_numbers_from_file)
for i in get_numbers_from_file:
    tot = tot + int(i)
print(tot)

# using functions
def double(x):
    return x*x
print([double(i) for i in range(10)])


print([x*y for x in [2,4,6] for y in [1,3,5]])
