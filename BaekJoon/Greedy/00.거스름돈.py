# 입력받은 값
input = int(input())
# 결과
result = 0
# 14
while 0 < input:
  # 5로 나누어 떨어질 경우
  if (input % 5 == 0):
    # 결과에 입력받은 값 // 5의 결과 담기
    result += input // 5
    break
  else:
    # 5로 나누어 떨어지지 않을 때
    # -2원을 해주면서 동전 갯수 result에 +1
    input -= 2
    result += 1

# 남은 돈 input이 0 미만이면 나누어 떨어지지 않음으로 -1 return
if input < 0:
  print(-1)
else:
  # 결과 반환
  print(result)