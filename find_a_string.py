string = 'ABCDCDC'
sub_string = 'CDC'
sub_s_found = []
index = len(sub_string)

for i in range(len(string)):

    next_sub_s = string[i:index]
    if next_sub_s == sub_string:
        sub_s_found.append(next_sub_s)
    index += 1

print(sub_s_found)