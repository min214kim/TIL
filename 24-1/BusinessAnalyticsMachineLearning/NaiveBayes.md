# Naive Bayes (지도학습)

### vs KNN

- not model based, but data driven (엄격히는 모델을 만들지 않는다)
    - based on similar records in terms of predictors in the training set
- Naive : 과거 유사 데이터 사용, 확률과 베이즈 이론을 활용
- KNN : 거리 사용, compute vote of k neighbors
- 머신러닝 : 훈련데이터로 모델 만들고, 미래 데이터에 적용해 예측 및 분류함

### Data driven 

- ex) 고객이 안드로이드를 살까 아이폰을 살까 예측
    - Naive Bayes
        - categorical predictor(숫자인 경우 범주형으로 변환)
        - use bayes theorem to calculate
        - P(인드로이드 | gender=F , Age=Young)?
            
            ![Screenshot 2024-04-11 at 10.25.01 AM.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/7bd8222d-d892-4000-b428-6e3a0d4550f3/d94c6c97-8855-4c40-904a-35028385ad56/Screenshot_2024-04-11_at_10.25.01_AM.png)
            
        - 위의 그림처럼, 확률을 계산해서 분류한다
    - KNN (K-Nearest Neighbor)
        - 주로 continuous predictor에 쓰임
            
            ![Screenshot 2024-04-11 at 10.27.22 AM.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/7bd8222d-d892-4000-b428-6e3a0d4550f3/0d5fdb62-880a-4e32-ba73-b7d87174cd8b/Screenshot_2024-04-11_at_10.27.22_AM.png)
            
        - 빨간 X : 예측할 고객! → voting방법을 통해 예측한다

### Bayes Theorem

- P(Y=1 | X1,…,Xp) —> Use bayes theorem
    
    ![Screenshot 2024-04-11 at 10.35.16 AM.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/7bd8222d-d892-4000-b428-6e3a0d4550f3/e04cdb8d-2f1d-4d59-8aac-4545dfe62804/Screenshot_2024-04-11_at_10.35.16_AM.png)
    
    ![Screenshot 2024-04-11 at 10.35.27 AM.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/7bd8222d-d892-4000-b428-6e3a0d4550f3/e279b332-38d8-4e91-96bf-fcab6b1c26a6/Screenshot_2024-04-11_at_10.35.27_AM.png)
    
    ![Screenshot 2024-04-11 at 10.35.20 AM.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/7bd8222d-d892-4000-b428-6e3a0d4550f3/70fc3fdf-b332-4bff-9458-1bf1c190a520/Screenshot_2024-04-11_at_10.35.20_AM.png)
    
    ![Screenshot 2024-04-11 at 10.35.16 AM.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/7bd8222d-d892-4000-b428-6e3a0d4550f3/e46e5a34-ac91-4338-b3ad-837f43d10d69/Screenshot_2024-04-11_at_10.35.16_AM.png)
    
    ![Screenshot 2024-04-11 at 10.35.45 AM.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/7bd8222d-d892-4000-b428-6e3a0d4550f3/96defbae-a4b1-4a8b-a4e6-c642d704db38/Screenshot_2024-04-11_at_10.35.45_AM.png)
    
    ![Screenshot 2024-04-11 at 10.35.50 AM.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/7bd8222d-d892-4000-b428-6e3a0d4550f3/31461c71-e6df-4572-9fc9-42621763b7f7/Screenshot_2024-04-11_at_10.35.50_AM.png)
    

### Exact Bayes Classifier

- 위의 공식 (Exact Bayes)은 조금 문제가 있어서 실제로는 나이브 베이즈를 사용한다
- 나이브 베이즈 : assume independence of predictor variables (within each class)
    - ex) personal loan offer
        - CC: Credit Card (1:씀, 0:안씀)
            
            ![Screenshot 2024-04-11 at 10.41.07 AM.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/7bd8222d-d892-4000-b428-6e3a0d4550f3/a52b1d0c-4448-4875-9353-6a45ebf8956e/Screenshot_2024-04-11_at_10.41.07_AM.png)
            
        - given B and A를 given A and B로
            
            ![Screenshot 2024-04-11 at 10.47.51 AM.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/7bd8222d-d892-4000-b428-6e3a0d4550f3/7d492e82-1675-4173-b051-b31c58dad9cc/Screenshot_2024-04-11_at_10.47.51_AM.png)
            
- Exact Bayes를 안쓰는 이유
    - 과거에 조건을 만족시키는 데이터가 없으면 0이 되지만, 실제로 0일지는 알 수 없음 (데이터가 적은 것일 뿐)
    - 0 이 no record가 되어버리면 misunderstand 가능성 O
        
        ![Screenshot 2024-04-11 at 10.55.49 AM.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/7bd8222d-d892-4000-b428-6e3a0d4550f3/62cd01e5-2cc8-47cc-a3a3-3da167c9acca/Screenshot_2024-04-11_at_10.55.49_AM.png)
        
        - predictor이 3이상인 경우, 그 조건을 모두 만족시키는 데이터가 없을 가능성도 높다
    - 이런 경우 나이브 베이즈를 사용한다
    - 그래서 이게 왜 한계인거지 ??? 나이브는 뭐가 다르길래 ??????

### Naive Bayes

- assume independence btw X, Y
- P(X=x,Y=y | Z=z) —> P(X=x | Z=z) * P(Y=y | Z=z)
    
    ![Screenshot 2024-04-11 at 12.25.45 PM.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/7bd8222d-d892-4000-b428-6e3a0d4550f3/9bce4255-c2dc-4d1d-b00f-6042429e0261/Screenshot_2024-04-11_at_12.25.45_PM.png)
    
    ![Screenshot 2024-04-11 at 12.26.26 PM.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/7bd8222d-d892-4000-b428-6e3a0d4550f3/781f416b-f1b2-4fad-a49a-5fac9cbe4ce3/Screenshot_2024-04-11_at_12.26.26_PM.png)
    
- example
    
    ![Screenshot 2024-04-11 at 1.24.36 PM.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/7bd8222d-d892-4000-b428-6e3a0d4550f3/1ecfa0eb-8407-4bc8-a951-f42c5a440a7c/Screenshot_2024-04-11_at_1.24.36_PM.png)
    
    ![Screenshot 2024-04-11 at 1.25.58 PM.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/7bd8222d-d892-4000-b428-6e3a0d4550f3/e16e8511-a286-4088-9e95-6114e4d57e16/Screenshot_2024-04-11_at_1.25.58_PM.png)
    
    ![Screenshot 2024-04-11 at 1.26.46 PM.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/7bd8222d-d892-4000-b428-6e3a0d4550f3/bf51269f-4c33-43c3-abc8-d65fe09a72d4/Screenshot_2024-04-11_at_1.26.46_PM.png)
    

### Laplace Smoothing

- 하나의 조건 확률이 0이면 전체 값이 0이 되어버린다
- 이에 대한 해결책으로 laplace smoothing을 한다
    
    ![Screenshot 2024-04-11 at 1.33.38 PM.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/7bd8222d-d892-4000-b428-6e3a0d4550f3/54324e0d-8fca-4cc6-8534-e6dfc2b4ecee/Screenshot_2024-04-11_at_1.33.38_PM.png)
    

### 장단점

- 장점
    - simple, 계산이 효율적
    - 스팸메일 등에 활용 → 스팸인지 아닌지 알 수 있는 키워드
    - 분류 데이터 처리가 쉽다
    - 큰 데이터셋에도 적용 가능
    - pretty robust to independence assumption
- 단점
    - 데이터가 많아야 함(combination이 0이 되는 경우는 좋지 않음)
    - 연속형 변수의 경우 범주형으로 분류해야 함
    - predictors with rare categories : 0prob problem
    - 변수들 중 어떤게 중요한 변수인지는 알 수 없다