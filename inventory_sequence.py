# inventory_sequence.py
# Andrew Lounsbury
# 20/3/23
# Purpose: generate the inventory sequence; https://www.youtube.com/watch?v=rBU9E-ZOZAI

import pandas as pd
sequence = [0]
highestNum = 0

# counts the number of occurrences of num in sequence
def count_num(num, sequence):
    total = 0
    for s in sequence:
        if s == num:
            total += 1
    return total

# computes up to the n-th number in the sequence
def generate(sequence, n):
    num = 0
    # while the sequence has less than n numbers
    while len(sequence) < n:
        if sequence[len(sequence) - 1] == 0:
            i = 0
            while i < 1000 and len(sequence) < n:
                val = count_num(i, sequence)
                sequence.append(val)
                i += 1
                if val == 0:
                    i = 0

generate(sequence, 100)
print(sequence)