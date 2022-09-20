def reverse_words(str1):
    str_empty = ""
    for i in range(len(str1)-1, -1, -1):
        str_empty += str1[i]
    return str_empty
