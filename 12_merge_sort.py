def merge_sort(alist):
    if len(alist) <= 1:
        return alist
    # 二分分解
    mid = len(alist)//2
    left = merge_sort(alist[:mid])
    right = merge_sort(alist[mid:])
    # 合并
    return merge(left,right)

def merge(left, right):
    '''合并操作，将两个有序数组left[]和right[]合并成一个大的有序数组'''
    #left与right的下标指针
    l, r = 0, 0
    result = []
    while l<len(left) and r<len(right):
        if left[l] < right[r]:
            result.append(left[l])
            l += 1
        else:
            result.append(right[r])
            r += 1
    result += left[l:]
    result += right[r:]
    return result

def merge_sort2(li, low, mid, high):
    i = low
    j = mid +1
    ltmp = []
    while i <= mid and j <= high:
        if li[i] < li[j]:
            ltmp.append(li[i])
            i += 1
        else:
            ltmp.append(li[j])
            j += 1
    while i <= mid:
        ltmp.append(li[i])
        i += 1
    while j <= high:
        ltmp.append(li[j])
        j += 1
    li[low:high+1] = ltmp #read the slice back


def mergeSort(li, low, high):
    if low < high:
        mid = (low+high) // 2
        mergeSort(li, low, mid)
        mergeSort(li, mid+1, high)
        merge_sort2(li, low, mid, high)


if __name__ == "__main__":
    li = [54,26,93,17,77,31,44,55,20]
    print(li)
    sorted_li = merge_sort(li)
    print(sorted_li)
    sorted_li2 = mergeSort(li, 0, len(li)-1)
    print(sorted_li)