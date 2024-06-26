# Django Project 예시 
- django project 생성 시 한글이 없는 디렉토리에!
   - 워크스페이스 저장
   - shell 말고 커멘드 터미널 사용 
 - 가상환경 만들기 : python -m venv venv
   -   맥은 (base)로 들어와있으면 이미 가상환경 만들어진거라 그냥 쓰면 됨
-   pip install Django
-   프로젝트 생성
    -   django-admin startproject ai_testPrj
        -   ai_testPrj안의 manage.py
        -   만들 때 프로젝트명 안쓰고 . 쓰면 그냥 해당 폴더가 프로젝트가 됨 
-   장고의 모든 시작은 manage.py파일! 
    -   이 프로젝트에서는 두 개의 app을 넣을 예정 : machine learning관련 앱, deep learning관련 앱 
    -   장고가 각각의 앶을 어떻게 관리하고 여기서 클라이언트로 넘겨주는 js나 css 이미지 같은 것들 어떻게 넘겨줘야하는지 구성에 관한 내용 위주로 설명! 
-   **ai_testPrj 파일에 들어와서 시작하는거 잊지 말기**
1.    서버실행 확인 (강의자료 9p)
    -   python manage.py runserver  
    -   web들어가서 잘 작동하는지 확인 후 ctrl c로 닫아야함!
2.   마이그래이션 : 사용하겠다고 디폴트로 설정되어있는 db.sqlite3에서 데이터베이스 관련한 테이블과 설정을 외부의 DBMS에 반영시켜주기 위한 준비 
    -   python manage.py makemigrations
    -   모델에 실제로 반영해주세요 : python manage.py migrate   
3.   app만들기 
    -   python manage.py startapp ai_app(앱이름)
    -   app 사용하겠다고 등록해주기
        -   ai_testPrj파일 안의 settings
        -   INSTALLED_APPS에 해당 app 이름 넣어주기
4.   url파일 따로 관리 (강의자료랑 순서 다름!)
    -   ai_app -> newfile -> urls.py
    -   app의 url이 프로젝트 url로 들어갈 수 있도록 코드 짜주기 (프로젝트가 app의 url들을 가지고와야함 )
        -   프로젝트의 url파일에서 `path("",include('ai_app.urls'))` 추가
            -   서버주소가 비어있으면, 이에 대한 내용은 ai_app의 urls가 가지고 있다는 의미
        -   from django.urls import include 함수 추가 
        -   http://localhost:8080 라고 클라이언트가 서버주소를 요청했을 경우, 위의 코드가 어떻게 해야할지 가지고 있음. 이 경우 ai_app.url에 패턴이 있으므로 이 파일에서 저 서버주소와 일치하는 파일을 여세요! 
    -   ai_app의 url 파일에 다음 내용 추가
        -   `from django.urls import path, include`
        -   `urlpatterns = [path("",include('ai_app.urls')),]`
5.   Template 설정
    -   ai_app에 templates dir생성 (html파일을 넣어둘 폴더) >  ai_app dir 생성 (app이름과 동일한 이름이어야함!) > 이 안에 index.html파일 생성
6.   url과 함수 연결
    -   ai_app>urls.py에서 클라이언트가 서버에 요청했을 경우 요청 처리할 함수 명시 : ai_app>views.py에 함수를 구성하고, 이걸 import 해준다
        -   ai_app>urls.py 위쪽에 `from . import views` 작성 (같은 경로에 있는 views파일 import하겠다는 뜻 )
        -   `path("",views.index, name='index')` 추가
            -   관리를 위해 path에 이름 설정 : 앞으로 이 url을 코드 내에서는 index라고 명시해도 됨! 
    -   ai_app > views.py에 다음내용 추가 
        ```python
            def index(request): # 요청내용에 대한 객체 request
                return render(request, 'ai_app/index.html') 
                # render : 파이썬 코드와 html코드가 혼용되어 있으면 파이썬 코드를 해석해서 html코드로 변환 후 클라이언트(request)에게 전송 

        ``` 
7.   강의자료의 package.txt를 manage.py와 같은 경로에 넣어준다 
    -   `pip install -r package.txt` : package 파일 안의 있는 패키지를 install해주는 것 
    ```
            Attempting uninstall: numpy
            Found existing installation: numpy 1.26.1
            Uninstalling numpy-1.26.1:
            Successfully uninstalled numpy-1.26.1
        Attempting uninstall: matplotlib
            Found existing installation: matplotlib 3.8.2
            Uninstalling matplotlib-3.8.2:
            Successfully uninstalled matplotlib-3.8.2
        Successfully installed joblib-1.3.2 matplotlib-3.7.3 numpy-1.24.3 pandas-2.0.0 pytz-2023.3.post1 scikit-learn-1.3.0 seaborn-0.12.2 threadpoolctl-3.2.0 tzdata-2023.4 라고 뜸.. 왜 uninstall된거지?
    ```
## 모델 백엔드 프로그램
- 아이리스 품종 예측 프로그램 
- 모델만 실행하는 폴더 생성하기 : ai_app > modules폴더 생성 , modules > __init__.py(이게 있어야 모듈로 인식이 돼서 import할 수 있음. 빈파일로 생성해도 된다!), data_anal.py 생성 
  - view에 다 crud 넣어버리면 어긋남! 
  - 분석이라는 기능에 대한건 모듈화 시켜서 빼줘야함 
  - 강의자료 iris.pkl 파일 modules 폴더 안에 넣어두기 
### ver.2 : index.html 출력 및 입력 창만 확인
- `data_anal.py`에 데이터 분석(시각화,모델예측등) 관련 프로그램을 함수화
  - 강의자료의 web강의1_참고코드.txt의 29쪽 내용을 data_anal.py에 복붙
  - 안에 ver2 처리 함수가 있음. 여기서 `joblib.load(file_path /'iris.pkl')`로 pkl파일을 불러올 수 있다
- views.py파일에 강의자료의 ver.2에 해당되는 함수 생성 , 아래 내용 추가 
  ```python
      from .modules.data_anal import iris_model_load
      # ver.2 : 코드에 입력되어 있는 임의 숫자에 대한 예측결과 반환 -> 클라이언트에게 전송
      def index(request): 
          class_name = iris_model_load()
          return render(request, 'ai_app/index.html',{'class_name':class_name}) # index.html로 이 dict 내용이 전송됨!
  ``` 
### ver.3 사용자에게 입력받아서 결과 반환 (ver.3) 
- 모듈 수정 : data_anal.py에 강의자료 35쪽 내용 함수 추가
  ```python
  def iris_predict_fn(s_l, s_w, p_l, p_w) :
    file_path = settings.BASE_DIR / 'ai_app' / 'modules'
    loaded_model = joblib.load(file_path / 'iris.pkl')
    pred = loaded_model.predict([[s_l, s_w, p_l, p_w]]) # 파라미터로 전달된 값을 활용해서 예측

    if pred[0] == 0:
        result = 'setosa'
    elif pred[0] == 1:
        result = 'versicolor'
    else:
        result = 'virginica'
    return result
  ``` 
  - 위와 동일한 함수지만 사용자에게 파라미터로 값을 입력하도록 하는 것만 다름! 
- `index.html`에서 확인버튼 눌렀을 때 어떻게 작동할것인지 정의해줌
  - views.py에 아래 추가
  ```python
      from .modules.data_anal import iris_model_load , iris_predict_fn
      # ver.3 : 입력받은 data 이용해서 예측하는 함수, 사용자가 데이터 입력 후 버튼 클릭하는 요청에 대해 처리 
      def iris_predict(request) : 
          if request.method == "POST" : 
              sepal_length = request.POST.get('sepal_length', '') # 사용자가 요청시 전달해준 form data 추출 
              sepal_width = request.POST.get('sepal_width', '')
              petal_length = request.POST.get('petal_length', '')
              petal_width = request.POST.get('petal_width', '')
              
              print(petal_width)

              class_name = iris_predict_fn(sepal_length, sepal_width, petal_length, petal_width)
          
              return render(request, 'ai_app/index.html', {'class_name':class_name})
          else:
              return render(request, 'ai_app/index.html', {'result':None})
  ```  
  - ai_app > ulrs.py 에서 `path("iris_predict/", views.iris_predict, name='iris_predict')` 추가 
  - index.html 에서 `<form id='predict-form' action="{% url 'iris_predict'%}" method="post">` 추가
### ver.4 페이지 새로고침 대신 결과 부분만 바뀌도록 (Ajax 사용)
  - 확인 버튼 눌렀을 때 새로운 페이지가 아닌 부분 데이터만 변경하는 작업
  - static폴더 : javascript css 이미지같은 정적 파일들은 서버 실행하는 파일이 아닌 경우 static 폴더에 데이터 넣고 클라이언트 쪽으로 날아갈 수 있게끔 서버를 세팅해준다. 
  - 프로젝트 폴더 안에 static폴더 생성 후 관련 js파일 저장 (강의자료에 있는 것 저장하면 됨!)
    -  settings.py에 static 경로 추가

        ```python
            STATIC_URL = "static/"

            # 서버에 static 파일 경로 
            STATICFILES_DIRS = [
                BASE_DIR / 'static'
            ]
        ```  
    -   static > js폴더 생성, 그 안에 강의자료의 iris_predict.js(만들어야하는 코드)와 jquere-3.7.1.min.js파일 넣기 (이건 제공되어지는 코드임 )
    -   urls.py 에 path 추가 :`path('iris_predict_ajax/' views.iris_predict_ajax, name='iris_predict_ajax')`
    -   index.html파일 수정
        -   html파일 맨 위에 `{% load static %}` 넣어줌 

        ```python
            <head>
                <meta charset="UTF-8">
                <title>index 페이지</title>
                <script src="{% static '/js/jquery-3.7.1.min.js'%}"></script>
                <script src="{% static '/js/iris_predict.js'%}"></script>
            </head>
        ```   
        - 위 코드 추가 : 클라이언트 쪽으로 날아감? 
    - views 수정
      - iris_predict_ajax 함수 생성, `return JsonResponse({'class_name':class_name})` 로 변경
      - `from django.http import JsonResponse` 추가
  - 이미지 등도 static파일에 추가 
  - 개발자도구에 static파일이 잘 뜨는지 확인!
  - index.html 파일에서 확인 버튼에 action이 포함되지 않아도 실행이 된다! 
### Ajax javascript 파일
```javascript
    $(document).ready(function () { // 다 준비가 되었다면 
    $("#predict-form").submit(function (e) { // id predict-form 태그내에서 submit(버튼클릭)이 발생하면 
        e.preventDefault(); // 함수를 실행 : submit 이벤트(서버에 페이지 새로 요청) 를 삭제 
        
        $.ajax({ // ajax가 서버에 요청보내고 응답되는 데이터도 받는다 
            type: 'POST',
            url: '/iris_predict_ajax/', // 요청할 서버 url 
            data: $(this).serialize(), // ajax가 적용되는 form태그내 form객체(input 태그 등) 내의 value값을 모두 묶어서 전송 
           
            success: function (response) { // 요청에 의한 응답이 성공하면, 서버가 준 데이터는 response 변수에 받음 
                console.log(response.class_name);
                $("#prediction_result").text("예측 결과: " + response.class_name); // prediction_result id 내에 예측결과와 response에서 받은 class_name을 넣어라!
            },
            error: function (error) { // 요청에 의한 응답이 실패 
                console.log(error);
            }
        });
    });
});
```
- `.serialize()` : 표준 URL 인코딩 표기법으로 텍스트 문자열을 생성 
  - form 태그에 사용 시 form의 객체와 값을 한번에 받을 수 있음 