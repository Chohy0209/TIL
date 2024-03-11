# git 기초
 
 
## 개념
-  버전관리 프로그램  (*vcs version
  control system*)
    - 소스코드의 변화를 추적 하기 위한 도구
- **git 과 github의 차이**
    - git은 스냅샷(사진첩) github는 cloud
- **Open source**
  - git 에 존재하는 무료로 배포한 소스 코드
- **기본 git 작동 구조**
  - **working Dirdctory**
    - 파일의 수정 생성등을 하는 파일로 분장실과 같은 공간
  - **stage** 
    - 수정된 파일을 commit 하기 전 add 시키는 공간으로 촬영 스테이지와 같은 공간
  - **commit**
    - stage에 위치한 파일등을 commit 시켜주는 것으로 사진과 같은 역할
- **repository(저장소)**
 - 파일을 git에 관리를 받는 프로그램으로 변환한 상태. 
 `git init` 명령어로 파일을 감싸서 *repository*상태로 만든 후 작업

## git 명령어
$는 터미널이 준비됐다는 것을 뜻함.

- `$ git init`:directory를 repository 형태로 바꿔줌

- `$ git config --global user.name 'NAME'` : git을 등록해 사용할 때 github의 user name를 등록하는 명령어

- `$ git config --global user.email 'EMAIL` :
    git을 등록해 사용할 때 github의 email을 등록하는 명령어

- `$ git add <file>` : file을 stage에 올리는 명령어
  
- `$ git commit -m 'MESSAGE'` : stage에 있는 file을 commit 해주는 명령어

- `$ git log --oneline` : 지금까지 실행된 커밋의 로그를 보여줌 

- `$ git status` : 현재 파일들의 add, commit 등의 상태를 보여줌

- `$ git remote add origin 'URL'` : github에 원격 저장소 생성후 URL 을 획득하고 연결시킴 

- `$ git push origin master` : commit 된 git을 github 원격 저장소로 push 시킴 origin은 remote add 로 설정한 URL의 name과 같아야함

- `$ git clone 'URL'` : github 내의 오픈소스로 공개되어 있는 소스코드를 clone으로 내 컴퓨터로 가져와서 실행 할 수 있는 명령어
 