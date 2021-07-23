def cube_list(number):
    for i in range(len(number)):
        number[i] **= 3
    return number


number = [1, 3, 5, 7, 8, 2]
result = cube_list(number)
print(result)
