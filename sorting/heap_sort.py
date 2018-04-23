def sift(data, low, high):
    i = low
    j = 2*i + 1
    tmp = data[i]
    while j <= high:  #inside dui
        if j + 1 <= high and data[j] < data [j+1]:  #if there is a right side child and it is bigger than left child
            j += 1 # j point to right child
        if data[j] > tmp:  # child is bigger than the most leader
            data[i] = data [j] #child fill in the father's position
            i = j  #child becomes a new dad
            j = 2*i + 1  #new child
        else:
            break
    data[i] = tmp  #the most leader in dad's position

def heap_sort(data):
    n = len(data)
    for i in range( n//2-1, -1, -1):
        sift(data, i, n-1)
    #dui is ready

    # li = []
    # for i in range(n-1, -1, -1):
    #     li.append(data[0])
    #     data[i]=data[0]
    #     sift(data, 0, i-1)

    for i in range(n-1, -1, -1):  #i point to last position od dui
        data[0], data[i] = data[i], data[0]  #leader retired and one is up
        sift(data, 0, i-1)  #adjust the new leader

if __name__ == "__main__":
    alist = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    heap_sort(alist)
    print(alist)
