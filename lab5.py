"""stack = []
postfix = ""

expression = input("Enter infix expression: ")

for ch in expression:

    if ch.isalnum():
        postfix += ch

    elif ch == '(':
        stack.append(ch)

    elif ch == ')':
        while stack[-1] != '(':
            postfix += stack.pop()
        stack.pop()

    else:
        while stack and stack[-1] != '(':
            postfix += stack.pop()
        stack.append(ch)

while stack:
    postfix += stack.pop()

print("Postfix Expression:", postfix)"""


stack = []

expression = input("Enter postfix expression: ")

for ch in expression:

    if ch.isdigit():
        stack.append(int(ch))

    else:
        b = stack.pop()
        a = stack.pop()

        if ch == '+':
            stack.append(a + b)

        elif ch == '-':
            stack.append(a - b)

        elif ch == '*':
            stack.append(a * b)

        elif ch == '/':
            stack.append(a / b)

print("Final Result:", stack.pop())