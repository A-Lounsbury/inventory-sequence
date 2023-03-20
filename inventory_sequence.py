# take_inventory.py
# Andrew Lounsbury
# 20/3/23
# Purpose: generate the inventory sequence; https://www.youtube.com/watch?v=rBU9E-ZOZAI
sequence = [0]
highestNum = 0

def count_num(num, sequence):
    total = 0
    for s in sequence:
        if s == num:
            total += 1
    return total

def take_inventory(sequence, n):
    num = 0
    # while the sequence has less than n numbers
    while len(sequence) < n:
        print("len:", len(sequence))
        if sequence[len(sequence) - 1] == 0:
            i = 0
            while i < 100 and len(sequence) < n:
                val = count_num(i, sequence)
                sequence.append(val)
                i += 1
                if val == 0:
                    i = 0

take_inventory(sequence, 100)
print(sequence)