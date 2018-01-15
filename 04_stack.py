# coding:utf-8

class Stack(object):
    """栈"""
    def __init__(self):
         self.__items = []

    # def is_empty(self):
    #     """判断是否为空"""
    #     return self.__items == []

    def push(self, item):
        """加入元素"""
        self.__items.append(item)

    def pop(self):
        """弹出元素"""
        return self.__items.pop()

    def peek(self):
        """返回栈顶元素"""
        if self.__items:
            return self.__items[-1]
        else:
            return None

    def is_empty(self):
        """ judge if it is empty"""
        return self.__items == []
        # return not self.__item  (same as above)

    def size(self):
        """返回栈的大小"""
        return len(self.__items)

if __name__ == "__main__":
    stack = Stack()
    stack.push("hello")
    stack.push("world")
    stack.push("itcast")
    print(stack.size())
    print(stack.peek())
    print(stack.pop())
    print(stack.pop())
    print(stack.pop())