"""
Lee Crawford
CP1404/CP5632 Practical
word_occurrences
"""

WORD_OCCURRENCES = {}


def main():
    """Analise user generated sentence and count each occurrence of each separate word"""
    words = []
    sentence = input("Text: ").split(" ")
    returns_word_count(sentence)
    print(WORD_OCCURRENCES)
    extract_keys_into_sorted_list(words)
    longest_string = (max(words, key=len))
    for word in words:
        print("{:{}}{}".format(word + " :", len(longest_string) + 3, WORD_OCCURRENCES[word]))


def extract_keys_into_sorted_list(words):
    """Sort list of keys"""
    for word, occurrence in WORD_OCCURRENCES.items():
        words.append(word)
    words.sort()


def returns_word_count(sentence):
    """Count each occurrence of word and add to dictionary then reset for next word"""
    for index, word in enumerate(sentence):
        if word not in WORD_OCCURRENCES.keys():
            WORD_OCCURRENCES[word] = 0
        if word == sentence[index]:
            WORD_OCCURRENCES[word] += 1


main()
