

하둡의  hdfs(저장장치) 핸들링 명령어 
    - 모든 명령어 : hdfs로 시작 그 뒤에 명령내릴 객체 쓰고 그 뒤에 명령어
    - hdfs namenode -format 
    - 하둡 명령어 -format을 namenode에게 전달하겠다 

하둡 저장장치 자체에 명령은 hdfs dfs
하둡 datanode에 디렉터리 생성 : 
    - hdfs dfs -mkdir 디렉터리명 

  - 하둡 datanode의 현재 디렉터리 상황 확인
    - - hdfs dfs -ls /
- 하둡 datanode에 데이터 이동
  - hdfs dfs -put 원본파일 이동디렉토리



## 하둡 
분산 저장 처리를 할 수 있는 기술

## 스파크
분산 저장 처리를 할 수 있게 하는 프레임워크 

