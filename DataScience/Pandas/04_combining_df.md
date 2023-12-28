# Combining DataFrames

## 1. Concatenation
- 단순히 두 개의 데이터프레임을 붙이는 것 
- 인덱스 혹은 컬럼 둘 중 하나가 같다는 것을 가정으로 한다.
  >`pd.concat([df1, df2, ...], axis=0/1)`
  - axis=0 : 행을 합친다 (컬럼이 같아야 함)
  - axis=1 : 컬럼을 합친다 (행이 같아야 함)
  - 다시 변수에 대입을 해줘야 저장된다 
- 만약 컬럼이 다른데 행을 합치고 싶다면?
  - df2.columns = df1.columns를 사용해서 컬럼 이름을 같게 만든다

## 2. Merge
> `pd.merge(df, how=, on=)`
  - on = '컬럼명' : PK! 값이 unique해야하고, 합치려는 컬럼들에 모두 존재해야한다
  - how = 'inner'/ 'outer'/ 'left'/ 'right'
  - on을 쓰지 않아도 알아서 합쳐주는 경우가 많지만, 이해를 위해 작성한다.
   
### 1. Inner Merge 
- 합치는 테이블 모두에 값이 있는 행만 반환한다 
- how = 'inner' 
- df를 대입하는 순서가 상관이 없다!

### 2. Left, Right Merge
- 순서가 중요하다 
> Left Merge
  - pd.merge(left= left_df, right= right_df, `how='left`', on='column')
  - left_df의 값들은 모두 결과에 반환되어야 한다
  - left_df의 column에는 존재하나 right_df의 column에는 값이 존재하지 않는 경우, NaN 반환 
> Right Merge
  - pd.merge(left= left_df, right= right_df, `how='right'`, on='column')
  - right_df의 값들은 모두 결과에 반환되어야 한다
  - right_df의 column에는 존재하나 left_df의 column에는 존재하지 않는 경우, NaN 반환 

### 3. Outer Merge
> pd.merge(df1, df2, `how='outer',` on='column')
  - 해당 컬럼의 모든 데이터프레임의 값을 반환한다


### 4. 기타 옵션
> pd.merge(df1, df2, `left_index=True, right_on='column`')
  - 왼쪽 테이블의 인덱스와 오른쪽 테이블의 column을 기준으로 합친다 
  - left/right_on : 왼/오른쪽애 있는 컬럼
  - left/right_index : 왼/오른쪽에 있는 인덱스 
- 다른 이름의 컬럼을 합치기
  - left_on , right_on을 따로 주면 된다
  - 이 경우 두 컬럼을 기준으로 합쳐지긴 하지만, 결과물에서 컬럼이 따로 존재하게 된다 (싫으면 drop활용)
- 합치는 컬럼 외에 다른 컬럼의 이름이 겹칠때,
  - 판다스에서 디폴트로 column_x, column_y로 지정해준다
  - `suffixes=(column1, column2)` : 디폴트 이름이 싫을 시, suffixes옵션으로 원하는 컬럼명을 입력해줄 수 있다.