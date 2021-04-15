firstNumber = int(input("Enter a number"))
secondNumber = int(input("Enter a number"))
thirdNumber = int(input("Enter the third number"))
numsum = firstNumber + secondNumber + thirdNumber
product = firstNumber * secondNumber * thirdNumber
average = product//3.0
smallest = firstNumber
if secondNumber < firstNumber:
    smallest = secondNumber
elif thirdNumber < secondNumber:
    smallest = thirdNumber

largest = firstNumber
if secondNumber < firstNumber:
    largest = secondNumber
elif thirdNumber < secondNumber:
    largest = thirdNumber

print(smallest)
print(largest)
print(numsum)
print(product)