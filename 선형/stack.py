stack = [None, None, None, None]
top =- 1

top+= 1
stack[top] = "컵1"
top += 1
stack[top] = "컵2"
top += 1
stack[top] = "컵3"

print("--스택상태--")
for i in reversed(stack):
    print(i)