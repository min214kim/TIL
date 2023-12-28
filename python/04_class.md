# 클래스

## OOP (객체 지향 프로그래밍)
Object Oriented Program 
- 절차 지향 프로그램에 비해 성능 향상 
- 사물을 객체화
- 재사용 극대화
- 상속 개념 : 코드의 재사용 용이 
  - 개선, 유지보수 경제적
  - side effect 최소화
- 경우에 따라서는 절차지향이 빠를 때도 있다 

## 클래스와 인스턴스 
- 클래스 : 붕어빵 틀과 같은 것
- 인스턴스 : 객체에 포함되는, 클래스로 찍어내는 객체
  
    ```python
    class Dog(object): # object 상속 : 괄호를 비워둬도, 아예 쓰지 않아도 에러가 나지 않음 
        # 클래스 속성 (클래스 변수)
        species = 'frstdog'

        # 초기화/ 인스턴스 속성 : 초기화 시 반드시 실행되는 속성 
        def __init__(self, name, age):
            self.name = name 
            self.age = age 

    # 클래스 정보
    print(Dog) 
    --> <class'__main__.Dog>
    # 인스턴스화
    a = Dog('miky', 2) # self에 들어갈 것은 자동으로 들어간다. 
    b = Dog('kimmy', 4)

    ```
    - id(a)와 id(b)와 id(c)는  다 다른 값을 가진다.
-  네임스페이스 : 객체를 인스턴스화할 때 저장된 공간 
- 클래스 변수 : 직접 접근 가능, 공유 
  - 직접접근 : Dog.species, a.species라고 직접적으로 접근이 가능하다. 
- 인스턴스 변수 : 객체마다 별도 존재 
- 인스턴스 속성 확인


- 
## self

## 인스턴스 메소드
## 인스턴스 변수 

## name space
## __init__, __del__ (생성자 소멸자)