import sys
input = sys.stdin.readline

stack = []
N = int(input().strip())
for _ in range(N):
  command = input().strip()
  
  if command in ['pop', 'top']:
    if len(stack) == 0:
      # -1 출력
      print(-1)
    else:
      if command == 'top':
        print(stack[-1])
      else:
        print(stack.pop())
  else:
    if command == 'empty':
      if len(stack) == 0:
        print(1)
      else:
        print(0)
    elif command == 'size':
      print(len(stack))
    else:
      stack.append(int(command.split(' ')[1]))
