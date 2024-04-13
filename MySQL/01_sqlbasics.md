# 스키마 이해하기 
## 스키마란?
> 데이터베이스의 테이블 구조 및 형식 (각 테이블에 어떤 필드가 들어가고 각 테이블간 관계가 어덯게 되는지)을 설명한 설계도를 말한다. (구조(필드), 형식(프라이머리키가뭐냐등),관계 정의)

## SQL (Structured Query Language)
> 관계형 데이터베이스 언어들에서 사용이 가능한 언어.  
### SQL의 세 가지 종류 
* 데이터 정의 언어 DDL
  * 스키마를 정의할 수 있는 기능
* 데이터 조작 언어 DML
  * **CRUD** (Create Read Update Delete) : 네 가지를 할 수 있으면 데이터 관리가 가능하다.
* 데이터 제어 언어 DCL 
  * 데이터베이스 관리와 관련이 많다. 권한 부여, 데이터 수정 검증 등의 작업을 실행할 수 있다.
  
# 데이터 타입
## 숫자형 데이터 타입
* 자료참고해서 정리 
* 이렇게 제한해서 지정하는 이유 : 저장공간을 작게 할당하기 위함
* DOUBLE : float보다 긴 소수점 지원
* 보통은 int 혹은 float를 자주 사용한다.

## 문자형 데이터 타입
* CHAR(n)
* TEXT(n): n에는 글자수를 지정할 수 있다 (byte단위)
* TINYTEXT(n): n <= 255
* 나머지는 자료

## 시간형 데이터 타입
* DATE
* TIME
* DATETIME
* TIMESTAMP
* YEAR
* 사실 이런 데이터타입 쓰면 저장공간 효율적으로 쓸 수는 있지만, 다시 변환해야하는 경우가 있기에 그냥 텍스트 형태로 지정하고 format만 맞추는 경우가 많다.

# Workbench로 MySQL 사용하기

## 기본 작동방법
* 실행 시 왼쪽 상단으 번개모양 버튼을 누른다 : 전체를 실행한다.
* 번개모양 옆 번개에 I가 있는 아이콘: 선택된 줄만 실행함.
* ctrl + enter : 커서가 있는 줄의 쿼리 실행

## mySQL로 데이터베이스 만들기
* 데이터베이스 파일 만들기 -> 테이블 만들기
## 데이터베이스 만들기 
* SHOW DATABASES ; : 기존에 있는 데이터베이스 확인한다
  * inforcation_schema, mysql, performance_schema, sys는 mysql 자체에서 사용하는 데이터베이스다.
* CREATE DATABASE [이름] ; : 데이터베이스를 생성한다.
* DROP DATABASE [이름]; : 데터베이스를 지운다
  * DROP DATABASE IF EXISTS [이름] : 해당 데이터베이스 이름이 없더라도 오류를 발생시키지 말라 



## 테이블 만들기
* USE [데이터베이스이름] : 테이블 생성 전, 어떤 데이터베이스를 사용할 것인지 지정해준다.
* CREATE TABLE [테이블명] (컬럼명 데이터형, ... PRIMARY_KEY (컬럼명));
  ```
  CREATE TABLE myproduct (
	KEY INT,
    ID STRING,
    TITLE STRING,
    ORI_PRICE INT,
    DISCOUNT_PRICE INT,
    DISCOUNT_PERCENT INT,
    DELEVERY STRING,
    PRIMARY_KEY (KEY)
  );
  ```

## 테이블 변경하기
* 컬럼 변경
  * ALTER TABLE 테이블명 ADD COLUMN 컬럼명 데이텉타입 옵션 : 새로운 컬럼을 추가한다

  * ALTER TABLE 테이블명 MODIFY COLUMN 컬럼명 데이터타입 옵션 : 테이블 컬럼 타입을 변경한다
  * ALTER TABLE 테이블명 CHANGE COLUMN 기존컬럼명 변경할컬럼명 변경할컬럼타입 : 테이블 컬럼명을 바꾸고 타입도 변경할 수 있다. (더 많은 기능)
  * ALTER TABLE 테이블명 DROP COLUMN 컬럼명: 테이블 컬럼을 삭제한다.


# CRUD

## Create
* INSERT INTO 테이블명 VALUES(값) : 컬럼 안에 값을 넣는다. 
  * 이 때 문자열은 '' 안에 넣어줘야 한다.
  * INSERT INTO 테이블명 (컬럼명) VALUES(값) : 특정 컬럼에만 값을 넣을 수 있다.

## Read
* 

* SELECT * FROM 테이블명; : 테이블 안에 모든 값을 조회할 수 있다.
  * * : 전체 조회를 의미함
  * SELECT 컬럼명1, 컬럼명2... FROM 테이블명; : 일부 컬럼을 조회
  * SELECT name AS new_name FROM table : 일부 컬럼을 조회 시 이름을 바꿔 뜨게할 수 있다.
  * SELECT name FROM table ORDER BY name DESC/ASC : 조회 시 결과 순서를 설정할 수 있다. 

* 조건 조회
  * SELECT name FROM table WHERE : 조건을 걸어 조회할 수 있다.
  * SELECT name FROM table WHERE 필드명 LIKE 'X%' : X로 시작하는 문자가 조회된다.
  * SELECT name FROM table WHERE 필드명 LIKE '%X%' : X가 끼여있는 문자가 조회된다.
  * SELECT name FROM table WHERE 필드명 LIKE 'X__' : X 뒤에 _의 숫자만큼 문자가 들어간 것이 조회된다. 
### 논리연산자
* AND 
* OR


## Update