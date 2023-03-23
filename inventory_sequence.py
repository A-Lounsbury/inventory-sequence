# inventory_sequence.py
# Andrew Lounsbury
# 20/3/23
# Purpose: generate the inventory sequence; https://www.youtube.com/watch?v=rBU9E-ZOZAI

import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

# counts the number of occurrences of num in sequence
def count_num(num, sequence):
    total = 0
    for s in sequence:
        if s == num:
            total += 1
    return total

# computes up to the n-th number in the sequence
def generate_inventory(n):
    sequence = [0]
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
    return sequence

n1 = 1000
sequence = generate_inventory(n1)
df1 = pd.DataFrame(sequence, columns=["Numbers"])

indices = []
for i in range(n1):
    indices.append(i)

df1["index"] = indices
sns.scatterplot(x="index", y = "Numbers", data=df1)
plt.show()

n2 = 10000
sequence = generate_inventory(n2)
df2 = pd.DataFrame(sequence, columns=["Numbers"])

indices = []
for i in range(n2):
    indices.append(i)

df2["index"] = indices
sns.scatterplot(x="index", y = "Numbers", data=df2)
plt.show()

n3 = 100000
sequence = generate_inventory(n3)
df3 = pd.DataFrame(sequence, columns=["Numbers"])

indices = []
for i in range(n3):
    indices.append(i)

df3["index"] = indices
sns.scatterplot(x="index", y = "Numbers", data=df3)
plt.show()