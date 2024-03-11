# Unix 명령어
유닉스에서 사용 가능한 명령어 집합 모음.
## 명령어 기초
### 기본 조작
- `$` : 현재 명령어를 받을 준비가 되었다 + **터미널 명령어**다.
- `ctrl + c` : 취소 (*cancle*)
- `ctrl + l` : 클리어 (*clear*)
- `tab` : 자동 완성
  
### 명령어들
- `touch` : 파일 생성
- `ls` : 현재 폴더의 내용물을 보여줌(*list*)
- `ls -a` : 현재 폴더의 내용물을 **모두** 보여줌 (*-a all*)
- `rm` : 파일 삭제 (*remove*)
- `rm -r` : **파일/폴더 모두** 삭제 (*-r recursibely*)
- `rm-rf` : **파일/폴더 모두** 강제 삭제 (*-f force*)
- `pwd` : 현재 작업 폴더 = 내위치(*Present Working Directory*)
- `mkdir` : 폴더 생성 (*make directory*)
- `rmdir` : ~~빈 폴더 삭제 (*remove directory*)~~
- `cd` : 폴더 이동 (*change directory*)
- `cp` : 파일 복사 (*cppy*)
- `cp. -r` : **파일/ 폴더**
- `mv`: **파일/폴더** 이동+ 이름 바꾸기

### 경로 관련
- `.` : 현재 폴더
- `..` : 상위 폴더
- `~` : *home dir*
- `/` : *root dir*
- `.xxx`:`.` 으로 시작 > 숨김파일 / 폴더