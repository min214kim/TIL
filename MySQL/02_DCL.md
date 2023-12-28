# DCL (Data Control Language) 이해 및 실습
- mysql 사용자를 추가하고 수정함 

- 보통 터미널 환경에서 더 많이 사용 
- mysql -u root -p 후 패스워드 입력하면 터미널에서 사용 가능

1. mysql 사용자 확인, 추가, 비밀번호 변경, 삭제 
- use mysql;
  - mysql안에는 mysql이름의 데이터베이스 파일이 있음. 여기에 접근하는 것 
  - show tables -> select * from user
    - user에 root, mysql이 사용중인 유저등이 보임 (root는 내가 사용하는 유저)
    - 사용자 정보를 테이블로 관리
  - 유저 추가하기
    - 로컬에서만 접속 가능한 유저아이디: create user 'userid'@localhost identified by '비번';
    - 모든 호스트에서 접속 가능한 유저아이디 : create user 'userid'@'%' identified by '비번';
      - 이후 mysql -u userid -p 후 비번 입력시 접속 가능 
  - exit누르면 나올 수 있음 
  - 사용자 비밀번호 변경
    - SET PASSWORD FOR 'userid'@'%' = '신규비번'
  - 사용자 삭제
    - drop user 'userid'@'%'


2. mysql 접속 혀옹 관련 설정 
- 어떤 데베는 모든 권한 부여하고, 어떤 데베는 조회만 부여한다든지,, 
- 터미널 접속 (mysql -u root -p)
- 현재 부여한 권한 확인 
  - SHOW GRANTS for id;
- 로컬에서만 접속 허용
  - GRANT ALL ON DATABASE.TABLE to '계정명'@localhost;
    - DATABASE.TABLE 을 *.*로 하면 모든걸 허용한다는 뜻 
- 특정 권한만 허용
  - GRANT [SELECT, UPDATE등 허용하려는 권한] ON DATABASE>TABLE to '계정명'@localhost;