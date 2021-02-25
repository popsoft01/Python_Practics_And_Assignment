numbers = [2, 2, 4, 6, 7, 1, 4, 5, 4, 9, 0, 2]
uniques = []
for number in numbers:
    if number not in uniques:
        uniques.append(number)
print(uniques)