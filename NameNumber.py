phoneBook = {}
for i in range(2):
    name = input("Enter ur name: \n")
    phone = input("Enter your phone number: \n")
    age = int(input("eter yu age"))
    phoneBook.update({
        name: [phone, age]
    })
print(phoneBook)
