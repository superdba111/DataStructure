#coding: utf-8


def selection_sort(alist):
    n = len(alist)
    # need n-1 times ops
    for j in range(n-1):
        count = 0
        for i in range(0, n-1-j):
            if alist[i] > alist[i+1]:
                alist[i], alist[i+1] = alist[i+1], alist[i]
                count += 1
        if 0 == count:
            return
if __name__ == "__main__":
    alist = [54,226,93,17,77,31,44,55,20]
    selection_sort(alist)
    print(alist)
