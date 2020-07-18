
# *I have to split the string and remove repeating characters.
def merge_the_tools(string, k):
    # your code goes here
    new_list = []
    starter = 0
    for i in range(k, len(string), k):
        new_list.append(string[starter:i])
        starter = i
    new_list.append(string[starter:])
    # print(new_list)

    #!I can probably store all the old ones (which showed up already in a list).
    for item in new_list:
        item_copy = ""
        for char in item:
            if char in item_copy:
                item.replace(char, "")
            else:
                item_copy += char
        print(item_copy)

# *My problem solving approach was correct but I could have used index slicing as well since k is a multiple of the string


def merge_the_tools2(string, k):
    num = int(len(string)/k)
    for index in range(num):
        a = string[index * k: (index+1) * k]
        b = ""
        for char in a:
            if char not in b:
                b += char
        print(b)


if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools2(string, k)
