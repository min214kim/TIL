# Pivot Tables
## 1. .Pivot() method
### 1. 주의사항  
  - 모든 df가 pivot이 가능하지 않으므로, pivot전에는 잘 생각해야 함 
  - groupby로 해결할 수 있는 경우도 많기 때문에, 어떤 물음에 답할 것인지, 결과 df가 어떻게 생겨야 하는지, pivot이 꼭 필요한지 생각한다. 
### 2. pivot()메소드
  ```python
  pd.pivot(data=데이터명,index='인덱스가될 컬럼명',
        columns='컬럼이될 컬럼명',values='값이될 컬럼명')
  ```
    - index : 인덱스가 될 컬럼명 (리스트가 들어가면 다중 인덱스가 된다)
    - columns : pivot 후 컬럼이 될 df의 컬럼명 (리스트가 들어가면 다중 컬럼)
    - values : 값으로 들어갈 컬럼명 

## 2. Pivot_table() method
  -  pivot()메소드 + aggregation 함수
  ```python
  pd.pivot_table(df, index='컬럼명',  column='컬럼명', aggfunc='함수명',values='컬럼명', fill_value = 0/1, margins=Ture/False)
  ```
    - index : 인덱스가 될 df의 컬럼명
    - column : 컬럼이 될 df의 컬럼명 (optional임)
    - aggrunc : 집계함수 
      - [np.sum, np.mean] 처럼 리스트로 여러개 들어갈 수 도 있음 
    - values : pivot_table()을 이용해 어떤 컬럼을 집계함수 적용하여 반환하고 싶은지
      - ['column1', 'column2' ...] 와 같이 리스트가 들어갈 수도 있음 
    - margins : Total을 반환해줌 (디폴트 False)
    - fill_value = x : nan대신 x를 반환해줌