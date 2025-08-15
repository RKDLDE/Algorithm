from collections import deque
import sys

input = sys.stdin.readline
n = int(input())
deque = deque()

for _ in range(n):
    command = input().strip()

    if command.startswith('1'):
        _, value = command.split()
        deque.appendleft(int(value))
    
    elif command.startswith('2'):
        _, value = command.split()
        deque.append(int(value))

    elif command == '3':
        print(deque.popleft() if deque else -1)

    elif command == '4':
        print(deque.pop() if deque else -1)

    elif command == '5':
        print(len(deque))

    elif command == '6':
        print(0 if deque else 1)

    elif command == '7':
        print(deque[0] if deque else -1)

    elif command == '8':
        print(deque[-1] if deque else -1)