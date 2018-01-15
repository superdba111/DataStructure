# coding:utf-8

class Queue(object):
    """队列"""
    def __init__(self):
        self.__items = []

    def is_empty(self):
        return self.__items == []

    def enqueue(self, item):
        """进队列"""
        self.__items.append(item)
        # use above for enqueue often, otherwise use the following
        #self.__items.insert(0, item)

    def dequeue(self):
        """出队列"""
        return self.__items.pop(0)
        #return self.__pop()

    def size(self):
        """返回大小"""
        return len(self.__items)

if __name__ == "__main__":
    q = Queue()
    q.enqueue("hello")
    q.enqueue("world")
    q.enqueue("itcast")
    print(q.size())
    print(q.dequeue())
    print(q.dequeue())
    print(q.dequeue())