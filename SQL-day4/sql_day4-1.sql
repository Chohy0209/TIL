use 한빛무역;
select 담당자명,도시,마일리지 from 고객 where 도시='대전광역시';


/*집계함수 : select 집계함수 from 테이블명 where 조건절 */
select sum(마일리지) from 고객 where 도시='대전광역시';

select * from 고객;

/*데이터의 전체 건수 카운트 */
select count(*) from 고객;

select count(고객번호) from 고객; /*결과 96건 */
/*카운트 함수에서는 null을 카운트 하지않기때문에 27이 뜸 */
select count(지역) from 고객;

select sum(마일리지),avg(마일리지),min(마일리지),max(마일리지) from 고객;

select sum(마일리지),max(마일리지),min(마일리지),avg(마일리지) from 고객 where 도시='서울특별시';

/*group by절: 그룹별로 묶어서 요약 */
/* select 그룹으로 묶을 열, 집계함수
from 테이블명
where 조건절
group by 그룹으로 묶을 열(번호)
*/
/*도시 단위로 그룹화 ->그룹별 마일리지의 합계 */

/*담당자 직위별로 그룹화, 같은 담당자 직위에 대해서 도시별로 그룹하 -> 집계함수 -> 집계*/
select 담당자직위,도시 , avg(마일리지) as 평균마일리지, count(*) as 고객수 from 고객 group by 담당자직위,도시;
 
 select 담당자직위, 도시, count(*) as 고객수
from 고객
where 담당자직위 like '%마케팅%'
group by 담당자직위, 도시;

/* with rollup : 그룹별 소계, 전체 총계 구하고자할때 사용, group by 다음에 기술 */
select 도시, count(*) as 고객수,
		avg(마일리지) as 평균마일리지
from 고객
where 지역 is null
group by 도시
with rollup;

/* having 절 : group by에 대한 조건 */
/*
select 그룹으로 묶을 열, 집계함수
from 테이블명
[where 조건절]
group by 그룹으로 묶을 열(번호)
[having 절];
*/

select 도시, count(*) as 고객수, avg(마일리지) as 평균마일리지 
from 고객 group by 도시
having 고객수 >= 3;

/* 도시 단위로 그룹화 -> 그룹별 마일리지의 합계*/
select 도시, count(*) as 고객수, sum(마일리지) as 마일리지합계, avg(마일리지) as 마일리지평균
from 고객
group by 1;
/*각 도시별 '고객수' 열을 추가 */