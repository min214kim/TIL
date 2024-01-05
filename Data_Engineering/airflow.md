# Airflow
## Airflow 설치
1. 관련 디렉터리 생성
  - airflow 디렉터리 : airflow 기능 관련 설치 디렉터리
  - 스케줄러 프로그램 관련 디렉터리 생성 
    - airflow conf 파일에 등록해야함 (수업에서는 study디렉터리 생성)
    - study > dags 디렉터리를 스케줄러 관련 폴더로 사용
    - dag : airflow 스케줄러 프로그램을 의미
      - airflow수업은 dag프로그램을 배운다는 것과 같은 의미이다!
2. 환경변수 설정
   vim ~/.bashrc 
   - airflow home dir 관련 설정, version 관련 설정
     ```python
        export AIRFLOWHOME = ~/airflow
        export AIRFLOW_VERSION = 2.3.4 # airflow는 이 버전을 쓰겠다 
        # export : 환경변수를 만들겠다는 예약어 
     ``` 
     - 변수를 알아서 가져다 쓰게끔 자동화하도록 이렇게 변수를 설정해두는 것이다 
   - 파이썬 관련 환경변수 설정 : python이 아닌 python3 명령어로 변경 (리눅스에서는 이미 bash명령어로 python3를 사용함)
     - 터미널에 python 이라고 쳤을 때 나오는 결과 확인 
     ```python
        export PYTHON_VERSION = "$(python3 --version | cut -d " " -f 2 | cut -d "." -f 1-2) 
        # $ 가 들어가면 그 안은 bash명령어 즉 shell명령어라는 의미 
     ``` 
   - airflow 다운 경로
     ```python
        export CONSTRAINT_URL = "https://raw.githubusercontent.com/apache/airflow/constraints-$(AIRFLOW_VERSION)/constraints-$(PYTHON_VERSION).txt"
        # 해당 경로에서, 해당 airflow 버전의 파이썬 버전에 맞는 것으로 다운을 받음  
     ```  
   - echo 명령어로 환경변수 잘 설정됐는지 확인 
3. pip로 설치 진행
   - 관련 소스 : 깃헙으로 공개  : CONSTRAINT_URL에서 다운
   - airflow 버전과 파이썬 버전 명시해서 다운 후 설치
   ```python
      python install "apach-airflow==$(AIRFLOW_VERSION)" --constraint "$(CONSTRAINT_URL)" 
      # 파이썬 자체의 repository가 아닌 지정한 repository에 가서 설치하라 
   ``` 
   - 내가 난 에러 : $ pip install "apache-airflow==${AIRFLOW_VERSION}" --constraint "${CONSTRAINT_URL}"
        Defaulting to user installation because normal site-packages is not writeable
        ERROR: Could not find a version that satisfies the requirement apache-airflow==2.3.4 (from versions: 1.10.9-bin, 1.8.1, 1.8.2rc1, 1.8.2, 1.9.0, 1.10.0, 1.10.1b1, 1.10.1rc2, 1.10.1, 1.10.2b2, 1.10.2rc1, 1.10.2rc2, 1.10.2rc3, 1.10.2, 1.10.3b1, 1.10.3b2, 1.10.3rc1, 1.10.3rc2, 1.10.3, 1.10.4b2, 1.10.4rc1, 1.10.4rc2, 1.10.4rc3, 1.10.4rc4, 1.10.4rc5, 1.10.4, 1.10.5rc1, 1.10.5, 1.10.6rc1, 1.10.6rc2, 1.10.6, 1.10.7rc1, 1.10.7rc2, 1.10.7rc3, 1.10.7, 1.10.8rc1, 1.10.8, 1.10.9rc1, 1.10.9, 1.10.10rc1, 1.10.10rc2, 1.10.10rc3, 1.10.10rc4, 1.10.10rc5, 1.10.10, 1.10.11rc1, 1.10.11rc2, 1.10.11, 1.10.12rc1, 1.10.12rc2, 1.10.12rc3, 1.10.12rc4, 1.10.12, 1.10.13rc1, 1.10.13, 1.10.14rc1, 1.10.14rc2, 1.10.14rc3, 1.10.14rc4, 1.10.14, 1.10.15rc1, 1.10.15, 2.0.0b1, 2.0.0b2, 2.0.0b3, 2.0.0rc1, 2.0.0rc2, 2.0.0rc3, 2.0.0, 2.0.1rc1, 2.0.1rc2, 2.0.1, 2.0.2rc1, 2.0.2, 2.1.0rc1, 2.1.0rc2, 2.1.0, 2.1.1rc1, 2.1.1, 2.1.2rc1, 2.1.2, 2.1.3rc1, 2.1.3, 2.1.4rc1, 2.1.4rc2, 2.1.4, 2.2.0b1, 2.2.0b2, 2.2.0rc1, 2.2.0, 2.2.1rc1, 2.2.1rc2, 2.2.1, 2.2.2rc1, 2.2.2rc2, 2.2.2, 2.2.3rc1, 2.2.3rc2, 2.2.3, 2.2.4rc1, 2.2.4, 2.2.5rc1, 2.2.5rc2, 2.2.5rc3, 2.2.5)
        ERROR: No matching distribution found for apache-airflow==2.3.4
4. airflow 관련 설정 
   1. DB 초기화
      - airflow는 작업 스케줄을 위해 sqlite db를 구동하고 있음   
        - airflow사용 시 문제가 있을 때 db초기화 진행(백업필요)
      - `airflow db init`
   2. 관리자 계정 등록
      ```python
        airflow user create\
             --username admin\
             --firstname Minseo\
             --lastname Kim\
             --role Admin\
             --email 
      ``` 
   3. airflow 스케줄 프로그램 폴더 설정파일에 등록
      - 수업 시에는 study>dags폴더
      - ~/study>dags : dag 저장 폴더
      - airflow 설정파일
        - ~/airflow/airflow.cfg
      - vim airflow.cfg에 들어가 아래 내용 진행
      1. dags_folder 위치 확인 후 변경
         - dags_folder = /home/lab21/study/dags  
      2. example dags Flase로 변경  
         - load_examples = False 
5. airflow 실행
   1. webserver : 관리툴(독립터미널 사용)
   - airflow webserver --port 8082
   - webserver가 잘 안되면 webserver_config.py 파일을 다른 곳에서 복사해줌 ?? 
   1. 스케줄러 실행 (독립터미널 사용)
   - airflow scheduler  
6. 설정 변경 등 재작업 후 
   - airflow db reset
   - airflow db init
   - airflow실행 후 로그인 -> 오른쪽 위 시간대 KST로 변경  

## DAG (Directed Acyclic Graph)
> airflow에서 실행할 작업들을 순서에 맞게 구성한 워크플로우 
- DAG를 구성하는 각 작업들을 task라고 함 
- 파이썬 코드로 정의 
  - $AIRFLOW_HOME/dags 폴더에 위치
### 1) 1분에 한번씩 hello world를 출력하게 하는 dag(스케줄 프로그램)
- 간단한 bash 명령의 프로그램이라 dag 프로그램에 실행할 명령 같이 코딩 
#### 기본 import 구문
# hello_dag.py : airflow_cfg.py 파일에 등록해놓은 디렉터리에 저장 
- 수업시간의 경우 study/dag 폴더였음 
```python
from datetime import timedelta # 작업 주기 설정을 위해 import 
from datetime import datetime # 전체 작업 자동화 시작 시간 설정

from airflow import DAG # DAG 인스턴스에서 사용하는 라이브러리

# operator 사용 위해 import 
from airflow.operators.bash_operator import BashOperator
from airflow.utils.dates import days_ago
```
1. airflow 스케줄 관련 파라미터 설정
    - 딕셔너리로 구성
    - airflow로 전달이 되어서 meta db로 사용하게 됨
    ```python   
        default_args = {
        'owrner' : 'airflow',
        'depends_on_pas' : False,
        'start_date' : datetime(2024,1,1) 
        'email' : ['메일주소'] # 관리자메일주소 - 작업실패시 봅고용
        'email_on_failure' : False,
        'email_on_retry' : False.
        'retries' : 1 # 작업 실패 시 재시도 횟수
        'retry_delay' : timedelta(minutes=5) # 재시도 기간(5분 후 재시도)
        'end_date' : datetime(2024,1,5) # 작업종류
    } 
    ```
2. 스케줄 객체 생성 : DAG 모듈 
 - **이름은 작업마다 달라야 함**
 ```python
   dag = DAG(
       'helloworld', # 스케줄 이름 (임의로 개발자가 명시, **id이므로 작업마다 이름 달라야)
       default_args = default_args, # 기본 설정 파라미터
       description = 'echo helloworld'# 스케줄에 대한 설명 
       schedule_interval=timedelta(days=1) # 하루에 한번씩 본 스케줄 작업을 실행 (작업의 간격결정)
   )
 ```  
   - schedule_interval : 복잡한 간격 지원
     - cron 구문 지원
       - 분 시간 일 월 요일    
     - timedelta 인스턴스 사용
       - 분 : timedelta(minutes=)
       - 시간 : timedelta(hour=)
1. task 생성 : 실제 실행되어야 할 작업 (dag객체에 종속)
 - **id는 task마다 달라야 함**
 - dag이 스케줄에 등록되는 전체 작업이라면, task는 작업의 단위 
 - 객체변수명 = operator 종류모듈(내용) 
   - 종류모듈 : 터미널 명령어면 BashOperator, 코드 직접실행이면 CodeOperator
   - 파이썬 프로그램일 시 BashOperator을 사용
   ```python
       t1-BashOperator(
           task_id = '임의 task_id명'
           bash_command = '실행할 터미널 명령어'
           dag = dag객체명
     )
   ```
- 코드를 스케줄러에 등록
- 관리도구 (web) 이용해서 실행 시작 

### 2) python프로그램을 실행하는 sh 명령을 task 등록

- python 프로그램 : 빈 csv 파일을 저장하는 프로그램 
- 위의 프로그램을 1분에 한번씩 실행하도록 schedule interval 설정 

1. 스케줄 파일 : study/dags 에 저장
2. python 프로그램 파일 : 저장 디렉터리 상관 없음
   - 수업에서는 study/test/make_csv.py 
   - python3 /home//lab21/study/test/make_csv.py로 실행해줌

make_csv.sh라는 shell프로그램 생성 
- shell 프로그램 : shell(터미널) 기반으로 실행되는 프로그램이다!
- sh라는걸 먼저 부르고  
  - sh /home/lab21/study/test/make_csv.sh  로 간접적으로 부를 수도 있음 : 이 안의 모든 프로그램이 실행


### corona project
- study/corona_project 안에 corona_extract.py 파일
-  " .sh파일
- study/dags 안에 project_v1_dag.py 
  - dag 객체 생성, 스케줄 관리 객체 생성, 스케줄 작업 객체 생성 

2. transform
   - study/corona_project 안에 corona_transform.py
     - pyspark 이용하는 것 
       - findspark install 해줌
       - spark session은 새로 만들어서 사용해줘야하기 때문에 관련 함수들을 만들었음 
     - 기능별로 스파크세션가져오기/데이터가져오기/Df형성하기/데이터 저장하기 함수를 만듦 
3. transform - dm,dw


4. 스케줄러 형성, 실행
   study/dags 폴더에 project_v2_dags.py
    - with as 구문 사용  
with as 구문 사용 
  airflow 실행 후 웹에서 확인하기
    그래프??

5. 수정 
- corona_extract.py 
  - 코로나 현황 데이터를 기간이 아닌 특정일에 대한 data를 추출 (코드에 이미 반영돼서 수정필요 없)
- corona_transform_dw.py
  - 특정일에 대한 데이터로 추출 (이미 코드 반영 완료 수정 필요 없)
- corona_transform_dm.py
  - 4개 함수 각각 최신 코로나 현황 데이터를 활용해 데이터 생성 후 insert 진행 
  - db에서 특정 조건에 맞는 레코드만 가져오는 방법 
    - test/jdbc_test.py
    - crorna_transform_dm.py파일에 find_query함수 작성 , patients를 불러올 떄  find_data대신 find_query로 변경 