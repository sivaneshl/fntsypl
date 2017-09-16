# List Comprehension

sentence = "the quick brown fox jumps over the lazy dog"
words = sentence.split()

# newwords = []
# for word in words:
#     if word != 'the':
#         newwords.append(word)
# print(newwords)

# Comprehension notation
newwords = [(word) for word in words if word != 'the']
print(newwords)
