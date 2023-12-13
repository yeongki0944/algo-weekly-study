# https://www.acmicpc.net/problem/1158

# N K
# 7 3

from queue import Queue

# N, K = input().split()
# 이렇게 입력받으면 str으로 입력받게 되는데, map을 사용하게 되면 타입을 명시적으로 변환이 가능하다
# N, K = int(input().split()) - 이것은 에러가 발생함.
N, K = map(int, input().split())

# 큐 생성
my_queue = Queue()

# 큐에 데이터 입력
[my_queue.put(i) for i in range(1, N + 1)]


# 요세푸스 순열을 만들기 위해 필요한 변수
count = 0
result = []

while len(result) < N:
    item = my_queue.get()
    count += 1

    if count >= K:
        result.append(item)
        count = 0
    else:
        my_queue.put(item)


print(result)
