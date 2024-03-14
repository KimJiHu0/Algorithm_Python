# 다른 사람 풀이
S = input()

S = S.replace('XXXX', 'AAAA')
S = S.replace('XX', 'BB')

if 'X' in S:
  print(-1)
else:
  print(S)
  
# 원래 내가 하려던 풀이(정답확인했음) => 위 방식은 그리디가 아님
SS = input().split('.') # 문자열 .로 나눠줌.
temp = '' # 정답 변수

for x in SS:
  if len(x) % 2 == 1:  # 홀수면 덮을 수 없음
    print(-1)
    break
  while len(x) >= 4:  # 4보다 크면 AAAA 덮기
    temp += 'AAAA'
    x = x[4:]
  if len(x) == 2:  # 2가 남았으면 BB 덮기
    temp += 'BB'
    x = x[2:]
  temp += '.'  # 나눠준 . 붙이기
else:
  print(temp[:-1])  # 성공이면 마지막 . 제외하고 출력
