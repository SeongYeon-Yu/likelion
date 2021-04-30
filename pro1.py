def is_prime(num):
  a=0
  for i in range(2, num):
    if num % i == 0:
      a=1
  if(a==0):
    return True  # 들어온 num이 소수이면 True를 반환하고
  else:
    return False # 소수가 아니면 False를 반환하는 함수

def calculate_prime_number(length):
  a = []
  cnt =0
  i=2
  while(cnt!=length):
    if(is_prime(i)):
      cnt+=1
      a.append(i)
    i+=1
  return a
    # 소수를 2부터 length개만큼 담고 있는 배열을 반환하는 함수
    # 예를 들어 length에 2를 입력하면 [2, 3]을 반환하고
    # length에 5를 입력하면 [2, 3, 5, 7, 11]을 반환해야 함
    # is_prime 함수를 사용하면 편하50게 코딩할 수 있음
n = int(input('Length? '))
print(calculate_prime_number(n))