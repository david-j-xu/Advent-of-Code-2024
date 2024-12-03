from collections import Counter

with open("input.txt") as f:
    lines = f.readlines()
    numbers = [list(map(int, line[:-1].split("   "))) for line in lines]
    # (a)
    first = sorted([number[0] for number in numbers])
    second = sorted([number[1] for number in numbers])
    
    diff = 0
    for x, y in zip(first, second):
        diff += abs(x - y)
    print(diff)

    #(b)
    count = Counter(second)
    print(sum([count[i] * i for i in first]))
    
        