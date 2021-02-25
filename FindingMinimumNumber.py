firstNumber = int(input("Enter the First number : \n"))
secondNumber = int(input("Enter the second number  \n"))
thirdNumber = int(input("Enter the third number: \n"))

minimum = firstNumber

if secondNumber < minimum:
    minimum = secondNumber

if thirdNumber < minimum:
    minimum = thirdNumber
    
print("Minimum number is ", minimum)