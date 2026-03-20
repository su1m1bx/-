def isEmpty(stack):
    if top < 0:
        return True
    return False


def pop(stack):
    global top
    if isEmpty(stack):
        print("스택이 공백 상태입니다")
        return
    data = stack[top]
    stack[top] = None
    top -= 1
    return data

stack = ["A", "B", "C"]
global top
top = 2

print("스택 상태:")
print(stack)
pop(stack)
print(stack)
pop(stack)
print(stack)
pop(stack)
print(stack)
pop(stack)
print(stack)