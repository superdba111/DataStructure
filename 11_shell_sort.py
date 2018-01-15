#coding: utf-8

def shell_sort(alist):
    n = len(alist)
    # 初始步长
    gap = n // 2
    while gap > 0:
        # 按步长进行插入排序
        for j in range(gap, n):
            i = j
            # 插入排序
            while i>0:
                if alist[i] < alist[i-gap]:
                   alist[i], alist[i-gap] = alist[i-gap], alist[i]
                   i -= gap
                else:
                    break

        gap //= 2

alist = [54,26,93,17,77,31,44,55,20]
shell_sort(alist)
print(alist)