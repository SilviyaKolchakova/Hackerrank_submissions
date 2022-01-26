n = int(input())
arr = list(map(int, input().split()))[:n]
max_score = max(arr)

max_score_removed = [num for num in arr if num < max_score]


print(max(max_score_removed))
