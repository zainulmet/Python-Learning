def calculate_final_grade(exam_scores, homework_scores):
    exam_weight = 0.7
    homework_weight = 0.3
    
    final_grades = []
    
    for exams, homework in zip(exam_scores, homework_scores):
        total_score = (sum(exams) / len(exams)) * exam_weight + (sum(homework) / len(homework)) * homework_weight
        
        if total_score >= 90:
            grade = "A"
        elif total_score >= 80:
            grade = "B"
        elif total_score >= 70:
            grade = "C"
        elif total_score >= 60:
            grade = "D"
        else:
            grade = "F"
        
        final_grades.append((total_score, grade))
    
    return final_grades

# Get user input for exam scores
num_students = int(input("Enter the number of students: "))
exam_scores = []
for i in range(num_students):
    exams = [float(score) for score in input(f"Enter exam scores for student {i + 1} (comma-separated): ").split(",")]
    exam_scores.append(exams)

# Get user input for homework scores
homework_scores = []
for i in range(num_students):
    homework = [float(score) for score in input(f"Enter homework scores for student {i + 1} (comma-separated): ").split(",")]
    homework_scores.append(homework)

final_grades = calculate_final_grade(exam_scores, homework_scores)

for i, (score, grade) in enumerate(final_grades, start=1):
    print(f"Student {i}: Total Score = {score:.2f}, Grade = {grade}")
