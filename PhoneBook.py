def phone_book():
    phoneBook = {}
    for i in range(2):
        name = input("Enter ur name: \n")
        phone = input("Enter your phone number: \n")
        age = int(input("enter yu age"))
        phoneBook.update({
            name: [phone, age]
        })
    return phoneBook


phoneBook = phone_book()
print(phoneBook)

