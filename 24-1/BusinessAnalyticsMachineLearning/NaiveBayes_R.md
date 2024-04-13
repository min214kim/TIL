# Naive Bayes 이용한 실습

## 비행기가 연착될까 안될까?

- 15분 넘게 늦어지면 delayed (=1)
- Washington DC → NewYork으로 가는 모든 2004년 1월의 비행기표
- 2201개의 비행편, delayed된건 19.5%
    
    ![Screenshot 2024-04-11 at 1.47.31 PM.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/7bd8222d-d892-4000-b428-6e3a0d4550f3/b5cb8917-9e43-4dd8-b4bd-5aba2f3e233e/Screenshot_2024-04-11_at_1.47.31_PM.png)
    
- R코드
    
    ```r
    # delays.df에 데이터 넣기 
    
    # package for naive bayes
    install.packages("e1071")
    library(e1071) 
    
    str(delays.df)# CRS_DEP_TIME, CARRIER은 int. 범주형이 아닌 것들은 범주형(factor)로 변환
    
    delays.df$DAY_WEEK <- factor(delays.df$DAY_WEEK)
    delays.df$DEST <- factor(delays.df$DEST)
    delays.df$CARRIER <- factor(delays.df$CARRIER)
    delays.df$Flight.Status <- factor(delays.df$Flight.Status)
    
    levels(delays.df$DAY_WEEK) # 범주 확인 가능 (이 데이터에서는 1~7)
    
    # create hourly bin for CRS_DEP_TIME
    # ex. 1745 -> 18, 415 -> 4
    
    # this won't work
    delays.df$CRS_DEP_TIME <- factor(round(delays.df$CRS_DEP_TIME/100))
    # this would work
    delays.df$CRS_DEP_TIME <- factor(round((delays.df$CRS_DEP_TIME+20)/100))
    
    ```
    

### 유용한 패키지 소개

- lubridate 패키지
    - mdy() : mm-dd-yy 형태를 yy-mm-dd의 date type으로 변환
        - ymd(), dmy()도 있음
        - 형태가 달라도 잘 알아들음
    - year(), month(), day() : 연, 월, 일을 따로 뽑아준다
