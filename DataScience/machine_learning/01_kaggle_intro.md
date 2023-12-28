# Intro to Machine Learning - Kaggle

## 1. How Models Work

## 2. Basic Data Exploration

## 3. ML Model

## 4. Model Validation 
- MAE (Mean Absolute Error)
  - from sklearn.metrics import mean_absolute_error
  - prediction = dfmodel.predict(X)
  - mean_absolute_error(y, prediction)
  - On average, our predictions are off by about X. 라고 표현 가능
- Issues
  - train data에서 패턴을 찾았기 때문에, train data에 대한 prediction은 정확할 것 
  - 하지만, 일반 데이터에서는 관련이 없는 패턴이나 train data에서만 연관성이 있는 패턴의 경우 일반적으로 적용하긴 힘들고, 이것은 일반 데이터에 해당 모델을 적용 시 오차를 크게 만들 수 있음 
  - 그렇기 때문에 validation data(모델을 만들 때 사용하지 않은 데이터)로 performance를 측정한다.
    - scikit-learn의 train_test_split를 사용해, features와 target 모두에 대해 데이터를 train/test(validation) data로 나눈다
    - from sklearn.model_selection import train_test_split
    - train_X, val_X, train_y, val_y = train_test_split(X, y, random_state=n)
  - model의 성능이 좋지 않은 경우, 더 나은 feature을 찾거나 다른 모델을 찾는 식으로 개선할 수 있다.

## 5. Underfitting and Overfitting
- decision tree's depth
  - 예측 전 몇 개의 split를 만드는지와 관련 
  - split가 여러개일 수록 2의제곱승으로 leaf가 많아짐
- Overfitting
  - Capturing spurious patterns that won't recur in the future, leading to less accurate predictions 
  - 학습 데이터에는 모델이 잘 맞지만, 평가 데이터 혹은 다른 새 데이터에는 정확도가 높지 않은 현상을 말함 (지나치게 많은 질문, 쓸모없는 질문)
  - split가 많아질수록 하나의 leaf 안의 데이터셋이 적어진다
    - may make very unreliabel predictions for new data bc each prediction is based on only a few houses
- Underfitting 
  - faililng to capture relevant patterns, again leading to less accurate predictions 
  - 모델이 데이터의 중요한 패턴을 인지하지 못해 학습 데이터에서조차 성능이 좋지 않은 경우
  - decision tree의 split가 너무 적은 경우
- Overfitting 과 Underfitting 사이의 적절한 지점을 찾아야한다!
![Overfitting and Underfitting](https://storage.googleapis.com/kaggle-media/learn/images/AXSEOfI.png)
### How to control between overfitting vs underfitting
- `max_leaf_nodes`
  - get_mae 라는 함수를 만들어 모델 정의부터 피팅, 예측, mae를 반환하도록 한다. 이때 model = DecisionTreeRegressor(max_leaf_nodes = n) 으로 설정 후 모델을 만들고, 피팅과 예측, MAE를 구한다. n을 5, 50, 100 등 바꿔보며 MAE를 비교하면서 몇 개의 depth가 있는 것이 적절한지 예측할 수 있다. 

## 6. Random Forests
- 랜덤으로 몇 가지의 데이터셋을 추출하고, 질문의 요인들도 랜덤으로 추출 해 분류된 결과의 평균을 구함 
- 결정트리모델에 비해 정확도가 높다