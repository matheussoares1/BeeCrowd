def check_parentheses(expression):
    stack = []
    for char in expression:
        if char == '(':
            stack.append('(')
        elif char == ')':
            if not stack:
                return "incorrect"
            stack.pop()
    return "correct" if not stack else "incorrect"


expressions = []
expressions.append(input(""))

for expression in expressions:
    print(check_parentheses(expression))
