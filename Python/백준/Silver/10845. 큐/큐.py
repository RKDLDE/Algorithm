import sys
input = sys.stdin.readline

N = int(input())
queue = []

for _ in range(N):
    command = input().strip()

    if command.startswith("push"):
        _, value = command.split()
        queue.append(int(value))
        
    elif command == "pop":
        print(queue.pop(0) if queue else -1)
        
    elif command == "size":
        print(len(queue))
        
    elif command == "empty":
        print(0 if queue else 1)
        
    elif command == "front":
        print(queue[0] if queue else -1)
        
    elif command == "back":
        print(queue[-1] if queue else -1)