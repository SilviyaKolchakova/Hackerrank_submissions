num = int(input())
new_list = []


def insert(lst, idx, obj):
    lst.insert(idx, obj)
    return lst


def sort(lst, *args, **kwargs):
    return lst.sort()


def remove(lst, idx):
    lst.remove(idx)
    return lst


def append(lst, el):
    lst.append(el)
    return lst


def pop(lst):
    return lst.pop()


def reverse(lst):
    lst.reverse()
    return lst


commands = {
    'insert': insert,
    'sort': sort,
    'print': print,
    'remove': remove,
    'append': append,
    'reverse': reverse,
}

for el in range(num):
    next_line = input().split()

    if len(next_line) == 1:
        command = next_line[0]

        if command == 'pop':
            new_list.pop()
            continue
        next_command = commands[command]
        next_command(new_list)
    elif len(next_line) == 2:
        command, idx1 = next_line[0], int(next_line[1])
        next_command = commands[command]
        next_command(new_list, int(idx1))
    elif len(next_line) == 3:
        command, idx1, idx2 = next_line[0], int(next_line[1]), int(next_line[2])
        next_command = commands[command]
        next_command(new_list, int(idx1), int(idx2))








