# student_grades contains scores (out of 100) for 5 assignments
student_grades = {
    'Andrew': [56, 79, 90, 22, 50],
    'Colin': [88, 62, 68, 75, 78],
    'Alan': [95, 88, 92, 85, 85],
    'Mary': [76, 88, 85, 82, 90],
    'Tricia': [99, 92, 95, 89, 99]
}

highest_total_points = {}
scores = []



for student, grades in student_grades.items(): 
    highest_total_points[student] = sum(grades)

top_student = max(highest_total_points) 
percentage = int(highest_total_points[top_student]) / int(len(student_grades[top_student]))
    
print('The top student is:', top_student, 
        'with a percentage of', percentage)

for grades in student_grades.values():
    scores.append(sum(grades))
    print(scores)
   
    
print(scores)
average_score = int(sum(scores)) / len(scores)
print(average_score) 