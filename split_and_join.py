string = 'this is a string'
new_string = ''

for element in string:
    if element == ' ':
        next_el = '-'
        new_string += next_el
        continue
    new_string += element

print(new_string)