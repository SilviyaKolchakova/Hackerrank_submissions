# input = abracadabra

s = 'abracadabra'
position = 5
char = 'k'

new_s = s[:position] + char + s[position+1:]
print(new_s)