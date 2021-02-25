try:
    age = int(input('age: '))
    income = 20000
    risk = income/age
    print(age)
except ZeroDivisionError:
    print('age cannot be zero')
except valueError:
    print('Invalid value')