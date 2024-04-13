# 크롤링 문법




## 파싱

bs4 BeautifulSoup 객체인 bs_obj에서 추출한 값을 uls변수에 저장 
type(uls) --> bs4.element.Tag (아직 문자열이 아닌 객체형태)

next_sibling이라는 속성값

- a태그
    - 속성의 값은 인덱싱을 통해 가져올 수 잇음!
      - bs_obj.findAll('a')[0]['href'] 와 같이 
    - 여는태그와 닫응태그 사이의 글자 : text 속성 사용 
      - bs_obj.findAll('a')[0].text


selector : findAll과 비슷한 함수
bs_obj.select('a') : 해당 태그 모두 찾아서 list로 반환 
- 이건 딕셔너리 형태로 id선택자를 넣는게 아니라 # 활용한다는 점에서 좀 더 용이 
- bs_obj.select('div #mainMenuBox') 이런식으로

크롬에서 오른쪽 클릭 -> 검사 (inspect) 누르명 해당하는 html코드를 개발자도구에서 볼 수 있음 (우리가 추출해야할 메뉴를 다 담고 있는 태그가 무엇인지 확인가능)
그 코드에서 오른쪽 클릭 -> copy -> copyselector 후 붙여넣기 : select 함수 사용할 때 더 쉬움 

