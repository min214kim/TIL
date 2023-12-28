# 선형회귀
## 학습 방법
1. Gradient descent based 
  - 실제 값과 예측치의 오차 최소화하는 파라미터 찾는 것이 목표 
    - 선형 회귀 
    - 오차을 양수로 만들기 위해, 오차 제곱의 합으로 변환 (Squared Error)
    - 오차제곱을 최소화할 수 있는 weight(w1, w0) 값 : 최대/최소 문제로, 미분 활용 
  - 모델이란? 수학 식이다 
    - 넘파이를 사용해 수학식 표현하는 법 알아두는 것이 좋다 

## 선형회귀란
- 하나 이상의 변수와 연속적 타겟 변수 사이 관계를 모델링 (예측) 
  - 연속적 값: 키, 돈 등 (분류와는 다름 범주형 변수는 로지스틱 회귀로 본다)
- 데이터를 잘 나타내는 선을 그리는 것이 목표 

## 비용함수 (Cost function, loss function)
- 예측 함수(=가설 함수) : f(x) = h0(x) (0:우리가 찾아야하는 w값)
- 비용 함수 : 실제값과 가설함수의 차이
- wieght의 최적값 찾기 : 선형회귀에서는 gradient descent 를 거의 쓰지 않고, 연립방벙식 푸는 것으로 찾는다. (normal equation)

## Nomal equation
- 코드로 구현하기
``` python
class LinearRegression(object):
  def __init__(self, fit_intercept=True, copy_X=True):
  # fit_intercept = True : 절편값을 넣어준다 
  # copy_X = True : 기존의 X데이터를 복사하지 않으면 X값 자체가 변할 수 있어서 카피해서 알고리즘을 돌림 
    self.fit_intercept = fit_intercept
    self.copy_X = copy_X

    self._coef = None
    self._intercept = None
    self._new_X = None

  def fit(self, X, y):
    self._new_X = np.array(X)
    y = y.reshape(-1, 1)

    if self.fit_intercept:
      intercept_vector = np.ones([len(self._new_X), 1])
      self._new_X = np.concatenate(
        (intercept_vector, self._new_X), axis=1)

    weights = np.linalg.inv(
      self._new_X_.T.dot(self._new_X)).dot(self._new_X.T.dot(y).flatten())
    
    if self.fit_intercept:
      self._intercept = weights[0]
      self._coef = weights[1:]
    else:
      self._coef = weights

  def predict(self, X):
    test_X = np.array(X)

    if self.fit_intercept:
      intercept_vector = np.ones(l[en(test_X), 1])
      test_X = np.concatenate(
        (intercept_vector, test_X), axis=1)

      seights = np.concatenate(([self._intercept], self._coef), axis=0)
    else:
      weights = self._coef
    return test_X.dot(weights)
    

  @property
  def coef(self):
    return self._coef

  @property
  def intercept(self):
    return self._intercept 



```
## 훈련
- 모델의 훈련
  - 훈련의 지표 : 비용함수
- 비용함수
  - MSE (Mean Squared Error)
    - 회귀 모델의 주요 손실 함수 
    - 참값, 예측값의 차이인 오차들의 제곱 평균
    - 제곱을 하기 때문에 이상치에 민감 
  - MAE (Mean Average Error)
    - 참값, 예측값의 차이(오차)들의 절대값 평균
    - MSE보다 이상치에 덜 민감 
  - RMSE (Root Mean Squared Error)
    - MSE에 루트를 취해줌
    - 참값과 비슷한 값으로 변환하기 때문에 해석이 쉬워짐
  - 보통 quadratic(2차 곡선형태) 형태의 미분 편의성이 좋기 때문에, 비용함수로 MSE를 많이 사용함 

## 선형 회귀 모델의 최적화 방법
1. 정규 방정식
   - 비용 함수를 최소화하는 세타 값을 찾기 위한 해석적 방법 
   - n개 특성수에 따라서 (n+1) * (n+1) 의 X XT 역행렬을 계산
     - 특성 수가 많아지면 구현 속도가 느려짐
   - 모델의 복잡도가 훈련 세트의 샘플 수와 특성 수에 선형적으로 증가
   - 메모리 공간 충분하면 큰 훈련 세트도 효율적으로 처리 가능 