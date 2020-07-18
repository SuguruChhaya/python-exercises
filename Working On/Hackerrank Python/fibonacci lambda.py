def cube(x): return x**3  # complete the lambda function


def fibonacci(n):
    # return a list of fibonacci numbers
    a = 0
    b = 1
    final = []
    
    final.append(a)
    final.append(b)
    for i in range(n - 2):
        final.append(a+b)
        temp_a = a
        temp_b = b
        a = temp_b
        b = temp_a + temp_b
    #!I sliced it so the list wouldn't be messed up when the input was 0 or 1
    return final[:n]


if __name__ == '__main__':
    n = int(input())
    fibonacci(n)
    print(list(map(cube, fibonacci(n))))
