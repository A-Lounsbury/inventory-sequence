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

print(generate_inventory(100))

n = 1000
sequence = generate_inventory(n)
df = pd.DataFrame(sequence, columns=["Numbers"])
df["index"] = [i for i in range(n)]
sns.scatterplot(x="index", y = "Numbers", data=df)
plt.savefig("images/1000.png")
plt.show()

n = 10000
sequence = generate_inventory(n)
df = pd.DataFrame(sequence, columns=["Numbers"])
df["index"] = [i for i in range(n)]
sns.scatterplot(x="index", y = "Numbers", data=df)
plt.savefig("images/10000.png")
plt.show()

n3 = 100000
sequence = generate_inventory(n3)
df3 = pd.DataFrame(sequence, columns=["Numbers"])
df["index"] = [i for i in range(n)]
sns.scatterplot(x="index", y = "Numbers", data=df)
plt.savefig("images/100000.png")
plt.show()

# Plots of Averages
n = 10
sequence = generate_inventory(n)
average_sequence = []
sum = 0
for i, s in enumerate(sequence):
    sum += s
    average = sum / (i + 1)
    average_sequence.append(average)

df_averages = pd.DataFrame(average_sequence, columns=["Average"])
df_averages['index'] = [i for i in range(n)]
sns.scatterplot(x="index", y="Average", data=df_averages)
plt.savefig("images/average_10.png")
plt.show()

n = 100
sequence = generate_inventory(n)
average_sequence = []
sum = 0
for i, s in enumerate(sequence):
    sum += s
    average = sum / (i + 1)
    average_sequence.append(average)

df_averages = pd.DataFrame(average_sequence, columns=["Average"])
df_averages['index'] = [i for i in range(n)]
sns.scatterplot(x="index", y="Average", data=df_averages)
plt.savefig("images/average_100.png")
plt.show()

n = 1000
sequence = generate_inventory(n)
average_sequence = []
sum = 0
for i, s in enumerate(sequence):
    sum += s
    average = sum / (i + 1)
    average_sequence.append(average)

df_averages = pd.DataFrame(average_sequence, columns=["Average"])
df_averages['index'] = [i for i in range(n)]
sns.scatterplot(x="index", y="Average", data=df_averages)
plt.savefig("images/average_1000.png")
plt.show()

n = 10000
sequence = generate_inventory(n)
average_sequence = []
sum = 0
for i, s in enumerate(sequence):
    sum += s
    average = sum / (i + 1)
    average_sequence.append(average)

df_averages = pd.DataFrame(average_sequence, columns=["Average"])
df_averages['index'] = [i for i in range(n)]
sns.scatterplot(x="index", y="Average", data=df_averages)
plt.savefig("images/average_10000.png")
plt.show()

n = 100000
sequence = generate_inventory(n)
average_sequence = []
sum = 0
for i, s in enumerate(sequence):
    sum += s
    average = sum / (i + 1)
    average_sequence.append(average)

df_averages = pd.DataFrame(average_sequence, columns=["Average"])
df_averages['index'] = [i for i in range(n)]
sns.scatterplot(x="index", y="Average", data=df_averages)
plt.savefig("images/average_100000.png")
plt.show()