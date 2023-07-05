from word_lists import north_america_words, international_words
import string

word_list = 'north_america'
# word_list = 'international'
assert word_list in ['north_america', 'international']

if word_list == 'north_america':
    print('Using North American word list.\n')
    words = north_america_words
else:
    print('Using international word list.\n')
    words = international_words

vowels = 'AEIOU'

def is_vowel(letter):
    assert len(letter) == 1
    return letter in vowels
def is_consonant(letter):
    assert len(letter) == 1
    return letter not in vowels

print('All two-letter words grouped by first letter:')
for first in string.ascii_uppercase:
    group = []
    for word in words:
        if word[0] == first:
            group.append(word)
    print(f'- {first}:  {" ".join(group) or "-"}')

print()
print('All two-letter words grouped by last letter:')
for last in string.ascii_uppercase:
    group = []
    for word in words:
        if word[1] == last:
            group.append(word)
    print(f'- {last}:  {" ".join(group) or "-"}')

print()
vowels_only = [word for word in words if is_vowel(word[0]) and is_vowel(word[1])]
consonants_only = [word for word in words if is_consonant(word[0]) and is_consonant(word[1])]
print(f'Vowels (AEIOU) only:  {" ".join(vowels_only)}')
print(f'Consonants only:      {" ".join(consonants_only)}')
