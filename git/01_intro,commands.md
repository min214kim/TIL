# Git
>코드를 관리하는 도구 (버전을 통해)

* SCM : Source Code Management
* 분산형 버전 관리도구 (Version Control System) : 분산된 형태로 버전을 통해 코드를 관리하는 코드다. (반대: Single sourced)
* 버저닝을 하는 이유 : 새 버전에 버그가 발견될 경우, rollback으로 코드를 이전 것으로 되돌릴 때가 있다.

<br>

* 코드 관리도구
* 코드 협업도구
* 코드 배포도구

<br>

## Git Commands
`git [명령어]` 형태이다.

### (1) `git init`
> Git으로 코드 관리를 시작한다.
* 코드 관리 단위(기준) : **폴더**
  * git 사용 시 가장 첫 번째 스텝은 폴더를 생성하거나 가져오는 것이다!
* `(master)`: ~~현재 브랜치명~~
* `.git` 폴더 생성 : Git의 관리와 관련된 파일
  * 리눅스에서 .이 앞에 붙은 디렉토리/폴더는 숨겨져있는 폴더이다.
  * ls -a 명령어를 사용하여 확인할 수 있다.
  * 이 파일 삭제 시, 더이상 git으로 관리되지 않는다.

<br>

### (2) `git status`
> Git 에게 현재 상태를 물어본다.

* 최초 상태 (Git init 직후)

    ```
    On branch main 
    -> main이라는 branch 위에 있음.

    No commits yet 
    -> commit이 아직 없음.

    nothing to commit (create/copy files and use "git add" to track) 
    -> commit할 것도 없음. (추적하려면 파일을 만들고 git add를 사용해.)

    ```

<br>

* `a.txt`파일 추가 후 상태 

    ```
    On branch main 

    No commits yet

    Untracked files: 
    (use "git add <file>..." to include in what will be committed)
        a.txt

    -> 추적되지 않은 파일이 있음.
    -> a.txt파일이 있는데, commit될 것에 포함시키려면 git add[파일명]을 사용해.

    nothing added to commit but untracked files present (use "git add" to track)

    -> commit할 것이 없지만 추적되지 않은 파일들은 있음. (git add 사용해.)

    ```

<br>

* `git add text.txt`직후
  
    ```
    On branch main

    No commits yet

    Changes to be committed: 
    (use "git rm --cached <file>..." to unstage)
        new file:   a.txt

    -> commit할 변화가 있음.
    -> stage에서 내리려면 git rm --cached [file]를 써.

    ```

<br>

* `git commit` 이후
  

    ```
    On branch main

    nothing to commit, working tree clean

    -> commit 할게 없음. 작업폴더 깔끔.

    ```

<br>

* 파일 수정 후
  ```

    On branch main
    Changes not staged for commit:

  -> Commit하기 위해 stage 되지 않은 변경 사항이 있음.

    (use "git add <file>..." to update what will be committed)
    (use "git restore <file>..." to discard changes in working directory)
        modified:   a.txt


  ```

<br>

### (3) `git add [파일/폴더]`
> commit을 위한 stage (사진 찍을 무대에 파일을 올린 것)
* 폴더에 변경사항이 있을 후 새로 커밋을 할 때, git은 이전 것과의 차이점을 인식한다. 따라서 이전 commit에서 변경사항이 없는 부분은 스테이지에 올리지 않아도 된다.
* `git add.` : 현재 폴더의 모든 변경사항 stage
* unstage : `git rm --cached [file]`를 사용한다.

<br>

### (4) `git commit -m "커밋 메세지"`
> commit == 버전을 생성(메세지와 함께 Versioning) == 현재상태의 스냅샷 촬영\
> 메세지는 주로 동사 혹은 목적어로 하는 것이 이후 보기 편하다.
* 처음으로 commit을 할 경우,
  ```
    Author identity unknown
    -> 작자미상

    *** Please tell me who you are.
    -> 당신이 누군지 알려주세요.

    Run
    -> 아래의 명령어를 실행주세요.
    git config --global user.email "you@example.com"
    git config --global user.name "Your Name"
  ```
    * mac의 경우, SSF활용
  
* `git config` 설정 후 (`vim`에디터 창)
  ```
    # Please enter the commit message for your changes.
    -> 변경사항에 대한 commit message를 입력해주세요.

    # Lines starting with '#' will be ignored, and an empty message aborts the
    commit.
    -> #로 시작하는 라인은 무시됩니다. 아무것도 없는 메시지는 종료됩니다.

    # On branch master
    #
    # Initial commit
    #
    # Changes to be committed:
    #   new file: a.txt
  
  ```

<br>

### (5) `git config`
> Git에 관한 설정 (configuration)
* `--global user.email "이메일"` : global(전역으로) user의 email을 설정
* `git config --global user.email` : 설정값 확인

<br>

### (6) `git log`
> 현재까지의 commit을 출력
* `git log` 출력화면
  ```
    commit 4d58fe915a210ce174d267fc0f8383d5eaea2740 (HEAD -> main)
    Author: Minseo Kim <lolz77@yonsei.ac.kr>
    -> 작성자

    Date:   Tue Sep 19 16:56:22 2023 +0900
    -> 날짜

        First commit
        -> 커밋 메세지

  ```
* `git log --oneline` : 한줄로 출력한다.
  ```
  4d58fe9 (HEAD -> main) first commit
  ```

<br>

### (7) `git remote`
* `git remote add [저장소이름] [저장소주소]` : git에게 원격저장소(remote) 추가(add)를 명령한다.

<br>

### (8) `git diff`
* 마지막 commit에서 무엇이 달라졌는지 물어보는 것

<br>

### (9) `git checkout`
> 포인터(head)를 바꾸는 행위
* `git checkout [commit했을때의 hash]` : 과거 커밋했을 때의 상태를 보여준다. 이 때 작업을 하는 것은 권장하지 않는다. 보고 다시 현재로 돌아와야 한다.
* `git checkout main` : 다시 main으로 (현재로) 돌아오는 것.
