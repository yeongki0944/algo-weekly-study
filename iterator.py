# 리스트 생성
my_list = [1, 2, 3, 4, 5]

# Iterator로 변환
iterator_obj = iter(my_list)
print(type(iterator_obj))

try:
    while True:
        # 다음 값을 가져와서 출력
        element = next(iterator_obj)
        print(element)
except StopIteration:
    # StopIteration 예외가 발생하면 루프 종료
    pass
