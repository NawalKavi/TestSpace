class Stack:

    def __init__(self):
        self.__data = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        self.__top = -1
        self.item = None

    def pop(self):
        if self.__top != -1:
            self.__top -= 1
            return self.__data[self.__top + 1]

    def data(self):
        return self.__data

    def push(self, item):
        self.__top += 1
        if self.__top > (len(self.__data) - 1):
            print("ERROR")
        else:
            self.__data[self.__top] = item
        return self.__data[self.__top]


myStack = Stack()
myStack.push("Melon")
myStack.push("Apple")
myStack.push("Grape")
print(myStack.pop())
print(myStack.data())
print(myStack.pop())
print(myStack.data())
print(myStack.pop())
print(myStack.data())
