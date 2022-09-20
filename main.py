import reversewords

str1 = "this is a test text, i want to convert even digit words."
str2 = str1.replace(", ", ' ') # replace ', ' with ' '
str2_1 = str2.replace(".", ' ') #replace '.' with ' '
splitted_string = str2_1.split()
for words in splitted_string:
    if len(words) % 2 == 0:
        rev_word = reversewords.reverse_words(words)
        str1 = str1.replace(words, rev_word)
print(str1)

