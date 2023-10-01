# try:
#     score = int(input("Score : "))
#     if 0 <= score <= 100:
#         if score >= 90 :
#             print("Grade : A1")
#         elif score >= 80 :
#             print("Grade : A")
#         elif score >= 70 :
#             print("Grade : B")
#         elif score >= 60 :
#             print("Grade : C")
#         elif score >= 50 :
#             print("Grade : D")
#         elif score >= 40 :
#             print("Grade : E")
#         else:
#             print("FAIL")

#     else:
#         raise ValueError("Score must be between 0 and 100")
# except ValueError:
#     print("Invalid input. Please enter a valid numeric score between 0 and 100.")


# Calculate Grade using Function

def calculate_grade(score):
    try:
        score = int(score)
        if 0 <= score <= 100:
            if score >= 90:
                return "A1"
            elif score >= 80:
                return "A"
            elif score >= 70:
                return "B"
            elif score >= 60:
                return "C"
            elif score >= 50:
                return "D"
            elif score >= 40:
                return "E"
            else:
                return "FAIL"
        else:
            raise ValueError("Score must be between 0 and 100")
    except ValueError:
        print("Invalid input. Please enter a valid numeric score between 0 and 100.")


while True:
    score = input("Enter the student's score: ")
    grade = calculate_grade(score)
    if grade == "Invalid input. Please enter a valid numeric score between 0 and 100.":
        print(grade)

    else:
        print(grade)
        break
