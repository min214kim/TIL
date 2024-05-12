# Sakila 데이터로 익히는 데이터 분석과 SQL 


### 일단 sakila-schema.sql 실행 후 sakila-data.sql 실행 
    - 스키마를 만드는 것!

1. LIMIT
   - 결과 중 일부의 데이터만 가져옴 
   - 데이터를 파악하는 데에 주로 사용 
   - SELECT * FROM table LIMIT 10 : 위에서부터 10개의 행만 반환 

2. COUNT
   - SELECT COUNT(*) FROM table;
     - 해당 테이블의 행의 수를 셀 수 있다.
   - SELECT COUNT(*) FROM table WHERE 조건문;
     - 특정 조건에 맞는 테이블 데이터 수 세기  

3. DISTINCT
   - SELECT DISTINCT column FROM table;
     - 특정 컬럼에 들어있는 컬럼값 종류 확인 
   - 데이터는 수치형, 범주형(남/녀같은), 시계열(시간순으로 표시) 등으로 나뉘어짐. 그 중 범주형에서 어떤 종류가 있는지 파악하는 데에 확인 

4. SUM, AVG, MAX, MIN
   - SUM(): 컬럼값의 합계
   - AVG() : 컬럼값 평균
   - MAX() : 컬럼값 최대값
   - MIN() : 컬럼값 최소값
   - select sum(column) FROM table

5. GROUP BY
   - 특정 컬럼값 기반으로 그룹핑
   - SELECT column FROM table GROUP BY column;

6. ORDER BY
   - 특정 컬럼값을 기준으로 데이터 정렬
   - ORDER BY columng DESC,ASC
     - DESC: 내림차순
     - ASC: 오름차순 


7. AS


8. SQL 조건 순서
   SELECT, FROM, JOIN, WHERE, GROUPBY HAVING, ORDERBY, LIMIT



# 중급 sql 익히기 

1. 외래키 (Foreign Key)
    - 여러 데이터를 넣을 때 외래키로 연결한다.
    - 테이블 생성 시 지정
      - CREATE TABLE table(
      - FOREIGN KEY (column) REFERENCES 참고할table(column)
      - )
    - 해당 컬럼값이 없으면 에러가 난다 (데이터의 무결성)
      - 데이터 무ㅕㄹ성 : 두 테이블 간 관계에 있어 데이터의 정확성을 보장하는 제약 조건 
    - 현업에서는 꼭 필요한 경우에만 사용한다 (비즈니스 로직 처리가 어려워지기 때문)
2. GROUPBY 와 HAVING
   - having은 groupby와 함께 사용한다.
   - 집계함수로 조건비교를 할 때 사용한다.
   - 집계함수는 where절에서 groupby와 함께 쓰지 못함 --> having 을 사용한다 

3. JOIN 
   - 현업에서 많이 쓰임! 여러 테이블에서 필요로 하는 정보를 조합해서 추출 
   - 데이터 분석, 추출, 처리 분야에서는 join을 많이 쓰나 개발적인 측면에서는 지양함
     - 프론트엔드에서 백엔드 DB정보를 가져올 때에 시간이 오래걸리기 때문에 잘 사용하지 않음 
  1. INNER JOIN(디폴트)
    - SELECT * FROM table1 alias INNER JOIN table2 ON table1.column = table2.column
      - default이기 때문에 innerjoin 대신 join을 써도 된다.
    - 두 테이블에서 필드값이 같은 것들을 기준으로 붙임 
    - 같은게 없을 경우 합쳐지지 않음! 매칭되는게 있는 경우에만 붙여진다.
  2. OUTER JOIN
    - 개발쪽에서는 많이 쓰이진 않으나 데이터분석 사이언스 쪽에서는 많이 쓰임! 
    - LEFT OUTER JOIN
      - SELECT * FROM table1 LEFT OUTER JOIN table2 ON table1.column = table2.column
      - table1은 전부 가져온 후 table2를 붙인다. 이때 table1의 컬럼값에 매치되는 table2의 컬럼값이 없는 경우 null값이 생긴다.
    - RIGHT OUTER JOIN
      - SELECT * FROM table1 RIGHT OUTER JOIN table2 ON table1.column = table2.column
      - table2는 전부 가져온 후 table1을 붙인다. 이때 table2의 컬럼값에 매치되는 table1의 컬럼값이 없는 경우 결측치로 채운다.
    - INNER JOIN과는 달리 테이블 순서에 따라 결과가 달라질 수 있다.

4. Sub Query 서브쿼리 
   - SQL문 안에 포함되어 있는 SQL문
   - 성능 이슈로 자주 사용하지는 않음 
   - table과 table 검색시, 테이블 중 필요한 부분만 가져올 때 사용한다.
     - join으로 대체 가능하다.
   - () 안에서 사용 가능 : select, from, where 등에 사용 가능 
   - WHERE에서 서브쿼리 사용하기 
     - ㅇㅇ
   - 비교로 사용하기 
     - 
   - 조인처럼 테이블 간 연결고리가 있어야 이를 기반으로 서브쿼리 사용이 가능하다.

5. IN 문법
   - 여러 개의 or 대신 사용이 가능 
   - X=a or X=b or X=c == X in (a, b, c)

6. CASE WHEN THEN
   - CASE WHEN [조건] THEN '반환값' WHEN [조건] THEN '반환값' ELSE '조건에 해당하지 않을 때 반환값' END
     - AS ~ 로 Alias 가능

7. NULL 처리하기 
   - WHERE 절 이용 
     - SELECT * FROM table WHERE column IS NOT NULL
   - COALESCE 사용 (0으로 대체)
     - SELECT col1, COALESCE(col2, 0) as allias FROM table