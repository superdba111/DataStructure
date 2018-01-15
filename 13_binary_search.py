def binary_search(alist, item):
    first = 0
    last = len(alist) - 1
    while first <= last:
        mid = (first + last) // 2
        if alist[mid] == item:
            return True
        elif item < alist[mid]:
            last = mid - 1
        else:
            first = mid + 1
    return False

def binary_search_2(alist, item):
    n = len(alist)
    if n > 0:
        mid = n//2
        if alist[mid]==item:
          return True
        else:
          if item<alist[mid]:
            return binary_search_2(alist[:mid],item)
          else:
            return binary_search_2(alist[mid+1:],item)
    return False


testlist = [0, 1, 2, 8, 13, 17, 19, 32, 42 ]
print(binary_search(testlist, 3))
print(binary_search(testlist, 13))
print(binary_search_2(testlist, 3))
print(binary_search_2(testlist, 13))