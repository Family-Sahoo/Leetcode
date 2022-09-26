input_string = "It is a kill ath filellaa111122 counterattacks@!@!vcshdc"

big_word = ''
word = []

for char in input_string:
    if char.isalnum():
        word.append(char)
    else:
        if len(big_word) < len(''.join(word)):
            big_word = ''.join(word)
            word = []
        else:
            word = []    

if len(big_word) < len(''.join(word)):
        big_word = ''.join(word)


print("Big word: ", big_word)

## 2

import re

regex_strings = re.findall('\w+', input_string)

maximum_len = max(len(item) for item in regex_strings)
for item in regex_strings:
    if len(item) == maximum_len:
        print("Longest word: ", item)
