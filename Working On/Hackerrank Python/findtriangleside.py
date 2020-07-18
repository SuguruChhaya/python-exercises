import math


len_ab = float(input())
len_bc = float(input())

len_ac = math.sqrt(len_ab ** 2 + len_bc ** 2)

#*This is returned in radians
answer = math.degrees(math.acos((len_ab ** 2 - len_bc ** 2 - len_ac ** 2) / (-2 * len_bc * len_ac)))

#*Using the unicode degree character
print(str(round(answer)) + str(u"\u00b0"))
