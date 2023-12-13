# 1. Iterator가 Iterable인 경우:
# my_list = [1, 2, 3, 4, 5]
#
# # Iterator로 변환
# iterator_obj = iter(my_list)
#
# try:
#     while True:
#         # Iterator에서 값을 가져와 출력
#         element = next(iterator_obj)
#         print(element)
# except StopIteration:
#     # StopIteration 예외가 발생하면 루프 종료
#     pass



# 2. Iterable이지만 Iterator가 아닌 경우:
my_list = [1, 2, 3, 4, 5]

# Iterable은 Iterator가 아닙니다.
try:
    iterator_obj = iter(my_list)
    while True:
        # Iterable에서 값을 직접 가져와 출력 (TypeError 발생)
        element = next(iterator_obj)
        print(element)
except TypeError as e:
    print("TypeError:", e)
