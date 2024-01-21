# 09 추천시스템
## 1.유형
### (1) 콘텐츠 기반 필터링 (Content based filtering)
- 
### (2) 협업 필터링(Collaborative Filtering)
1. 최근접 이웃(Nearest Neighbor) 협업 필터링
   - 아마존의 경우 아직 사용 
   - 메모리 협업 필터링이라고도 함 
   1) 사용자 기반 : 사용자와 비슷한 고객들이 구매한 상품을 추천
   2) 아이템 기반 : 해당 상품을 선택한 다른 고객들이 구매한 상품 추천 (주로 더 정확)
      - 아이템의 속성과 관계 없이, 사용자들이 그 아이템을 평가한 평가척도가 유사 아이템을 추천하는 기준이 된다!
      - Counter Vectorize 후 코사인 유사도를 활용해 행별(해당 영화에 대한 여러 사람들의 평점) 유사도를 측정해 도출 
      - > [공식]
2. 잠재 요인 (Latent Factor) 협업 필터링 
   - 넷플릭스 추천 시스템 경연 대회에서 행렬분해 기법 이용 잠재 요인 협업 필터링 방식이 우승하며 대부분 이걸 사용하기 시작 
   - **행렬분해(Matrix Factorization)** 사용
   - 사용자-아이템 평점 매트릭스 속 숨어있는 잠재 요인 추출해 추천 예측 : 대규모 다차원 행렬을 SVD와 같은 차원 감소 기법으로 분해하는 과정에서 잠재 요인 추출 
   - 사용자-아이템 평점 행렬 -> (사용자-잠재요인 행렬 , 잠재요인-아이템 행렬) 로 분해 후 이 행렬의 내적곱을 통해 예측 평점 도출 
## 2. 행렬분해
- 다차원 매트릭스 --> 저차원 매트릭스로 분해 
- SVD(Singular Vector Decomposition), NMF(Non-Negative Matrix Factorization) 사용
   > **R = P*Q.T**
   > 
   > R : MxN 사용자-아이템 행렬 / P: MxK 사용자-잠재요인 행렬 / Q : NxK 아이템-잠재요인 행렬
- R행렬을 P와 Q로 분해하기 위해 **SGD**(Stochastic Gradient Descent)를 사용한다
  - SVD의 경우, NaN 값이 없는 행렬에만 적용이 가능하기 때문 
### 확률적 경사 하강법(SGD)을 이용한 행렬 분해
> 예측된 R행렬 값이 실제 R행렬과 최소의 오류를 가지도록 비용 함수 최적화를 통해 P와 Q를 예측하는 방법
- P와 Q를 임의의 값을 가진 행렬로 설정
- P와 Q.T 값을 곱해 예측 R행렬을 계산
- 예측 R 행렬과 실제 R 행렬에 해당하는 오류 값 계산 
- 오류 값을 최소화할 수 있도록 P와 Q행렬 업데이트
- 위 작업 반복하며 근사화
```python
   # 행렬 생성
   import numpy as np
   R = np.array[[4,np.Nan,np.Nan,2,np.Nan],
                  [np.Nan,5,np.Nan,3,1],
                  [np.Nan,np.Nan,3,4,4],
                  [5,2,1,2,np.Nan]]
   num_users, num_items = R.shape # (4,5)
   K = 3 # 잠재요인의 개수 
   # np.random.normal : 정규분포로부터 임의의 샘플 그림
   P = np.random.normal(scale=1./K, size=(num_users,K))
   Q = np.random.normal(scale=1./K, size=(num_items,K))

   # 오차를 가져오는 함수 생성
   from sklearn.metrics import mean_squared_error
   def get_rmsa(R,P,Q,non_zeros): # non_zero는 추후 코드에서 생성
      error = 0
      # 예측 R 생성 (P와 Q의 전치 내적)
      pred_R = np.dot(P,Q.T)

      # 실제 R에서 null이 아닌 값의 위치 인덱스 추출 (예측R과 비교위해)
      x_non_zero_ind = [non_zero[0] for non_zero in non_zeros]
      y_non_zero_ind = [non_zero[1] for non_zero in non_zeros]
      R_non_zeros = R[x_non_zero_ind, y_non_zero_ind] #
      full_pred_matrix_non_zeros = full_pred_matrix[x_non_zero_ind, y_non_zero_ind]
      mse = mean_squared_error(R_non_zeros, full_pred_matrix_non_zeros)
      rmse = np.sqrt(mse)

      return mse

```
- 실제 적용하기 
```python
   # R>0인 행과 열 위치, 값을 non_zero 리스트에 저장 
   non_zeros = [ (i, j, R[i,j] for  i in range(num_users) for j in range(num_items) if R[i,j] > 0 )]

   steps = 1000 # 몇번 반복할건지
   learning_rate = 0.01
   r_lambda = 0.01

   # SDG기법 
   for step in range(steps):
      for i, j, r in non_zeros:
         # 실제 값과 예측 값의 차이인 오류 
         eij = r - np.dot(P[i,:], Q[j,:].T)
         # Regularization을 반영한 SGD 업데이터 공식 적용
         P[i,:] = P[i,:] + learning_rate*(eij * Q[j,:] - r_lambda*P[i,:])
         Q[j,:] = Q[j,:] + learning_rate * (eij * P[i,:] - r_lambda*Q[j,:])

         rmse = get_rmse(R,P,Q,non_zeros)
```
- 예측행렬 생성 
```python
   pred_matrix = np.dot(P,Q.T)
   # 실제 값을 출력해보면, 원본 행렬과 비교해 널이 아닌 값은 큰 차이가 나지 않음! 
```
- np.random.normal : 정규분포로부터 임의의 샘플 그림
  - 파라미터 : loc=평균의 위치, scales=표준편차, size=샘플사이즈, loc와 scales는 float형태로 받음(?)
- np.array는 R[[1,2],[2,3]] 이렇게 다차원 리스트로 인덱싱이 가능하다(?)
<br>
<br>

## 3. 콘텐츠 기반 필터링 추천 시스템 - 코드
**선택한 아이템과 비슷한 장르의 아이템 추천**
### 1. CountVectorizer 피처 벡터화
- 문자열로 변환된 장르 컬럼을  Count기반으로 피처 벡터화
- 장르 문자열을 피처 벡터화 행렬로 변한한 데이터 세트를 코사인 유사도 통해 비교 
- 장르 유사도가 높은 영화 중에 평점이 높은 순으로 영화 추천 
```python
   from sklearn.feature_extraction.text import CountVectorizer

   count_vect = CountVectorizer(min_df=0, ngram_range=(1,2))
   genre_mat = count_vect.fit_transform(movies_df['genres_literal'])
```
- CounterVectorizer()
  - min_df : 너무 희소하게 나오는 단어 제거
    - min_df = 0.01 : 1% 이하로 나오는 단어 제거 
    - min_df = 0 : 모든 단어 사용
  - max_df : 너무 자주 나오는 단어 제거
    - max_df = 0.5 : 50%이상 나오는 단어 제거
    - max_df = 1.0 : 모든 단어 사용
  - ngram_range (최소단어수, 최대단어수) : 공백으로 분할한 단어들을 이용해서 범위 내에서 구성 

### 2. 코사인 유사도 반환
  - 행별로 유사도를 행렬으로 반환히줌 
```python
from sklearnmetrics.pairwise import cosine_similarity

genre_sim = cosine_similarity(genre_nmat, genre_mat)

# 반환된 genre_sim값에서 유사도 값이 가장 높은 순으로 정렬된 행렬의 위치 인덱스 값 추출
genre_sim_sorted_ind = genre_sim.argsort()[:, ::-1]
```
- `np.argsort()`
  - 주어진 배열의 요소를 정렬 후 **인덱스**를 반환해주는 함수 
- `list[a:b:-1]`
  - 리스트에서 역순으로 출력하는 방법 : a인덱스에서 b인덱스까지 역순으로 출력해준다 , 0일경우 생략 가능!
### 3. 유사도에 따른 추천 함수
- 유사도에 따라 영화 추천하는 함수 생성
```python
   def find_sim_movie(df, sorted_ind, title_name, top_n=10):
      # 영화 데이터프레임에서 영화명이 넣은것과 같은 행 추출 (사용자가 이미 본 영화)
      title_movie = df[df['title'] == title_name]

      title_index = title_movie.index.values
      similar_indexes = sorted_ind[title_index, :(top_n)]

      # 위 인덱스는 2차원이므로 1차원으로 변경
      similar_indexes = similar_indexes.reshape(-1)

      return df.iloc[similar_indexes]

   # 함수 호출
   find_sim_movie(movies_df,genre_sim_sorted_ind,'The Godfather',10)
``` 
- `np.reshape()`
  - `np.reshape(-1)` : 1차원으로 반환
  - `np.reshape(4,2)` : 해당 array를 4*2 행렬로 반환
  - `np.reshape(-1,n)` : -1이 행에 들아간다면 행의 값은 원래 배열의 길이와 남은 차원으로부터 알아서 추정. (열 n개가 나오게 하려면 행은 몇개인지 알아서 추정), vice versa
- 리스트 객체 내 값을 연속된 문자열로 반환하기 위한 함수
  - `('구분자').join(리스트)`

### 4. 평점을 도입한 추천 - 정확도 증가를 위한 가중평점 도입
- 여러 후보군 선택 후 그 중 편점이 높은 것을 추천해주는 시스템
- 높은 평점 기준으로 추천 시, 인기가 없는 작품이 오히려 평균 평점은 높은 왜곡이 생길 수 있다.
- 따라서, 가중치가 부여된 가중 평점 사용 (영화 평점 사이트 IMDB에서 사용하는 방식)
> 가중평점 : ( v / (v+m)) * R + (m / (v+m)) * C 
> - v : 영화별 평점 투표 횟수
> - m : 평점 부여 위한 최소 투표 횟수 (투표 횟수에 따른 가중치를 직접 조절하는 역할. 높으면 평점 투표 횟수가 많은 영화에 더 많은 가중 평점 부여)
> - R : 영화별 평균 평점
> - C : 전체 영화 평군 평점
- 가중평점 
```python
   C = movies_df['vote_average'].mean()
   m = movies_df['vote_count'].quantile(0.6) # 여기서는 전체 투표 횟수에서 상위 60%를 m으로 정함
   def weighted_vote_averate(record):
      v = record['vote_count']
      R = record['vote_averate']

      return ( (v/(v+m)) * R + (m/v+m) * C )

   # 함수 호출
   movies_df['weighted_vote'] = movies.apply(weighted_vote_average, axis=1)
```
- 가중평점을 고려한 영화 추천 함수
```python
   def find_sim_movie(df, sorted_ind, title_name, top_n=10):
      title_movie = df[df['title'] == title_name]
      title_index = title_movie.index.values

      # top_n의 2배에 해당하는 장르 유사성 높은 인덱스 추출
      similar_indexes = sorted_ind[title_index, :(top_n*2)]
      similar_indexes = similar_indexes.reshape(-1)

      # 해당 후보군에서 가중평균 높은 순으로 top_n만큼 추출
      return df.iloc[similar_indexes].sort_values('weighted_vote',ascending=False)[:top_n]

   # 함수 호출
   find_sim_movie(movies_df,genre_sim_sorted_ind,'The Godfather',10)
``` 
## 3. 최근접 이웃 협업 필터링 - 코드

### 1. 협업 필터링을 위한 데이터 만들기
- pivot table로 데이터프레임을 로우:사용자 - 컬럼:영화 형태로 변경 
- 예제의 경우, 영화명이 아이디로 들어가있기 때문에, 영화명-영화제목 데이터프레임과 join을 통해 영화 아이디를 영화명으로 대체 
- 평점은 0.5부터 5까지 0.5점 단위로 부여. Nan값은 0으로 대체
```python
   # ratings df :유저아이디 - 영화아이디 - 평점 형태의 데이터프레임
   # movies df : 영화아이디 - 영화명 - 장르 형태의 데이터프레임

   rating_movies = pd.merge(raings, movies, on='movieId')
   ratings_matrix = ratings_movies.pivot_table('rating', index='userId', columns='title')
   ratings_matrix = ratings_matrix.fillna(0)
```
### 2. 영화 간 유사도 산출
- 위의 `ratings_matirx` 데이터프레임에 코사인 유사도를 계산하면, 사용자 간의 유사도가 만들어짐
- 우리는 아이템 기반의 협업필터링이기 때문에, 영화들 간의 유사도를 측정해야함 -> 데이터프레임 변경 필요
- `transpose()` 함수를 통해 새 행렬 만들기
```python
   # df의 형태 변경
   ratings_matrix_T = ratings_matrix.transpose()

   # 유사도 계산
   from sklearn.metrixs.pairwise import cosine_similarity

   item_sim = cosine_similarity(ratings_matrix_T, ratings_matrix_T)

   # 유사도 넘파이 행렬에 영화명 매핑해서 DataFrame로 반환
   item_sim_df = pd.DataFrame(data=item_sim, index=ratings_matrix.columns, columns=ratings_matrix.columns)

```
- 유사도가 높은 영화 추출하기 : input으로 넣은 영화와 가장 비슷한 사용자 평점을 받은 영화를 추천해준다
```python
   item_sim_df['Godfather, The (1972)'].sort_values(ascending=False)[:6]
```
### 3. 아이템 기반 최근접 이웃 협업 필터링으로 개인화된 영화 추천
- 앞은 영화 간의 유사도만으로 추천함. 3번에서는 개인에게 최적화된 영화 추천 구현
- 개인이 아직 관람하지 않은 영화 추천! : 관람하지 않은 영화에 대해 아이템 유사도 + 기존에 관람한 영화의 평점 데이터를 기반으로 모든 영화의 예측 평점 계산 후 추천 
- 개인화된 예측 평점은 아래의 식으로 구한다. 
![협업필터링식](https://velog.velcdn.com/images/ranyjoon/post/d040df10-cf7b-4692-9976-18e661f73fe3/image.png)
  - Si,N : 아이템 i와 가장 유사도가 높은 Top-N개 아이템의 유사도 벡터 
  - Ru,N : 사용자 u의 아이템 i와 가장 유사도가 높은 Top-N개 아이템에 대한 실제 평점 벡터 
<br>
<br>
<br>
- Rui는 사용자 u의 모든 영화에 대한 실제 평점과 영화 i의 다른 모든 영화와의 코사인 유사도를 벡터 내적 곲 한 값을 정규화를 위해 SiN으로 나눈 것 
- Top-N 유사도를 가지는 영화 유사도 벡터만 적용하기 위해서는 행, 열별로 for 루프를 반복 수행하며 계산해야하기 때문에 시간이 오래 걸린다
```python
   # N의 범위에 제약을 두지 않을 경우
   def predict_rating(ratings_arr, item_sim_arr, n=20):
      # 사용자-아이템 평점 행렬 크기만큼 0으로 채운 예측 행렬 초기화
      pred = np.zeros(ratings_arr.shape)

      # 사용자-아이템 평점 행렬의 열 크기만큼 루프 수행
      ratings_pred = ratings_arr.dot(item_sim_arr)/np.array([np.abs(item_sim_arr).sum(axis=1)])
   # 위의 함수 이용해 개인화된 예측 평점 구하기 
   ratings_pred = predict_rating(ratings_matrix.values), item_sim_df.values
   ratings_pred_matrix = pd.DataFrame(data=ratings_pred, index=ratings_matirx.index, columns=ratings_matrix.columns)
```
### 4. MSE 줄이기 
- 평점 부여하지 않은 영화는 0으로 부여했으나 개인화된 예측 점수는 평점을 주지 않은 영화에 대해서도 아이템 유사도에 기반해 평점을 예측했으므로, 기존에 평점을 부여한 영화에 대해서만 MSE 측정 
```python
   def get_mse(pred, actual):
      # 평점이 있는 실제 영화만 추출
      pred = pred[actual.nonzero()].flatten()
      actual = actual[actual.nonzero()].flatten()
      return mean_squared_error(pred, actual)
```
  - `np.flatten()` : 차원을 1차원으로
    - 복사본 만들어줌
    - order = 'C' : row, 'F' : column 순서로 flatten
  - np.nonzero() : 값이 0이 아닌 인덱스값 반환
    - 반환된 결과에서 인덱스가 같은 것을 묶으면 0이 아닌 값들의 인덱스가 됨 
## 4. 잠재 요인 협업 필터링 - 코드
