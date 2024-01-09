# 카프카
## 1. 설치
- 필요 소스 다운 
  - wget https://dlcdn.apache.org/kafka/3.4.1/kafka_2.13-3.4.1.tgz
- 압축 해제, 바로가기 생성 
  - 압축해제 : tar -xzf kafka_2.13-3.4.1.tgz
  - 바로가기 : ln -s kafak_2.13-3.4.5 kafka (tgz있는거 말고!)
- 환경설정 
  - vim ~/.bashrc
  - 카프카관리 ZOOKEEPER 프로그램의 home생성
  - zookeeper
    ```python  
    ZOOKEEPER_HOME = /home/lab21/kafka
    PATH = $PATH:$ZOOKEEPER_HOME/bin
    export PATH
    ```
  - kafka
  - 카프카 홈 생성 
  - 

## 2. 개요 