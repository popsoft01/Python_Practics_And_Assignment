def string_check(word):
    l_num = 0
    for letter in range(len(word)):
        find_letter = ""
        for j in range(letter, len(word)):
            if word[j] not in find_letter:
                find_letter += word[j]
                l_num = max(l_num, len(find_letter))
            else:
                break
    return l_num


sprint = string_check("bessyjanekingsley")
print(sprint)
