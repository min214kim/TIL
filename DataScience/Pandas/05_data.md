# Data
## 1. String Data
### Text 메소드 
1. 메소드
- str. + tab 로 정보 확인!
> `str.split('')`
  - ''안의 값을 기준으로 나눠준다
> `Series.str.upper()`
  - 해당 시리즈 안의 str을 모두 대문자로 바꾼다
  - 다시 할당해줘야 저장된다
> `Series.str.isdigit()`
  - 해당 문자가 숫자인지 boolean 시리즈 형태로 반환한다

2. split를 활용해서 시리즈를 df로 바꾸기
```python
tech_finance = ['GOOG,APPL,AMZN', 'JPM,BAC,GS']
tickers = pd.Series(tech_finance)
tickers.str.split(',').str[0] -> GOOG # .str을 붙여줘야하는걸 잊지 말자 

tickers.str.split(',', expand=True) -> df가 생성된다
``` 

3. 대체 메소드 
> `Series.str.replace('a', 'b')`
  - a를 b로 바꾼다 
> `.strip()`
  - white space를 지워주는 메소드 

## 2. Datetime Data

### Datetime 오브젝트

1. Datetime 오브젝트
  - 판다스에는 Datetime 오브젝트에 대해 dt메소드가 있다
    ```python
    from datetime import datetime
    mydate = date(year, month, day, hour, min, sec)
    mydate.year --> year반환
    ```
      - .year, .month, .day, .hour 다트연산자로 연, 일 시간 등을 반환할 수 있다
   - `pd.to_datetime(Series)` : Seires안의 str 데이터를 datetime데이터로 변환한다 
2. 유럽/아메리카 스타일
  - Europian(Y-M-D)/American style (M-D-Y) format 존재
  - pd.to_datetime(euro_date, dayfirst=True) 로 Europian datetime을 명시한다.
    - ex) 10-12-2000이 2000년 12월 10일인경우

### Time 메소드
1. Custom Timestring fromatting
  - ['DatetimeFormats'](https://pandas.pydata.org/pandas-docs/stable/user_guide/timeseries.html#converting-to-timestamps) 참고
  - 위의 링크를 참고해서 커스텀 포멧을 만들 수 있다.
  - example1
    ```python
    style_date = '12--Dec--2000'
    pd.to_datetime(style_date, format='%d--%b--%Y')
    ```
2. .resample()
  - timeseries data가 인덱스인 경우, .resample()함수를 사용할 수 있다.
  - basically groupby 메소드와 같은 것이라 볼 수 있다.
    - df.resample(rule='A').mean() 의 경우, 매년 마지막 날의 데이터들을 그룹화한 후 평균을 반환한다.
    - 'A'는 별칭인데, 타임 시리즈의 별칭은 검색해서 찾아봐야 한다