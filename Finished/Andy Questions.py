a = input("Convert to pig latin: ")

def piglatin(string):
    for char in range(0, len(string)):
        b = string[char]
        if char == 0 and (b == "a" or b == "e" or b == "i" or b == "o" or b == "u"):
            string = string + "way"
            break
        elif b == "a" or b == "e" or b == "i" or b == "o" or b == "u":
            save = string[:char]
            string = string[char:] + save + "ay"
            break
    return string


print(piglatin(a))
#!I wrote some fancy testing
assert piglatin("computer") == "omputercay"
assert piglatin("yellow") == "ellowyay"
assert piglatin("algorithm") == "algorithmway"
assert piglatin("hello world") == "ello worldhay"


def reverseLookup(dictionary, target):
    key_list = []
    for key, value in dictionary.items():
        if value == target:
            key_list.append(key)
    return key_list


# multiple keys
assert reverseLookup({"a": 1, "b": 1, "c": 1}, 1) == ['a', 'b', 'c']
# single key
assert reverseLookup({"a": 1, "b": 2, "c": 2}, 1) == ['a']
# no keys
assert reverseLookup({"a": 2, "b": 2, "c": 2}, 1) == []
