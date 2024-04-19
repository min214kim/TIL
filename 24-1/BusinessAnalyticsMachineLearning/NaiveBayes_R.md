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

### 파티셔닝

- 훈련데이터 / validation data로 나누기!
- 모든 attribute 쓰지 않고 predict로 5가지만 씀 → 전처리 필요 (필요 데이터셋만 뽑고 데이타 partitioning)
    
    ```python
    selected.var <- c("DAY_WEEK", "CRS_DEP_TIIME", "ORIGIN") # 이런식으로 이름을적어도 되고,
    selected.var <- c(1,2,3) # 이렇게 컬럼숫자를 넣어줘도 된다 
    
    dim(delays.df)[1] # num of row
    ```
    
- 파티셔닝
    
    ```r
    set.seed(2) 
    
    train.index <- sample(c(1:dim(delays.df)[1]), dim(delays.df)[1]*0.6)
    
    train.df <- delays.df[train.index, selected.var]
    valid.df <- delays.df[-train.index, selected.var]
    ```
    

### Run Naive Bayes

```r
naiveBayes(output변수 ~ ., data = 훈련데이터셋) 

delays.nb <- naiveBayes(Flight.Status ~ ., data = train.df) 
delays.nb
```

- ~ : =과 같은 것
- Flight.Status ~ . : 나머지 attribute를 predictor으로 사용해달라
- .을 안찍고 predictor attribute들을 +로 연결해 작성해도 된다
- naiveBayes 함수 없이 같은 결과 도출하기
    
    ```r
    table(train.df$Flight.Status, train.df$DEST)
    prop.table(table(train.df$Flight.Status, train.df$DEST), margin=1) 
    # margin = 1 : 각각의 row의 합이 1이 됨
    # margin = 2 : 각 col의 합이 1
    ```
    
- predicting probabilities
    
    ```r
    pred.prob <- predict(delays.nb, newdata = valid.df, type = "raw")
    
    class(pred.prob) # matrix 형태 
    ```
    
    - type = ‘raw’ : 확률을 먼저 계산
    - type = ‘class’ 가 default : 데이터가 어떤 class에 속하는지 보여준다?
    - 잘 맞췄는지 확인
    
    ```r
    df <- data.frame(actual = valid.df$FLIGHT.STATUS,
    							 pridected = pred.class, pred.prob) 
    ```
    

- val 데이터에 특정 record가 있으면
    
    ```r
    df[valid.df$CARRIER == "DL" & valid.df$DAY_WEEK == 7 & valid.df$CRS_DEP_TIME == 10 &
    		valid.df$DEST == "LGA" & valid.df$ORIGIN = "DCA", ]
    
    new.record1.df <- data.frame()
    ```
    
    - DF indexing
        
        ```r
        df11 <- data.frame(x = rep(1,10), y = rep(1:2, 5), z = letters[1:10])
        
        # 특정 row뽑기
        df11[c(1,3,5,7,9), ] # 직접 인덱스 번호 주기
        df11[df11$x==1 & y==1, ] # x가 1을 만족하고 y가 1을 만족하는 조건 주기 : 위와 같이 1,3,5,7,9 idx row가 뽑힌다
        
        # 다른 DF에서도 df11를 사용해 인덱싱 가능
        df12 <- data.frame(a = rep(1,10), b = rep(1:2, 5), c = letters[1:10])
        df12[df11$x==1 $ df11$y==1, ] # df12의 1,3,5,7,9 idx row가 뽑힘
        ```
        
    

### ROC and AUC NB모델의 정확도

```r
install.packages("pROC")
library(pROC) 

# roc() : need 2 vectors 
# ifelse(valid.df$Flight.Status == "delayed", 1, 0)
# pred.prob[ ,1] : 첫 컬럼인 delayed의 확률

ROC_flight <- roc((ifelse(valid.df$Flight.Status == "delayed", 1, 0)), pred.prob[ ,1])
plot(ROC_flight, col = "blue") # 색 설정
# ROC Curve를 그려준다! 

# AUC 확인 
auc(ROC_flight) 
```

- gain(=lift) chart

```r
install.packages("gains")

library(gian)
gain <- gains(ifelse(valid.df$Flight.Status == "delayed", 1, 0), pred.prob[ ,1], groups = 10)

```

- confusion matrix
    
    ```r
    library(caret)
    pred.class <- predict(delays.nb, newdata = train.df)
    # overfitting issue가 있는지 확인 : train과 test에 적용했을때 차이가 있는지 확인
    
    confusionMatrix(pred.class, train.df$Flight.Status) 
    
    pred.class <- predict(delays.nb, train.df$Flight.Status)
    confusionMatrix(pred.class, train.df$Flight.Status) 
    
    # 차이를 보고 overfitting 여부를 판단 
    ```
    
- accuracy 희생하고 sensitivity올리기
  ```r
  pred.probbth <- factor(ifelse(pred.prob[, 1] >= 0.3, "delayed", "ontime"))
  ``` 