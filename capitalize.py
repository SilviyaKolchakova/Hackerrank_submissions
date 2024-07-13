
def solve(s):

    capitalized = []
    result = ''
    for el in s.split(' '):
        capitalized.append(el.capitalize())

    for el in capitalized:
        result += el
        result += ' '

    return result.strip()


if __name__ == '__main__':
    d = input()
    print(solve(d))

