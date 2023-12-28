# Pandas
## 판다스를 사용하는 이유
- 많은 현업에서 사용하는 형태와 가장 비슷하다 
## 자료구조
- 데이터프레임과 시리즈가 있다.
1. 데이터프레임
   - 특징
     - 컬럼과 로우로 구성되어 있다. (2차원)
       - 컬럼 : feature(독립변수)
       - 로우 : 수집한 하나의 데이터
2. 시리즈
   - 특징
     - 데이터프레임보다 더 작은 자료구조
     - DF 에서 분리된 자료구조
     - 인덱스를 붙일 수 있는 일차원 구조 

## 함수, 명령어
   1. 생성
      - DF 생성방법: pd.DataFrame(data, index, columns)
       ```python
       data = [[1, 25], [3, 11], [5, 31]]
       df = pd.DaataFrame(data, columns = ['month', 'day'])
       df
       ```
       ```python
       data = {'month' : [1, 3, 5],
               'day' : [25, 11, 31]}
       df = pd.DataFrame(data, index=['first', 'second', 'third'])
       ```
       - Series 생성방법 : pd.Series([]) 
   2. 정보확인
       - .info() 
       - .head(), .tail()
       - df.columns, df.index
       - df.describe : 수치가 들어있는 컬럼에 대해 통계적 정보 반환 
       - df.transpose() : 인덱스와 컬럼 전환 
       - series.value_counts() : value별 개수를 반환 

    3. 인덱싱
       - df['column'] : 해당 컬럼의 data를 시리즈로 반환 (열 우선 인덱싱이 기본이다.)
         - df[['column']] : 해당 컬럼의 data를 dataframe으로 반환 
         - df['column'][0:2] : 해당 열의 0부터 1행을 시리즈로 반환
       - data.column : 다트연산자 이용 - 시리즈로 반환
       - df[['column1', 'column2', ...]] : 여러 컬럼을 한번에 반환할 때는 리스트로 컬럼명을 전달해야 한다. dataframe으로 반환함.
       - 조건인덱싱 : data.column[조건] - t/f 시리즈 반환
        - ``` python
             sort = data.위생업태명.str.contains('통닭|치킨', na=False)
             data.위생업태명[sort]
            ```
        - data.column.isin(['원소']) : 시리즈 원소가 집합형자료의 원소 적어도 1개와 일치하면 true를 반환  
        - data.column == 'str' : str과 일치하면 true반환 , &, | 연산자와 활용 가능 

    4. 컬럼 생성, 수정, 제거
        - df.rename(columns={바꿀 데이터 위치: 새로운 값}, inplace=True) : 컬럼명이 변경된 df를 반환 
        - del df['column'] : 컬럼 제거
        - df.drop(index) : 행 제거 

    5. 기타 함수 
       - str.slice() : 해당 컬럼의 데이터들을 슬라이싱
         - df.column.str.slice(start=x, stop=y) : 해당 컬럼의 모든 열에서의 문자를 11부터 16번째까지만 시리즈로 반환 
       - pd.to_numeric(df['column']) : 해당 컬럼을 숫자형으로 바꿔준다. 숫자형으로 바꾸면 컬럼끼리의 계산이 가능해진다. 
       - df.unique() :  중복 데이터 제외하고 반환
       - df.sort_values(by='column', ascending=T/F) : 해당 컬럼을 기준으로 크기순 정렬 ascending F일 시 큰 순서대로 정렬
       - df.isnull() : 값이 null이면 True 반환
         - df[df.column.isnull()] : 해당 컬럼이 null값인 경우 그 행을 df형태로 반환 
       - df.corr() : 상관계수를 구해주는 함수 
         - 보통 계수의 절대값이 0.3을 넘어가면 상관관계가 있다고 간주 
         - np.corrcoef(df['column1'], df['column2']..)
 

### 시리즈 

1. 특징

2. 함수
   
3. 


## 명령어
- set() : 중복 제거 후 데이터 확인시 많이 사용 
    - set(data.column) : 시리즈를 넘겨줌
    - set(data.위생업태명.values) : ?
- 문자열.contains(문자열1, na=) : 문자열 안에 문야열 1의 포함여부 T/F로 반환 
  - data.[column].str.contains('str', na=False) 
    - na = False : 결측치 제외한 나머지만 처리가 가능하도록
-  
