# itertools.combinations
`itertools.combinations(iterable, r)`
- 경우의 수(조합)를 구할 수 있는 함수 
- 조합
- 예시
  ```python
    imort itertools

    # 2개를 뽑는 조합
    com_2 = itertools.combinations(['A', 'B', 'C'], 2) 

    # 결과
    list(com_2)

    # 경우의 수
    len(com_2)
  ``` 