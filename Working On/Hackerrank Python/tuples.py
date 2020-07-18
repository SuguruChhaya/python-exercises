'''
def mutate_string(string, position, character):
    #!This separates the characters in the list and turns them into a list
    l = list(string)
    l[position] = character
    string = "".join(l)
    
    return string

if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)
'''

'''
def count_substring(string, sub_string):
    count = 0
    for i in range(len(string)):
        if string[i] == sub_string[0]:
            if string[i:i + len(sub_string)] == sub_string:
                count += 1
    return count


if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()

    count = count_substring(string, sub_string)
    print(count)
'''
