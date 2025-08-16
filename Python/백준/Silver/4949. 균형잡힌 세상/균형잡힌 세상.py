import sys

while True:
    line = sys.stdin.readline().rstrip()
    if line == '.':
        break

    stack = []
    for ch in line:
        if ch in '([':
            stack.append(ch)
        elif ch == ')':
            if stack and stack[-1] == '(':
                stack.pop()
            else:
                print("no")
                break
        elif ch == ']':
            if stack and stack[-1] == '[':
                stack.pop()
            else:
                print("no")
                break
    else:
        print("yes" if not stack else "no")
