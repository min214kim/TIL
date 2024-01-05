# 판다스 기초
## 판다스란?
- 데이터 분석을 위한 라이브러리
- numpy 라이브러리 기반
- 판다스를 사용하는 이유
  - dataframe table사용
  - 여러 포멧의 파일을 읽고 쓸 수 있다 (sql, html 등..)
  - 인덱싱, logic, subsetting 등 사용 가능
  - 결측리 관리, 데이터 수정과 restructure에 용이 

## Series
### 1. Series 란
  - 인덱스와 함께 array를 가지고 있는 판다스의 데이터 구조
  - named index가 있다는 점에서 NumPy array와 다름 (넘파이는 그냥 숫자 인덱스가 있다)
    - series에도 numeric index가 있기는 있음
  - Formal Definition: One-dimensional ndarray with axis labels
- help(pd.Series)로 여러 기능들을 볼 수 있음
- pd.Series + shift enter : 어떤걸 넣어야하는지
### 2. 생성
```python
myindex = ['USA', 'Canada', 'Mexico']
mydata = [1776, 1876, 1821]
myser = pd.Series(data=mydata, index=myindex) 
# 순서만 맞다면 pd.Series(mydata, myindex)라고 줘도 된다
```
   - 딕셔너리로 생성
  
```python
ages = {'MIN' : 23, 'Tom' : 24, 'Frank' : 10}
pd.Series(ages)
```
### 3. 인덱싱
```python
# numeric index 사용
myser[0] --> 1776
# name index 사용
myser['USA'] --> 1776
```
- data.keys() : Series의 인덱스 반환 

### 4. 연산
   - 넘파이 기반이기 때문에 연산이 가능하다
```python
sales_q1 = {'Japan': 80, 'China' : 450, 'India' : 200, 'USA' : 250}
sales_q2 = {'Brazil' : 100, 'China' : 500, 'India' : 210, 'USA' : 260}
sales_q1 * 2 --> 모든 value들에 2가 곱해져서 반환
```
 - 두 시리즈 사이 연산도 가능하다. 연산 시 float타입으로 반환된다

```python
sales_q1 + sales_q2
    --> Brazil, Japan의 경우 NaN 반환
```
  - 두 시리즈에 공통으로 존재하지 않는 인덱스에 대해서는 NaN값을 반환
  - NaN값
  - 
```python
sales_q1.add(sales_q1, fill_value=0)
--> Brazil, Japan의 경우 각각 80, 100 반환
# fill_value: 결측치 대신 대입할 값 
```

## DataFrame
### 1. DataFrame란: 
   - Formal Definition: A group of Pandas Series objects that share the same index 
   - 컬럼, 로우가 있는 판다스의 table
   - ![DataFrame](https://hossainlab.github.io/pandas/_images/pandas.png)

### 2. 생성
   ```python
   np.random.seed(101)
   mydata = np.random/randint(0,101,(4,3)) # (4,3)에서 4가 행의 개수

   myindex = ['CA', 'NY', 'AZ', 'TX']
   mycolumns = ['Jan', 'Feb', 'Mar']

   df = pd.DataFrame(data=mydata, index=myindex, columns=mycolumns)
   ```
   - csv 파일 불러오기
```python
df = pd.read_csv('파일경로')
```


### 3. 컬럼
   - 단일컬럼 가져오기
     ```python
     df['컬럼명'] # tab활용하자
     ```
     - 가져온 컬럼은 series형태이다.
        type(df['컬럼명']) --> pandas.core.series.Series
   - 여러개의 컬럼 가져오기
     ```python
     mycols = ['col1', 'col2']
     df[mycols] # 컬럼의 리스트를 넣어야 한다 
     ```  
     - 가져온 컬럼은 DataFrame 형태이다. 
   - 컬럼 추가하기
     ```python
     df['추가할컬럼'] = 시리즈 형태의 데이터 대입
     ```
   - 컬럼 수정하기
     ```python
     df['수정할컬럼명'] = 시리즈 데이터 대입
     ``` 
   - 컬럼 제거하기
     ```python
     df.drop(
        labels = 컬럼명, 행명 
        axis = 0:행 제거 1: 컬럼 제거 # 0이 디폴트
        inplace = True: 바로 적용 False: 바로 적용하지 않음
     )
     ``` 
     - drop메소드는 바로 df에 적용되지 않는다. 
       - inplace=True 를 주거나 
       - df = df.drop() 시에 적용됨. 이 방법이 이슈가 적다
   - 컬럼 위치 바꾸기 
     - df.reindex(원하는 컬럼 순서 리스트, axis=1)
     - df[원하는 컬럼 순서 리스트]
   - 컬럼 이름 변경하기
     - 전체 컬럼명 변경시
       - `df.columns = ['변경할이름1', '2', ...]`
     - 지정하여 변경 시 
       - `df.rename(columns={'변경전이름':'변경후이름'}, inplace=)`

### 4. 로우
  - 인덱스
    - 데이터프레임을 읽어올 때 인덱스를 따로 지정해주지 않으면 자동으로 rangeindex가 들어간다
    - 인덱스를 다른 컬럼으로 변경하기 
        ```python
        df = df.set_index('컬럼명')
        ``` 
    - 인덱스 리셋하기 : 기존 인덱스는 컬럼으로
        ```python
        df = df.reset_index()
    - 인덱스 이름 변경하기
       - 전체 인덱스명 변경시
         - `df.index = ['변경할이름1', '2', ...]`
       - 지정하여 변경 시 
         - `df.rename(index={'변경전이름':'변경후이름'}, inplace=)`
    - 여러 행 가져오기 
        ``` 
  - 단일행 가져오기
    ```python
        df.iloc[0] # numeric index 사용
        df.loc[''] # name index 사용
    ``` 
    ```python
    df.iloc[x:y] # integer index based
    df.loc[['index1', 'index1'..]] # string labeled index based
    ``` 
  - 행 삭제하기
    ```python
    df.drop(
        인덱스명 
        axis = 0
        )
    ``` 
    - 마찬가지로 바로 적용되지 않으므로, inplace=True 혹은 다시 변수에 대입을 해줘야한다.
    - integer based index활용하려면 df.iloc[x:y]로 슬라이싱을 해줄 수 있다.
  - 행 추가하기
    ```python
    df.append(시리즈데이터)
    ``` 
  - 행 위치 바꾸기
    - df.reindex(원하는 인덱스 순서 리스트)
    - swap하기
      - temp = df.loc[2].copy()
      - df.loc[2] = df.loc[3]
      - df.loc[3] = temp
  - 중복 행 제거
    - `df.drop_duplicates()`


## Conditional Filtering
- 컬럼의 조건에 따라 행을 가져올 수 있다 
- column = features
- row = instances of data
- 단일 조건으로 필터링하기
  ```python
  df[df['column'] <,==,...(비교연산자들 사용해 원하는 조건 주기)]
  ``` 
- 여러 조건으로 필터링하기
  ```python
  # AND & 
  df[(df[''] 조건1) & (df[''] 조건2)]
  # OR | 
  df[(df[''] 조건1) | (df[''] 조건2)]
  ``` 
  - isin 조건 활용하기
    - df['컬럼명'].isin(['옵션1', '옵션2, ...])


## 유용한 메소드 
### 1. .apply()
- 시리즈에 커스텀된 함수를 적용할 수 있게 해준다.
  ```python
  df['column'].apply(커스텀함수명)
  ```
- 커스텀함수에는 lambda를 넣을 수도 있다.
- 여러 개의 컬럼에 적용할 때
  - apply함수 사용하기
  ```python
  df[
    ['column1', 'column2', ...]
    ].apply(
        lambda df: function(
            df['column1'], df['column2'], ...
            ), ,axis=1)
  ```
  - np.vectorize 사용하기
    ```python
    np.vectorize(function)(df['column1'],df['tip'])
    ``` 
    - makes the function numpy aware (now the function is aware that it's taking in numpy array)

### 2. 정보확인
- 기본 정보 확인
  |메소드|역할| 
  |---|---|
  |`df.info()`| 데이터프레임에 대한 정보 반환 (null값, 데이터타입, 로우와 컬럼수 등 )|
  |`df.columns` | 컬럼값을 반환|
  |`df.index` | 인덱스값을 반환|
  | `df.index.names` | 인덱스 이름을 반환 |
  |`df.head()` | 첫 5개의 로우만 반환|
  |`df.tail()` | 마지막 5개의 로우만 반환 |
  |`df.sort_values('column', ascending=True/False)` | 해당 컬럼을 기준으로 정렬|
  |`df.duplicated()` | 같은 컬럼에 같은 값이 있다면true반환 (오리지널에는 false, 겹치는 값부터 true 반환)
  | `df.drop_duplicates()`| 중복되는 값 삭제|
- 통계정보 확인

  |메소드|역할| 
  |---|---|
  |`df.describe()` | numeric 컬럼에 대해 통계적 정보 제공 mean, count, std, min, max, 25%, 50%, 75% 하나의 컬럼 대신 여러개의 컬럼 리스트 대입 시 첫 컬럼으로 정렬 후 같은 값일 경우 두번째 컬럼으로 정렬한다.|
  |`df['column'].max() / min()` | 해당 컬럼의 최대/최솟값 반환|
    - `df['column].idxmax() / idxmin()`: 최대/최솟값의 인덱스 반환
  |`df.corr()` | 컬럼들끼리의 상관관계 반환


- 기타
 - `df['column'].value_counts()` : 해당 컬럼에서 각 값의 개수가 몇개인지 반환
 - `df['column'].unique()` : 해당 컬럼에서 중복 없이 값을 반환
 - `df['column'].nunique` : 해당 컬럼에서 중복 없이 값이 몇가지가 있는지 반환
   - len(df['column'].unique) 와 동일
 - `df['column'].between(x, y, inclusive=True/False)` : 컬럼값 이  x 와 y 사이에 있는지 boolean으로 반환 : 조건인덱싱으로 사용 가능! 
 - `df.nlargest(x, 'column')` : 해당 컬럼에서 값이 가장 큰 순서부터 x개의 행을 반환 
   - nsmallest도 있음

### 3. 값 대체하기
- replace함수 사용
```python
df['column'].repllace(대체할값, 대체될값)
df['column'].repllace([대체할1, 대체할2], [대체될값1, 대체될값2])
# 대체할, 대체될 값에 각각 리스트로 여러 개를 대입할 수 있다.
```
- map 사용
```python
mymap = {'대채할1':'대체될값1', '대체할2':'대체될값2'}
df['column'].map(mymap)
```

### 4. 샘플링
- df.sample(5) : 5개의 랜덤 행 반환 
  - df.sample(frac=0.1) : 내 데이터프레임 중 10%의 샘플 반환


### 5. 옵션
- 옵션 설정
  - 생략되지 않게 설정
    - 컬럼 생략되지 않게 (행은 columns대신 rows)
    `pd.options.display.max_columns = None` 
    `pd.set_option('display.max_columns', 5)` : 숫자 넣어서 제한 가능
  - 소수점 2자리까지만 표시
   `pd.options.display.float_format = '{:.2f}'.format`
  - 정규식 표현
   `pd.reset_option('^display.', silent=True)`
  -  
- 옵션 리셋
  - pd.reset_option('all')
---


  - `df.transpose()`: 컬럼과 로우를 바꿔 반환
  - np.round(data, num) : num-몇번째 소수점까지 반환할 것인지 