def most_occuring_first_letter(passage: str):
    '''
    Returns the letter which occurs most frequently
    as the first letter of any word.(case insensitive)

    Args:
        passage (str): A multi-line string representing the passage.

    Returns:
        str: The most frequently occurring first letter in lowercase.
    '''
    letter_occurrences = {}
    passage = passage.lower()
    list_of_words = passage.split('\n')
    for word in list_of_words:
        if len(word) > 0:
            for a in word.split():
                c = a[0]
                if c in letter_occurrences:
                    letter_occurrences[c] += 1
                else:
                    letter_occurrences[c] = 1
    print(letter_occurrences)
    x=dict(sorted(letter_occurrences.items(), key=lambda item: item[1], reverse=True))
    print(sorted(letter_occurrences.items(), key=lambda item: item[0], reverse=True))
    return list(x.keys())[0]


print(most_occuring_first_letter('''
aaaa bbbb cccc AAAA bbbb
CCCCCC DDDDD CCCCC CdcDC
abab cDcD
'''))
