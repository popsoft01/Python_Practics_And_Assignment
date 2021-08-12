def string_check(word):
    l_num =0
    for letter in range(len(word)):
        find_letter = " "
        for j in range(letter, len(word)):
            if word[letter] not in find_letter:
                find_letter = word[j]
