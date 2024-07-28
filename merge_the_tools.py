def merge_the_tools(string, k):
    string_list = [x for x in string]
    sep_string = []

    while string_list:
        next_el = string_list.pop(k)
        sep_string.append(next_el)
        if len(sep_string) < k:
            break


    print(sep_string)
string, k = input(), int(input())
merge_the_tools(string, k)
