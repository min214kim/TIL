# Inputs and Outputs
## 1. CSV Files
1. Input
   - pd.read_csv('파일경로', header=, index_col=열번호)
       - header : 판다스는 기본적으로 첫 행을 컬럼으로 읽어오는데, 이게 싫으면 header=None 옵션을 주면 됨
       - index_col : 첫 열을 인덱스로 설정하고 싶을 때 설정한다

2. Output
    - df.to_csv('파일경로,파일명', index=True/False)
      - index는 기본적으로 저장됨. 인덱스를 저장하고 싶지 않을 때 index=False를 해준다. 이 때 기존 인덱스는 'Unnamed:0'이라는 이름의 새로운 컬럼으로 들어간다. 

## 2. HTML File
