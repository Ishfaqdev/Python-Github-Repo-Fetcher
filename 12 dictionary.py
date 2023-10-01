# students = {
#     "Ishfaq": "Dargai",
#     "Ahmad": "Mardan",
#     "Khan": "Dir",
#     "Ali": "Swat",
# }

# for student in students:
#     # print(student)
#     print(student, students[student], sep=", ")

students = [
    {"name": "Ishfaq", "City": "Dargai", "Job": "Developer"},
    {"name": "Ahmad", "City": "Mardar", "Job": "Teacher"},
    {"name": "Khan", "City": "Dir", "Job": "Computer Operator"},
    {"name": "Ali", "City": "Swat", "Job": "Software Developer"},
]

for student in students:
    print(student["name"], student["City"], student["Job"], sep=", ")
