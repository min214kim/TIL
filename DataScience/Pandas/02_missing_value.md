# 결측치 
- 실제 데이터에는 결착값이 많다
- 머신러닝에서 결측치가 있으면 오류가 나는 경우가 많아 처리를 해줘야한다
- pd.NaT : means it's missint timestamp value
- 결측치인지 확인하기 위해서는 `==` 가 아닌 `is` 연산을 사용해야 한다.
  - 결측치의 실제 값이 무엇인지 알 수 없기 때문에, np.nan == np.nan -> Flase!

## 결측치 관련 메소드
- `df.isnull()`, `df.isna()` : null인지 아닌지 boolean값 반환 
- `df.notnull()` : 위와 반대 
- `df.isna().any(axis=1)` : 각 행에 결측치가 있으면 boolean값 반환 (조건검색에서 사용)
- `df[df.isna().any(axis=1)].index` : 결측치의 인덱스 반환

## 결측치 처리의 옵션
1. 가지고 있기
   - 장점: 처리가 쉽다, 실제 데이터를 변경하지 않는다
   - 단점: 여러 메소드는 null을 지원하지 않는다
2. 제거하기
   - 장점: 비교적 처리가 쉽다, 룰 적용이 쉽다
   - 단점: 유용한 정보를 제거하게 될 수도 있다, 컬럼 전체를 제거할 경우 미래 데이터를 제한하게될 수 있다 (limits future train model)
   - 언제 제거하는게 좋은가 
     - 해당 컬럼/행 안의 거의 모든 정보가 결측치일 때 
     - 제거 시 제거되는 데이터가 전체 데이터에서 얼마나 큰 비중을 차지하는지 고려한다
3. 대체하기
   - 장점: 모델 학습 시 많은 데이터를 남겨둘 수 있음
   - 단점: 어려움, 잘못된 가정으로 값을 대체할 가능성이 있음
   - 언제 대체하는게 좋은가?
     - 그냥 채우기 위해 0값을 NaN으로 넣은 경우
     - 값의 예측이 가능한 경우

### 1. 가지고 있기 

### 2. 제거하기
- help(drop.na())로 정보 확인하기
- `df.dropna()`
  - `df.dropna(thresh=n)` :  null을 포함하는 행을 제거하되, n개의 not-null이 포함된 행은 제외하고 제거
  - `df.dropna(axis=1)` : 컬럼을 기준으로 null을 포함하는 컬럼을 제거
  - `df.dropna(subset=['column'])` : 해당 컬럼값이 null인 행들만 제거

### 3. 대체하기
- hlep(df.fillna)로 정보 확인하기
- `df.fillna(값)` : null값을 ()안의 값으로 대체
  - df['column'].fillna() : 해당 컬럼에서 null값을 ()안의 값으로 대채ㅔ
    - 변화 저장을 위해서는 변수에 다시 대입하거나 inplace 사용
    - `df['column'].fillna(df['column'].mean())` 
    - `df.fillna(df.mean())` : 평균을 구할 수 있는 것들은 평균을 구해 채움
- df.interpolate() : 해당 값을 정렬 후, 바로 위 값과 아래 값의 평균으로 채움
