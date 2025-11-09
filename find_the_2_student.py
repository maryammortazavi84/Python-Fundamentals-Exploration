user1 = 0
grade1 = 0
user2 = 0
grade2 = 0
number = int(input("enter the number of students: "))
if number<2:
    print("enter a number higher than 2")
else:
    for students in range(number):
        user = int(input("user: "))
        grade = int(input("grade: "))
        if grade > grade1:
            user2= user1
            grade2 = grade1
            user1 = user
            grade1 = grade
        else:
            if grade> grade2:
                user2 = user
                grade2 = grade
    print(f' the second student is student{user2} with the score {grade2}')