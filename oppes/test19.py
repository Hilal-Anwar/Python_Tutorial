def get_freq(filename):
    """
    Extract frequency information from the file

    Argument:
        filename: string, path to file
    Return:
        result: dictionary; keys are strings, values are integers
    """
    words = {}
    file = open(filename, 'r')
    print(file.readlines())
    for a in file:
        a=a.replace('\n','')
        if a in words:
            words[a] += 1
        else:
            words[a] = 1
    return words

print(get_freq(' words.txt'))
print(get_freq(' words.txt'))
