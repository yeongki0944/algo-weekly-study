import sys
# input()
# 키보드 입력을 받는 함수 - Enter를 치기 전까지 입력한 것을 str 타입으로 리턴
# age = int(input("나이를 입력하세요: "))


# s = input().split()
# print(s)
# print(type(s))
#
# b = map(int, s)
# print(b)
# print(type(b))



# 리스트 생성
my_list = [1, 2, 3, 4, 5]
# 리스트의 메모리 사용 확인
print("Memory Usage (List):", sys.getsizeof(my_list))

# 리스트 생성
numbers = [1, 2, 3, 4, 5]
# 제곱 함수를 각 요소에 적용한 map 객체 생성
squared = map(lambda x: x**2, numbers)

# map 객체의 메모리 사용 확인
print("Memory Usage (Map):", sys.getsizeof(squared))
squared_list = list(squared)

# Lazy 평가
print("Memory Usage (Map):", sys.getsizeof(squared))
print("Memory Usage (squared_list):", sys.getsizeof(squared_list))
