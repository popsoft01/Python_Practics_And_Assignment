score = int(input("Enter student score : \n"))

if score >= 90:
    print("Congratulation your score is", score, " and your grade is A")
elif score >= 80:
    print("Congratulation your score is", score, " and your grade is B")

elif score >= 70:
    print("Congratulation your score is", score, " and your grade is C")

elif score >= 60:
    print("Congratulation your score is", score, " and your grade is D")

elif score >= 50:
    print("Congratulation your score is", score, " and your grade is E")

else:
    score < 50
    print("Sorry your score is : ", score, "you need to retake the course")