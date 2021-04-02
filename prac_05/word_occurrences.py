"""
Lee Crawford
CP1404/CP5632 Practical
word_occurrences
"""

word_occurrences = {}

words = []
occurrences = []
sentence = "this is a collection of words of nice words this is a fun thing it is".split(" ")
for index, word in enumerate(sentence):
    if word not in word_occurrences.keys():
        word_occurrences[word] = 0
    if word == sentence[index]:
        word_occurrences[word] += 1
print(word_occurrences)
for word, occurrence in word_occurrences.items():
    words.append(word)
words.sort()
longest_string = (max(words, key=len))
for word in words:
    print("{:{}}{}".format(word + " :", len(longest_string) + 3, word_occurrences[word]))
