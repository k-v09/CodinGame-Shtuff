from collections import Counter

LETTER_SCORES = {
    'e': 1, 'a': 1, 'i': 1, 'o': 1, 'n': 1, 'r': 1, 't': 1, 'l': 1, 's': 1, 'u': 1,
    'd': 2, 'g': 2,
    'b': 3, 'c': 3, 'm': 3, 'p': 3,
    'f': 4, 'h': 4, 'v': 4, 'w': 4, 'y': 4,
    'k': 5,
    'j': 8, 'x': 8,
    'q': 10, 'z': 10
}

def word_score(word):
    return sum(LETTER_SCORES[letter] for letter in word)

def can_form_word(word, available_letters):
    word_counter = Counter(word)
    available_counter = Counter(available_letters)
    return all(word_counter[letter] <= available_counter[letter] for letter in word_counter)

def find_best_word(dictionary, available_letters):
    best_word = ""
    best_score = 0

    for word in dictionary:
        if can_form_word(word, available_letters):
            score = word_score(word)
            if score > best_score:
                best_score = score
                best_word = word

    return best_word

N = int(input())
dictionary = [input().strip() for _ in range(N)]
available_letters = input().strip()

print(find_best_word(dictionary, available_letters))