from django.db import models


class Person():
    SHIRT_SIZES = (
        ('S', 'Small'),
        ('M', 'Medium'),
        ('L', 'Large'),
    )
    name = models.CharField(max_length=60)
    shirt_size = models.CharField(max_length=1, choices=SHIRT_SIZES)

    class Meta:
        abstract = True


class Student(Person):
    hostel_name = models.CharField(max_length=67)

    def __str__(self):
        return self.name + " " + self.shirt_size + " " + self.hostel_name


p = Student
p.name = "Tunde Ojo"
p.shirt_size = 'A'
hostel_name = "SSSS"

print(str(p.hostel_name))