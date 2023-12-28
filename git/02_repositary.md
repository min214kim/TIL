

# 원격 저장소 활용하기

## 기본 명령어
|명령어|역할|예시|
|---|---|---|
|`git remote`|원격저장소에 대한 정보를 조회한다.|| 
|`git remote [저장소이름] [저장소주소]`|원격저장소를 설정한다.|git remote origin [github주소]
|`git branch`|branch 정보를 조회한다.|
|`git push`|원격 저장소에 내 컴퓨터의 commit내용을 저장한다.|
|`git pull`|원격 저장소에서 세로 commit된 내용을 가져온다.|
|`git clone [저장소주소]`|원격 저장소에 저장된 폴더 자체를 통째로 가져온다.|
|`git checkout`|포인터를 바꾼다.|

<br>

## 협업 단계
### 1. 회사(혹은 관리자) - 첫 단계
* **원격저장소 설정하기**
  * 먼저 github에서 저장소를 생성한다.
  * git remote [저장소이름][저장소주소]로 원격 저장소를 설정한다.
  * 저장소 이름은 내맘대로 해도 되나, 일반적으로 origin이라는 이름을 붙인다.
  * 저장소 주소는 오타가능성이 높으므로, github화면에서 copy + paste하는 것이 좋다.

* 팀원 접근 허락하기
  * 내 repository -> project settings -> collaborators -> add people

  * git branch : main 인지 master인지 확인 가능 

* 협업파일 저장하기
  * git push [저장소이름(origin)] [branch이름(main)]

* 접근허용의 불편함 해소하기 위한 방법
  * pull request : 접근허용의 불편함 해소
  * github에서 다른 프로젝트에 들어가 fork 누르기!
  * 다른 사람의 프로젝트를 가져와 내가 작업 후 pull request 가능
  * 만든 사람이 내 request를 수락할 때 수정된다.

<br>

### 2 .참여자
* 원격파일 다운받기 
  * 저장소에서 원격파일을 가져온다.
  * git clone [저장소주소]
  * mac은 ssh 저장소주소 사용

* 작업한것 원격저장소에 올리기
  * commit을 완료한다.
  * clone로 가져온건 clone받았던 주소를 origin으로 갖고있다.
  * git push [저장소이름] [브랜치이름]를 사용한다.

<br>

### 3. 다시 회사
* 프로젝트를 원격에서 가져오기 
  * git pull [저장소주소][브랜치이름] : 저장소를 clone할 필요 없이, commit된 것만 가져온다.
  * 여기서 github에서 설정한 프로젝트 이름을 폴더명으로 그대로 가져온다.
  * git clone [저장소주소] [프로젝트이름] 으로 해줄 시 폴더명이 바뀐다.

**git저장소의 상위 폴더에서 git init또는 git clone을 하면 안된다**

<br>

