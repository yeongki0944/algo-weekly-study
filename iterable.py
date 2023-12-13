# Iterable 클래스 정의
class MyIterable:
    def __init__(self, data):
        self.data = data

    def __iter__(self):
        # Iterable은 __iter__ 메서드를 가지고 있음
        return iter(self.data)

# Iterable을 생성
my_iterable = MyIterable([1, 2, 3, 4, 5])
print(type(my_iterable))

# Iterator로 변환
my_iterator = iter(my_iterable)

# 값을 순차적으로 가져오기
print(next(my_iterator))  # 출력: 1
print(next(my_iterator))  # 출력: 2
