import sys

input = sys.stdin.readline
N = int(input().strip())

for _ in range(N):
  stack = []
  command = input().strip()
  for cmd in command:
    if '(' in cmd:
      stack.append(cmd)
    else:
      # if not stack:링 동일
      if len(stack) == 0:
        print("NO")
        break
      else:
        # 아래 조건을 추가하면 40ms인데
        # 빼면 64ms가 걸림
        if stack[-1] == '(':
          stack.pop()
  else:
    if len(stack) == 0:
      print("YES")
    else:
      print("NO")