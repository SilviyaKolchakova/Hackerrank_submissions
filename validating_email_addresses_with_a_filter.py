import re

def fun(s):
    # return True if s is a valid email, else return False
    regex = r'[\w-]+@[a-z|A-Z|0-9]+\.[a-z|A-Z]{1,3}'
    if re.fullmatch(regex, s):
        return True
    return False

def filter_mail(emails):
    return list(filter(fun, emails))

if __name__ == '__main__':
    n = int(input())
    emails = []
    for _ in range(n):
        emails.append(input())

filtered_emails = filter_mail(emails)
filtered_emails.sort()
print(filtered_emails)