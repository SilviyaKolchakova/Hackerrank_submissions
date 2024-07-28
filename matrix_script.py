import re

first_multiple_input = input().rstrip().split()

n = int(first_multiple_input[0])

m = int(first_multiple_input[1])

matrix = []

for _ in range(n):
    matrix_item = input()
    matrix.append(matrix_item)

decoded_script = ""

for row in range(m):
    for col in range(n):
        decoded_script += matrix[col][row]

pattern = r"(?<=\w)([!@#$%&]+)(?=\w)|(?<=\W)([!@#$%&]+)(?=\w)"
decoded_script = re.sub(pattern, " ", decoded_script)
print(decoded_script)
