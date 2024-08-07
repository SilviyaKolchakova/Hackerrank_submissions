if __name__ == '__main__':
    scores = []
    records = []

    for _ in range(int(input())):

        name = input()
        score = float(input())

        if score not in scores:
            scores.append(score)

        next_record = []
        next_record.append(name)
        next_record.append(score)
        records.append(next_record)

    scores.sort()
    second_low = scores[1]
    target_students = []
    for el in records:
        if el[1] == second_low:
            target_students.append(el[0])

    target_students.sort()

    for name in target_students:
        print(name)