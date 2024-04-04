use 한빛무역;
select * from 고객;

select 고객번호,
		담당자명 as 담당자이름,
        마일리지 * 1.1 as "10%인상" from 고객;
        
select 고객번호,담당자명,도시,마일리지 from 고객 where 도시='서울특별시'
order by 마일리지 asc;


select 고객번호,담당자명,도시,마일리지 from 고객 where 도시='서울특별시'
order by 마일리지,도시명,담당자명 asc;
/*asc(오름차순)는 생략가능 내림차순은 desc order by에는 열 이름 대신 별명 or 컬럼 순서 넣을 수 있음)*/

select *
from 고객
limit 5;

select *
from 고객
order by 담당자명
limit 5;

select *
from 고객
order by 마일리지 desc
limit 10;

select *
from 고객;

select distinct 도시
from 고객; /* 중복을 제외한 도시들을 볼 수 있음*/

select 1+2 as 더하기,
1*2 as 곱하기,
5%3 as 나머지,
10 mod 3 as 나머지;

select 3>1;

select *
from 고객 
where (도시='서울특별시' or 마일리지>=1000) and 담당자직위 = '영업 사원';

select 고객번호,담당자명,주소,마일리지 from 고객 where 도시 = '부산광역시'
union
select 고객번호,담당자명,마일리지,도시 from 고객 where 마일리지<1000
order by 마일리지; 
/*추출하려는 열의갯수가 다르면 에러가 뜸 열의 종류가 다르면 위에 열들만 출력*/

select * from 고객;

select * from 고객 where 지역="";
select * from 고객 where 지역 is null;
/*
null은 알 수 없는 값, ""는 빈 문자열
csv데이터를 import해서 가져오면 빈 셀들이 공백으로 입력되서 넘어옴
n=null
변수가 준비되어 있는 상태. 값이 들어있다
바구니= 사과

바구니(변수)만 준비되어 있다.
바구니=null
바구니(변수)가 준비되어 있으며, 아무것도 없다.
바구니=""
그래서 바구니를 참조할때 바구니 is null 문장과 바구니=""는 다르다
*/
/* 변경: update 테이블명 set 열=값 where 조건식; */
update 고객 set 지역=null where 지역="";

select * from 고객 where 지역 is null;

/*담당자 직위가 영업 과장 또는 마케팅 과장 인 고객 자료 출력 in 연산자 활용*/
select * from 고객 where 담당자직위 in ('영업 과장','마케팅 과장');
/*마일리지가 5만 이상이면서 20만 이하인 고객 */
select * from 고객 where 마일리지 between 50000 and 200000;

/* like연산자 %: 문자 여러개, _: 문자 한개 */
/*" " 가 없으면 기본적으로 테이블이나 컬럼 명으로 인식*/
select * from 고객 where 도시 like "대전광역시";

select *
from 고객
where 도시 like "%광역시";

select *
from 고객
where 도시 like "%인천광%";


select * from 고객 where 도시 like '%광역시' and (고객번호 like'_C%' or 고객번호 like '__C%');