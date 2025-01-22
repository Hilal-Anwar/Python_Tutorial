# Sample inputs (# note: The values given in the prefix code(grey) will be changed by the autograder according to the testcase while running them.
word1 = "Wingardium" # str
word2 = "Leviyosa" # str
word3 = "Silver" # str
sentence = "Learning python is fun"
n1 = 6 # int
n2 = 4 # int
# <eoi>

output1 = word1+word2 # str: join word1 and word2 with space in between
print(output1)
output2 = word1[:5]+"-"+word2[-4:] # str: join first four letters of word1 and last four letters of word 2 with a hyphen "-" in between
print(output2)
output3 = word3+" "+str(n1) # str: join the word3 and n1 with a space in between
print(output3)
output4 = "-"*50 # str: just the hypen "-" repeated 50 times
print(output4)
output5 = "-"*n2 # str: just the hypen "-" repeated n2 times
print(output5)
output6 = str(n1)*n2 # str: repeat the number n1, n2 times
print(output6)
are_all_words_equal = word1==word2==word3 # bool: True if all three words are equal
print(are_all_words_equal)
is_word1_comes_before_other_two = word1>word2>word3 # bool: True if word1 comes before word2 and word3 assume all words are different
print(is_word1_comes_before_other_two)
has_h = word1.__contains__('h') # bool: True if word1 has the letter h
print(has_h)
ends_with_a = word1.endswith('a') or word1.endswith('A') # bool: True if word1 ends with letter a or A
print(ends_with_a)
has_the_word_python = sentence.__contains__('python') # bool: True if the sentence has the word python
print(has_the_word_python)