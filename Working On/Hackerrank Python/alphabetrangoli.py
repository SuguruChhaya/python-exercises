
# *This was a pretty interesting challenge
#!It became much easier when I stored what was printed so I can reuse them again.
def print_rangoli(size):
    # your code goes here
    # *Probably have to use chr and ord
    row_alpha = chr(96 + size)
    current_ord = 96 + size
    width = 4 * size - 3
    print((row_alpha).center(width, "-"))
    version_list = [(row_alpha).center(width, "-")]
    for i in range(1, size):
        row_alpha += "-" + chr(current_ord - i)
        reversed_row_alpha = row_alpha[::-1][1:]
        print((row_alpha + reversed_row_alpha).center(width, "-"))
        version_list += [(row_alpha + reversed_row_alpha).center(width, "-")]

    for h in range(size-2, -1, -1):
        print(version_list[h])


if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)
