
1. 하둡 설정파일 확인 
  - cd $HADOOP_CONF_DIR 로 이동, ls로 확인 
  1. vim core-site.xml 확인 
    - localhost:9000 부분이 꼭 있어야함!
    - 이 아래코드는 namenode 실행 시 오류에 대비한 코드임 
      - 이 파일에서 9000번 포트가 사용중이라 포트사용불가 에러 발생 시, 포트번호 사용하지 않는거로 변경 or 포트종료 (vscode의 터미널 옆 port 탭 이용)
    - 밖으로 나가는법 : esc+:+q
  2. vim hdfs-site.xml 확인
    - dfs.replication : 데이터 노드 몇개 쓸것인지
      - 도커 여러개 돌리면 컴퓨터 다운될 수 있어 1로 해둠
    - 아래 namenode와 datanode 디렉토리의 경로 및 최종폴더명이 정확한지 확인

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

