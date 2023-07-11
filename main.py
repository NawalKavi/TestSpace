data = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
top = -1
pos = len(data) - 1


def pop():
    global top, data
    return data[top]


def push(item):
    global top, data
    top += 1
    if top > (len(data) - 1):
        print("ERROR")
    else:
        data[top] = item
    return data[top]


print(top)
push("Apple")
push("melon")
push("lemon")
print(pop())
print(pop())
print(data)
