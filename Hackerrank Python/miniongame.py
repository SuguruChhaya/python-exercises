
# *One strategy could be to make a dictionary with all the possible combinations with the # of times they appear.
#!Some issue with the number counts.
# ?I should be able to iterate using a for loop, don't know why it gives me the wrong answer.
#!Somehow the dictionary method doesn't work
'''
def minion_game(string):
    # your code goes here
    stuart_score = 0
    kevin_score = 0
    my_dict = {}
    for i in range(len(string)):
        for h in range(i+ 1, len(string) + 1):
            if string[i:h] == "":
                pass
            elif string[i:h] in my_dict:
                my_dict[string[i:h]] += 1
            else:
                my_dict[string[i:h]] = 1

    for key, values in my_dict.items():
        if key[0] in "AEIOU":
            kevin_score += values
        else:
            stuart_score += values
    if kevin_score > stuart_score:
        print(f"Kevin {kevin_score}")
    elif kevin_score < stuart_score:
        print(f"Stuart {stuart_score}")
    elif kevin_score == stuart_score:
        print("Draw")


if __name__ == '__main__':
    s = input()
    minion_game(s)
'''

def minion_game(string):
    stuart_score = 0
    kevin_score = 0
    s = len(string)
    for i in range(s):
        if string[i] in 'AEIOU':
            kevin_score += s - i

        else:
            stuart_score += s - i
        
    if kevin_score > stuart_score:
        print(f"Kevin {kevin_score}")
    elif kevin_score < stuart_score:
        print(f"Stuart {stuart_score}")
    elif kevin_score == stuart_score:
        print("Draw")