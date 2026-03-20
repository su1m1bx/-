stack = ["컵1", "컵2", "컵3", "컵4"]
top = len(stack)-1

data = stack[top]
stack[top] = None
top -= 1
print("스택 상태:", stack)

data = stack[top]
stack[top] = None
top -= 1
print("스택 상태:", stack)

data = stack[top]
stack[top] = None
top -= 1
print("스택 상태:", stack)