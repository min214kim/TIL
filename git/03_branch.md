# branch
## 개념
* synchronous : 동기적 - 하나가 끝나야 다음이 시작된다.
* Asynchronous : 비동기적 - 하나가 끝나지 않아도 다음이 시작될 수 있다.
* 비동기성을 위해, 하나의 시간라인을 두는 것이 아닌 여러 개가 같이 시작될 수 있도록 하는 것이 branch의 개념이다.
* ex) main 도 하나의 branch 이다.

## 명령어
* `git branch [새로운 브랜치명]` : 새 branch를 만든다.
  * 새 브랜치 만들고 커밋을 해주면 main에서는 commit내용아 반영되지 않고, 새 브랜치에서만 반영된다.
* `git branch `: branch를 조회한다.
* `git checkout [branch명]`: 현재 포인터(head)를 특정 branch로 바꾼다. 
* ex) new 라는 branch 만들고 `checkout new`라고 가면 head pointer가 바뀐다!
  * `git log `시 확인 가능하다. 
    ```
    (base) minseo@gimminseoui-MacBookPro branch % git log --oneline
    5a82c89 (HEAD -> new) Add c.txt
    4d1cbe2 (main) Add b.txt
    0e9225e Add a.txt
    ```
<br>

## branch 병합
1. 주체가 되는 브랜치로 head를 이동한다. (어디에 병합할 것인지)
2. 병합하고자 하는 branch에 `git merge [병합하고자 하는 branch]` 명령어를 사용한다.
  * ex) main 에 new를 병합할 때, 
    * git checkout main
    * git merge new
### branch의 종류
  * fast forward branch 
    * 새 브랜치에만 변경사항이 있어서 병합시 그냥 이전 브랜치가 새 브랜치로 옮겨지기만 하면 되는 경우 
  
  * main, new 모두에서 변경사항이 있으 경우 
    * 겹치거나 충돌하는게 없다면 깔끔하게 merge가 된다.
      * 생활코딩 참고~~

