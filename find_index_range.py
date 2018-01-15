li = [1, 2, 4, 3]
target = 3

def func1():
    for i in range(len(li)):
        for j in range(i+1, len(li)):
            if li[i]+li[j] == target:
                return(i, j)

def func2():
    pass

if __name__ == "__main__":
    print(func1())

