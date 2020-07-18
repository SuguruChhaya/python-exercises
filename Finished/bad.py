def shift(seq):
    a = seq[0]
    seq.remove(a)
    seq.append(a)
    return seq

print(shift(["-2","-5","4"]))

