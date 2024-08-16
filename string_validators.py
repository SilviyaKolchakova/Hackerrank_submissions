s = input()
commands_list = []

is_alnum = [True for el in s if el.isalnum()]
commands_list.append(is_alnum)

is_alpha = [True for el in s if el.isalpha()]
commands_list.append(is_alpha)

is_digit = [True for el in s if el.isdigit()]
commands_list.append(is_digit)
is_lower = [True for el in s if el.islower()]
commands_list.append(is_lower)
is_upper = [True for el in s if el.isupper()]
commands_list.append(is_upper)


for el in commands_list:
    if len(el) == 0:
        print(False)
    else:
        print(el[0])





