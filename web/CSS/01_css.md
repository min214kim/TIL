# Selector 선택자
Css는 HTML요소의 style을 정의하는데 사용됨. 이를 위해 스타일을 적용하고자 하는 html요소를 선택할 수 있어야 함.

h1 {color:red;font-size:12px} 이런 식으로 선언.
여기서 h1이 셀렉터이다

# 프로퍼티 (property 속성)

인라인 css는 통일성때문에 잘 쓰지 않음 (모든 태그마다 써야하고, 수정 때도 직접 고쳐야하기 때문 )

CSS가 어려운 이유 : 
Cascading Style Sheet : cascading은 계단식이라는 뜻
css는 우선순위가 있다. 동시에 여러 style 적용 시 어떤 것 먼저 적용하는지 정해져 있어ㅡㅁ.
예를 들어, inline css로 정의된 style 가장 우선임.

# CSS 적용 방법 3가지 
1. inline에서 스타일 선언 
2. head에 선언
css에는 class가 있따! 인라인에 써줌 
id와 class 
id는 태그를 구분하는 유일한 구분자. 해당 태그를 선택하고 싶을 때 씀 (p 선택 시 p가 두개 있음 두개다 선택됨.. id쓰면 하나만 선택 가능 ) 
id는 중복해서 쓸 수 없다.
class 는 공통 특성으로 이름을 붙여줄 수 있는 것. 공통으로 묶을 수 있다. (학교의 반과 같은 느낌) 
class는 스타일 적용 시 .[classname]이라고 씀 
현업에서는 무조건 class를 이용해서 스타일을 적용함!
스타일링은 기본적으로 클래스로 한다 ~ 

3.link 사용
스타일 css를 따로 저장 후 head에 표기 현업에서 매우 ㅁ낳이 사용 

## 전체 셀렉터 (Universla Selector)
    우선순위 매우 낮음 
    * 사용
  ## 태그 셀렉터
  우선순위 낮음

  ## id 셀렉터
  #~~ 하고 헤드에서 부틈 
    근데 안씀.. javascript때문에 id를 양보했기 때문. css에서는 id안쓴다. 

## class 셀렉터
사실 이게 거의 쓰임. 

##
a[hef] (스타일) : 이 형식에 스타일 적용
a[target="__blank"]

## 부정
h1[title~=first]


>??
색이랑 길이 단위까지 

## 색지정
rgba 

# 박스모델 (매우 중요)
* 레이아웃을 결정하는 박스!
  * 컨텐트-보더 사이가 패딩, 보더 밖이 마진 
  * 보더 부터 박스의 영역이다.
  * boarder radius : 
    * 사실 에셋을 쓰면 되긴 한다. 
  * boarder box vs content box

# block
* 항상 새로운 라인에서 시작
* 화면 크기 전체의 가로폭을 차지
* ... 내용 확인 
* 
# inline 요소

# 상속과 적용 (어려운 부분)

# flexbox
* 개별 요소 정리 위해 밖을 감싸가ㅗ 있는 것에 flexbox속성을 준다.
* 축 이라는 개념 : 주축과 교차축 : 
* jusstify-content: 주축이동 (기본값:가로축)
  * flex-start, flex-end, center, space-around, space-between
* align-items: 교차축 이동 (세로축)
  * flex-start, flex-end, center, 
* flex-direction: 주축을 결정 
  * row, row-reverse(주축이 가로축인데, 방향 반대), column(주축이 세로축으로), column-reverse(주축 세로축, 방향 반대)
* 개별이동
  * order: 특정 애만 순서를 바꾸는 것
    * .yellow{order: 1;}
    * 초기값은 order 0임. 숫자가 적을수록 앞으로.
    * 다른게 다 0이라면, 특정 애를 +1 해준것과 +100 해준것 결과 같음.
  * align-self: 특정 애만 교차축 이동
* wrap: flexbox는 공간이 작아도 그냥 우겨넣음. 공간을 넘으면 줄을 넘어가게 하는 것이 wrap
  * nowrap, wrap, wrap-reverse
* flex-flow: flex-direction과 wrap를 한줄에 쓸 수 있다
  * flex-flow [flex-direction] [wrap]
* align-content: 행간 결정 (교차축) 
  * wrap해서 여러 줄이 생겼을 때만 의미가 있음
  * flex-start, flex-end, center, space-between, space-around, space-evenly, stretch(default)

# 부트스트랩 라이브러리 

서버 입장에서는, pc나 모바일이나 태블릿이나 앱이나 전부 같음. 
이 서버에서 하는게 백앤드 개발자, 
html아니고 json을 주기도 함.
아무튼, 앱개발도 클라이언트 개발이라 프론트엔드임.

이건 css업그레이드 버전인 scss sass 에 대해 지원해줌 

버튼 만들 때 class만 가져오면 됨 css따로 작성 필요 없고, 카드도 그냥 클래스로 만들 수 있고,, 홈피 상단의 메뉴도 

깃헙이 대표적으로 부트스트랩 갖다가 커스텀하는 기업 

**pc뿐아니라 모바일용 디자인을 반응형으로 한번에 지원**
여러 웹 브라우저를 지원하기 위한 크로스 브라우징에 골머리를 썩일 필요가 없다!

구형브라우저 지원이 미흡 

라이브러리/
  제어권이 사용자에게 있음 (내가 갖다쓰고 싶은걸 갖다씀)

프레임워크
  내가 자유롭게 뭔가를 하기보단 정해진 프로세스 안에서 일을 하는 것 

  모바일을 먼저 짜야함 (작은화면 먼저 짜야한다)

## semantic
header, nav내비게이션의미, aside사이드에위치하는 공간 의미, section본문의 여러 내용을 포함하는 공간ㅇ르 의미(ex.정치 섹션, 00섹션 등 ..), article본문의 주내용이 들어가는 공간을 의미, footer 푸터의미
이전에는  div태그로 영역을 구분했지만, div 는 아무 의미가 없어서
요즘에는 sexantic태그를 쓴다. 기능적으로는 얘도 의미 없음. 근야 공간ㅇ르 묵어주는 용으로 쓰는 것 

SEO잘쓰기 중 하나에 semantic잘쓰는 것이 있음 ! 그러니 아무런 의미가 없는 것은 아님.. 큰 차이가 있다 특히 장기적 관점으로 봤을 때 사이트ㅡ이 유입을 늘릴 수 있는 방법
웹 표준을 잘 지키면 지킬수록 검색엔진이 좋아함 (구글, 네이버 문서 다 있음 ! 읽어보고 지켜놔야함)

##
구글 개발자도구에서 먼저 wrap등을 주면 어떻게 나올지 확인해보고 코드 수정하는 것
##
class = "d-flex" 라고 해도 됨 
https://getbootstrap.com/docs/5.3/utilities/flex/
위를 참고하면, 어제 배운게 다 class에 묶여있을 수 있음 

## margin주기
https://getbootstrap.com/docs/5.3/utilities/spacing/

아랍어는 오른쪽으로 시작 그래서 ml mr 대신 ms me가 됨 (margin start margin end)
mx : 양옆에 마진
my: 상하

alt + 클릭 : 멀티커서 in vscode 취소하려면 esc

# grid
기본적으로 row-col 
12 column system : 로우는 12개로 구성되어있다. (로우는 12칸임)
--> col이 4개이면 개당 3씩 잘라먹는 것 
class = "col-6" 라고 설정 시  해당 col은 무조건 반을 차지
col-md-4 : mid사이즈부터 (더 클때) 4칸으로 설정

더 쉽게 : row에서 class="row row-cols-2" 설정 시 한 줄에 clo이 두 개씩 있게 설정

row/col 에 별말 없으면 xsmall
## breakpoints
전환점 
- 화면크기에 기준들이 있음 
boothstrap에서 화면 사이즈에 맞춰서 디바이스나 viewport size (가로길이) 기반으로 커스텀할 수 있는 것 
## containers
https://getbootstrap.com/docs/5.3/layout/containers/
어떤 사이즈로 나오는지 적은 것 
container fluid : 어떤 breakpoint지나도 무조근 100% 

# nesting
중첩 \row안에 row를 넣을 수 있음 
