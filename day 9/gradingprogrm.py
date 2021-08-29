student_scores = {
  "Harry": 81,
  "Ron": 78,
  "Hermione": 99, 
  "Draco": 74,
  "Neville": 62,
}
def grading(marks):
    if marks>90 and marks<=100:
        return "Outstanding"
    elif marks>80 and marks<=90:
        return "Exceeds Expectations"
    elif marks>70 and marks<=80:
        return "Acceptable"
    elif marks<=70:
        return "Fail"
    

student_grades={}

for key in student_scores:
    mark=student_scores[key]
    grade=grading(mark) 
    student_grades[key]=grade

print(student_grades)