# write code that ask us from input
# to say yes/no for each student if they are present or not
# then gather all infos and tell me that present student are in which grade

# This is a sample of output
# ---------------------------------------------------------------
# Is Alice present? (yes/no): yes
# Is Bob present? (yes/no): yes
# Is Charl present? (yes/no): f
# Is Sara present? (yes/no): f
# Is Nik present? (yes/no): d

# Present students: {'Alice', 'Bob'}
# Absent students: {'Charl', 'Sara', 'Nik'}

# Grades of present students:
# Alice (Grade: A, Score 8)
# Bob (Grade: B, Score 9)
# -----------------------------------------------------------------


# List of students with details
students = [
    {'name': 'Alice', 'id': 101, 'grade': 'A', "score": 8},
    {'name': 'Bob', 'id': 102, 'grade': 'B', "score": 9},
    {'name': 'Charl', 'id': 103, 'grade': 'A', "score": 10},
    {'name': 'Sara', 'id': 104, 'grade': 'C', "score": 7},
    {'name': 'Nik', 'id': 105, 'grade': 'C', "score": 6}
]

# List to track attendance
attendance = []

# Marking attendance
for student in students:
    answer = input(f"Is {student['name']} present? (yes/no): ")
    record = {
        'name': student['name'],
        'id': student['id'],
        'grade': student['grade'],
        'score': student['score'],
    }

    #inside the above recorde variable ---> 'present': 1 if answer.lower() == 'yes' else 0
    if answer.lower() == 'yes':
        record["present"] = True
    else:
        record["present"] = False

    attendance.append(record)

# Summary of attendance
present_students = {record['name'] for record in attendance if record['present'] == 1}
absent_students = {record['name'] for record in attendance if record['present'] == 0}

# Display results
print(f"\nPresent students: {present_students}")
print(f"Absent students: {absent_students}")

# Display grades of present students
print("\nGrades of present students:")
for record in attendance:
    if record['present'] == 1:
        print(f"{record['name']} (Grade: {record['grade']}, Score {record['score']})")
