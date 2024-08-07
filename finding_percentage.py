n = int(input())

student_marks = {}
for _ in range(n):
    name, *line = input().split()
    scores = list(map(float, line))
    student_marks[name] = scores

query_name = input()
student_scores = student_marks[query_name]

average_score = sum(student_scores)/len(student_scores)

print(f'{average_score:.2f}')
