"""if there are too many the repeatable numbers in the list, quick_sort is not good, the count_sort is the best"""

import random

def count_sort(A):

    # create counters initialized to zero
    frequencies = [0] * (max(A)+1)

    # count each item
    for value in A:
        frequencies[value] += 1

    # recreate sorted array
    writepos = 0
    for value, count in enumerate(frequencies):
        for i in range(count):
            A[writepos] = value
            writepos += 1

    return A

if __name__ == "__main__":
    alist = [4, 3, 2, 1, 4, 3, 2, 4, 3, 4]
    print(alist)
    bb = count_sort(alist)
    print(bb)

    data = []
    for i in range(20):
        data.append(random.randint(0,10))
    print(data)

    cc = count_sort(data)
    print(cc)
