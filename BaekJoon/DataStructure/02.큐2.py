import sys
from collections import deque

input = sys.stdin.readline

N = int(input().strip())
q = deque([])
for _ in range(N):
  command = input().strip()
  if command == 'pop':
    if len(q) == 0:
      print(-1)
    else:
      print(q.popleft())
  elif command == 'size':
    print(len(q))
  elif command == 'empty':
    print(0 if len(q) else 1)
  elif command == 'front':
    print(-1 if len(q) == 0 else q[0])
  elif command == 'back':
    print(-1 if len(q) == 0 else q[-1])
  else:
    q.append(int(command.split(' ')[1]))