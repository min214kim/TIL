# Python 기초
- 근거: [python tutorial](https://docs.python.org/3/tutorial/index.html)
- *스타일 가이드*: [pep 8](https://peps.python.org/pep-0008/)
  - 스타일 가이드는 글쓰기 양식같은 것. 잘 지키는 것이 매우 중요하다.

## 스타일 가이드
- '+', '=' 와 같은 연산자는 앞뒤로 띄어쓴다.
- 주석 # 옆은 띄어쓴다.
- 코드 중간에 주석을 넣을 땐 두번띄어쓰기, #, 한번띄어쓰기
- 변수명 설정 : 예측가능하게 / 복수형으로 (변수 안에 2개 이상의 객체가 있는 경우)/ 길이가 너무 길어지지 않다면 변수 타입까지 작성하면 좋음 
  - ex) l1(X) location(O) series_list(O)

## 기초 문법
    - 프로그래밍 언어란 컴퓨터에게 일을 시키는 언어
    - 언어이기 때문에 문법 중요
    - 저장 / 조건 / 반복 세 가지가 가장 기초이자 근간
      - 저장: **변수**(이름) 에 **데이터**(값)을 저장
      - 조건:
      - 반복:


## 1. 들여쓰기
- 코드 블록을 구분할 때는 들여쓰기 (identation)를 사용한다.
- 들여쓰기는 space 4칸 혹은 tab 1칸
- 한 코드 안에서는 한 종류의 들여쓰기를 사용한다.
```python
print('hello')
print('world')

a = 'apple'

if True:
    print(True)
else:
    print(False)
```

## 2. 변수(Variable)
### `변수`에 `값`을 `저장`한다! 
### 변수: 이름, 값: 객체
- 객체(object) : 숫자, 문자, 클래스 등 값을 가지고 있는 모든 것
- 동일 변수에 다른 객체 할당 가능

|코드|결과|설명|
|---|---|---|
|`x = '김민서'`||변수는 할당연산자 `=` 를 통해 할당된다.|
|`type(x)`|str|데이터 타입을 확인한다.|
|`id(x)`|4389961968|해당 값의 메모리 주소를 확인한다.|
|`del`||지정한 변수가 삭제된다.|

### 변수 할당
|코드|결과|설명|
|---|---|---|
|`x, y = 1, 2` <br> print(x, y)|1 2|두 개의 변수에 값을 동시에 할당하는 것이 가능하다.|
|`x, y = 1`|ERROR|두 변수에 하나의 값을 할당 시 오류가 뜬다.|
|`x, y = 1, 2, 3`|ERROR|마찬가지로 오류가 뜬다.|

### 실습문제
> x, y = 10, 20 일 때 변수 x와 y의 값을 바꿔봅시다.
```
1. 임시변수 사용
        tmp = x
        x = y
        y = tmp
2. pythonic 사용
        x, y = y, x
3. 그외
        x = x + y
        y = x - y
        x = x - y
```

### 식별자 (Identifiers)
#### 식별자란?
- 파이썬에서 식별자는 변수, 함수, 모듈, 클래스 등을 식별하는데 사용되는 **이름(name)**이다.
#### 주의사항
  - 식별자의 이름은 영문 알파벳, _, 숫자로 구성된다.
  - 첫 글자에 숫자가 올 수 없다.
  - 아래 키워드는 사용할 수 없다.<br> 
    *False, None, True, and, as, assert, async, await, break, class, continue, def, del, elif, else, except, finally, for, from, global, if, import, in, is, lambda, nonlocal, not, or, pass, raise, return, try, while, with, yield*
  - 사용할 수 없는 키워드를 직접 불러올 수 있다.
  ```python
  improt keyword
  print(keyword.kwlist)
  ``` 
  - 한글 사용은 하지 않는다.
  - 내장함수나 모듈 등의 이름으로 만들면 안된다. 해당 함수가 더 이상 동작하지 않게 된다.
  - 내장함수에 다른 값을 할당했을 경우, del을 사용한다.
  ```python
  print = 'hi'
  print(100)
  --> ERROR

  del print
  print('good')
  --> good
  ```
  - 내장함수를 불러올 수 있다.
  ```python
  dir(__builtins__)
  ```
### 사용자 입력 (input)
- 사용자로부터 즉시 값을 입력받을 수 있는 내장함수
- 입력받은 값은 항상 str(문자열) 형태로 반환된다.
```
data = input('이름을 입력해 주세요')
print(data)
```

## 3. 주석 (Comment)
- 한 줄 주석은 `#`로 표현한다.
- 여러줄 주석은 한줄씩 #를 사용하거나, ```를 사용한다.
- 여루줄 문자열은 주로 함수/클래스를 설명(docstring)하기 위해 활용된다.
- cmmd + / 를 활용해 주석처리한다.


## 4. 자료형 (Data Type) : 이름에 저장되는 **값**
### 종류
- **Boolean Type** 불린형
- **Numeric Type** 수치형
  - int (정수, integer)
  - float (실수)
  - complex (복소수)
- **String Type** 문자열
- None 타입

## Boolean Type
- True와 False로 이루어진, 비교/논리 연산 수행 등에 활용되는 타입
- 파이썬의 모든 값은 예 아니오로 바꿀 수 있다.
- 비어있다와 비슷한 개념은 False 라고 볼 수 있다.
```
0, 0.0, (), [], {}, '', None
```
- bool() 함수를 통해 특정 데이터가 True 인지 False인지 검증할 수 있다.
```python
bool('')
--> False

bool([1, 2, 3])
--> True
```

## Numeric Type
- int : 정수
- 파이썬에서 표현할 수 있는 가장 큰 수
  - sys.maxsize의 값은 2**63이나, 파이썬은 int에서 오버플로우(데이터 타입별 사용 가능한 메모리 크기 정해져있는 것)가 없다. -> 현재 남아있는 만큼의 가용 메모리만큼 출력 가능!
- float : 실수
  - 부동소수점 사용 과정에서 약간의 오류가 생기기도 함
  - 실수의 경우, 값을 처리할 때 조심! round를 써서 반올림/내림을 한다.
    - 그러면 a,b가 같은 값인지 어떻게 확인하나? : math를 import한 후, `math.isclose(a, b)`를 사용
  - 올림: ceil, 내림: floor 
  - 5e3 : e에 0을 3개 붙이겠다는 것 = 5000.0
- complex: 복소수
  - 허수부분: j로 표현 

## String Type
- `''` 혹은 `""` 사용
- **input을 통해 받은 값은 항상 str타입니다**
- immutable하며, iterable(순회 가능)하다.
- ``` 이 안에 넣으면, 문자열 안에 작은따옴표 혹은 큰따옴표를 쓰거나 여러 줄을 사용할 때 편리하다.```
- escape sequence
  |예약문자|내용|
  |---|---|
  |\n|줄바꿈|
  |\t|탭|
  |\r|캐리지리턴|
  |\0|널|
  |\\|\|
```python
print('철수\'안녕\'')
--> 철수 '안녕'
```
- formatting
  - %-formatting

  |%d|정수|
  |---|---|
  |%f|실수|
  |%s|문자열|
  ```python
  nume, score = '김민서' 4.3
  print('내 이름은 %s, 성적은 %F' % (name, score))
  --> 내 이름은 김민서, 성적은 4.300000
  ```

  - str.format()
  ```python
  print('내 이름은 {}, 성적은{}'.format(name, score))
  --> 내 이름은 김민서, 성적은 4.3
  ```

  - f-string
  ```python
  print(f'내 이름은 {name}, 성적은 {score}')
  --> 내 이름은 김민서, 성적은 4.3
  ```


## None Type
- None도 값이다.