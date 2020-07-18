def fun(s):
    # return True if s is a valid email, else return False
    checker = True
    at_index = 0
    dot_index = 0
    for i in range(len(s)):
        if s[i] == "@":
            at_index = i
        elif s[i] == ".":
            dot_index = i

    if len(s[:at_index]) <= 0 or len(s[at_index: dot_index]) <= 0:
        checker = False

    for a in range(at_index):
        if not (s[a].isalpha() or s[a].isdigit() or s[a] == "_" or s[a] == "-"):
            checker = False
            break

    for b in range(at_index + 1, dot_index):

        if not (s[b].isalpha() or s[b].isdigit()):
            checker = False
            break

    if len(s) - dot_index > 4 or len(s) - dot_index < 0:
        checker = False
    return checker


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
