# Groupby 
- 카테고리별 데이터 접근, 집계가 가능하게 해준다 
- 범주형 컬럼 (연속X) 에 적용한다
  
##
- df.groupby('column') : 해당 컬럼의 unique 값을 카테고리를 만든다.
  - groupby와 한 후 아무것도 하지 않은 것은 lazy groupby다 : 실행 시 딱히 뭘 반환하지 않음, 여기에 뭔가 더 해줘야 df나 시리즈를 반환한다.
  - df.groupby('column').집계함수
    - .mean()
    - .count()
    - .describe()
- 여러 개의 컬럼으로 그룹핑하기 
  - df.groupby(['column1', 'column2'])
  - multi-level index를 반환한다 
- 그룹핑을 하기 전 어떤 결과를 갖고싶은지 잘 아는 것이 중요하다! 그룹핑을 한 후에 뭔가를 조정하기는 어렵기 때문에, 필터링을 해주고 그룹핑을 해주는 편이 쉽다.

## 멀티레벨 인덱스
- 인덱스 가져오기
  - `df.index` --> 튜플 형식의 인덱스가 반환된다
  - `df.index.levels`
- 멀티레벨 인덱스에서 인덱싱
  - `df.loc[[indexlv1, indexlv1, ...]`] : 가장 바깥 인덱스에 대해 적용된다
  - `df.loc[(indexlv1, indexlv2, ...)]` : 튜플을 대입해야 안쪽 인덱스 접근이 가능하다. 
- .xs 메소드 (cross-section)
- `df.xs(key=, level=)`
  - key =  가장 바깥쪽 레벨 인덱스
  - level = 그외 레벨의 인덱스
  - key값은 하나만 들어갈 수 있다. -> 여러개의 인덱스 반환 시에는 loc활용 
  - 안쪽 인덱스를 기준으로 값을 반환하고 싶을 때 사용한다. 
    - (A,a) (A,b), (A,c), (B,a), (B,b), (B,c), (C,a), (C,b), (C,c) 와 같은 인덱스가 있을 때, .loc 메소드로는 A, B, C 모두에 대한 a의 값으 반환하기는 함들다. 이때 .xs메소드를 사용한다.
- outter level과 inner level인덱스 바꾸기
- df.swaplevel() 
- 정렬하기
  - df.sort_index(level=, ascending=True/False) 
    - level = 정렬하고싶은 인덱스 
    - 안쪽 인덱스로 정렬 시 그룹핑이 깨질 수 있다.


## agg 함수
- df.agg() : ()안에 mean, sum, count, std 등의 집계함수를 넣어서 원하는 값을 반환할 수 있다
  - df.agg(['std', 'mean']) : 모든 컬럼에 대해 std와 mean 반환
  - df.agg({column1 : [집계함수1,집계함수2], column2 : 집계함수, ...}) : 각 컬럼별로 원하는 집계를 반환할 수 있다 
    - 이때  null이 반환될 수 있다.