# Data Pipeline
## 1. Flow
1. Data Warehouse
   - DataLake(하드디스크,웹) --> HDFS(하둡, json형태의 row데이터) 
   -> Trans 처리 -->  mysql로 옮기기 (table 형태 high level)

2. Data Mart
   - mysql사용, 테이블 형태로 저장 
   - DW --> Trans 처리 -> DM

3. Trans 처리
   - hdfs에서 mysql로 옮길 때 : 단순한 처리
     - ex. ex.코로나 환자 발생을 날짜별로 insert
   - Data warehouse에서 Data Mart로 옮길 때 : 데이터 내용을 바꿈. 가공처리해서 밀어넣는다
     - ex.요일별 환자발생 insert, 백신 접종률과 환자발생의 관계 등
   - Trans처리 시 **spark** 기술 제공 : RDD, DF, SQL 등의 기술 활용 (Json->Tabel, Mysql -> Mysql)

4. 데이터 파이프라인
   - 하둡과 mysql은 저장공간, 이런 저장공간 사이 데이터 옮겨지는게 데이터 파이프라인
   - 이 때 spark 코드를 사용한다 
   - Extract - Transform - Load 까지 완료되면 데이터 파이프라인이 동작한 것 

## 2. Extract 
