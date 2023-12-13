# https://velog.io/@magnoliarfsit/RePython-1.-self-%EC%9D%B4%ED%95%B4%ED%95%98%EA%B8%B0
class Foo:
    def func1():
        print("function 1")

    def getId(self):
        print(f'id(self) : {id(self)}')


f1 = Foo()
print(id(f1))
# id() 함수는 객체가 메모리 상에서 어느 위치에 저장되어 있는지를 나타내는 정수 값을 반환

f1.getId()
# self는 Class -> Instance의 주소값


Foo.func1()

# TypeError: getId() missing 1 required positional argument: 'self'
# Foo.getId()

Foo.getId(f1)