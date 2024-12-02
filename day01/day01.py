from collections import Counter

from aocd import get_data

data = get_data(day=1)

# Read lines into two lists. This uses a bit of "zip magic" to transpose the data.
# Basically, the inner list is a list of tuples, where each tuple contains the corresponding elements of the two lists.
# The * operator unpacks the list of tuples into two lists.
l1, l2 = zip(*[map(int, line.split()) for line in data.splitlines()])

# Sum over differences of sorted list using a generator expression
# Chances are, this would be faster in numpy because it can do vectorized operations.
# But this is a one-liner that works with the standard library and it is _fast enough_.
print(sum(abs(a - b) for a, b in zip(sorted(l1), sorted(l2))))

# Part 2
count = Counter(l2)

answer = sum(a * count[a] for a in l1)
print(answer)
