#'abbxxxxzzy'

groups = {}
string = input()
for el in string:
    if el not in groups:
        groups[el] = [el]
    else:
        groups[el].append(el)
start_index = 0
target_groups = []
for v in groups.values():
    end_index = (start_index+len(v))-1
    if len(v) >= 3:
        target_groups.append([start_index, end_index])
    start_index = end_index + 1

print(target_groups)
