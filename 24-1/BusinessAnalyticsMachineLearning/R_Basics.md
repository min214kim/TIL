`ls()` : 어떤 변수들이 있는지 출력 

`rm(list = ls())` : 변수 싹 다 지우기 

11

- 변수 지정
    - `a < - 6`
    - `b < - “a”`
- 변수 이름
    - letter, 숫자,
    - 대소문자 구분
    - .혹은 문자로 시작, 숫자로 시작 불가

12

벡터 데이터구조 

- 하나의 숫자는 길이 1인 벡터
- ordered collection of data of the same data type
- `x1 <- c(10, 8, 5, 3.3, 2, 15)`
- `class(x1)` : “numeric”, 데이터 타입 반환

13

![Screenshot 2024-03-28 at 2.13.53 PM.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/7bd8222d-d892-4000-b428-6e3a0d4550f3/b65a48a5-12a0-4962-b7b1-109eec419a43/Screenshot_2024-03-28_at_2.13.53_PM.png)

14

![Screenshot 2024-03-28 at 2.19.26 PM.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/7bd8222d-d892-4000-b428-6e3a0d4550f3/84bc6532-f30d-4fe5-82c3-f59a5283e937/Screenshot_2024-03-28_at_2.19.26_PM.png)

15

![Screenshot 2024-03-28 at 2.27.03 PM.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/7bd8222d-d892-4000-b428-6e3a0d4550f3/260ec0d5-5886-4c6a-8585-1e8118fe38d2/Screenshot_2024-03-28_at_2.27.03_PM.png)

17

Functions and Packages 

- R에서 패키지 다운받기
- library(ggplot2) : 이거로 패키지 로딩 해야함

빗자루 모양 버튼으로 변수들 다 지울 수 있다

---

### Data Structure

- Data Frame : 2차원 (스프레드시트 생각하면 됨 )
- array : 2차원 이상
    - matrix를 array라고 보면 2차원 이상
- list : 다른 구조들을 포함해서 만든 구조
- 하나의 컬럼에는 하나의 데이터타입만!
- subsetting : data[row,col] 이런식
- command : 파일보기

### List

- collection of data of any types
- x ← list(c(5,4,-1), c(”john”, “nick”)
- 쓸일은 거의 없으나 결과를 뽑아줄 때 리스트 형태로 뽑아주는 경우가 많음!

### Matrix

x2 ← (c(1:12), ncol = 2) # ncol: 컬럼개수 

불러오기 : mean(x2[,1])

### DataFrame and DataFiles

- 어떻게 읽을건가!

### Missing Value

- character 에 missing value가 있는걸 읽으려면, na.strings = “”  라는 옵션 줘야함
- character을 범주로 생각하기