list_len = int(input())
my_list = [int(x) for x in input().split()]
sum = 0
used_nums = {}
num_elements = int(input())
for i in range(num_elements):
    next_size, next_num = input().split()
    if int(next_size) in my_list:
        if next_size not in used_nums:
            used_nums[next_size] = []
        if next_num not in used_nums[next_size]:
            used_nums[next_size].append(next_num)
            sum += int(next_num)


print(sum)
