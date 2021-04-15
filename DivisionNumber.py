numbers = range(1700, 3000)
for number in numbers:
    if number % 5 == 0 or number % 7 == 0:
        print(number, end=" ")
