/*
서브쿼리(subquery) : sql내부에서 사용되는 select문 괄호안에 기술 , 복잡한 데이터 추출
서브쿼리가 먼저 실행된 후 메인 쿼리 실행
select *
from 테이블명
where 컬럼=(select 컬럼명 from 테이블명);
*/
use 한빛무역;
select 고객번호,담당자명,마일리지
from 고객
where 마일리지=(select max(마일리지) from 고객);

select 고객회사명, 담당자명
from 고객
where 고객번호=(select 주문.고객번호 from 고객 inner join 주문 on 고객.고객번호=주문.고객번호 where 주문.주문번호='H0250');


select 고객회사명, 담당자명 from 고객
left outer join 주문
on 고객.고객번호 = 주문.고객번호
where 주문번호 = (select 주문번호 from 주문 where 주문번호 = 'H0250');

select 고객회사명, 담당자명
from 고객
where 고객번호 = (select 고객번호 from 주문 where 주문번호='H0250');

SELECT 고객회사명, 담당자명
FROM 고객
INNER JOIN 주문
ON 고객.고객번호 = 주문.고객번호
WHERE 주문번호='H0250';

select *
from 고객
where 마일리지>(select min(마일리지) from 고객 where 도시='부산광역시');

/*부산광역시 고객의 전체 주문건수를 출력 subquery 값이 한개가 아닐경우 in 사용하면 결과가 나옴*/
select count(*) as 주문건수
from 주문
where 고객번호 in (select 고객번호
from 고객
where 도시='부산광역시')
;
/*부산광역시 전체 고객의 마일리지 추출 */
select 마일리지
from 고객
where 도시 in (select 도시 from 고객 where 도시='부산광역시');

/* any : 서브쿼리의 각 결과에 대해 비교했을때 최소 1건 이상 조건이 만족되는 자료를 추출 <- 부산광역시에 해당하는 고객에 대한 마일리지가 추출되고 그 결과랑 비교해 최소 한건이상의 결과보다 큰 고객의 마일리지 추출*/
select *
from 고객
where 마일리지 > any(select 마일리지 from 고객 where 도시='부산광역시');


select avg(마일리지)
from 고객
group by 지역;

/*any: 여러 개 중에 적어도 1 개이상 조건에 부합되면 추출*/
/*all: 여러 개 모두에 대해 조건에 부합되면 추출*/

select *
from 고객
where 마일리지> all(select avg(마일리지) from 고객
group by 지역);

/* 고객 중에서 최소 1번 이상 주문한 적이 있다면 해당 고객의 정보 추출 (in 연산자 사용) */

select *
from 고객
where 고객번호 in (
select 고객번호 
from 주문);
 
 /*해당 데이터가 있다면 추출*/
select *
from 고객
where exists (
select 고객번호 
from 주문
where 고객번호=고객.고객번호);

select distinct 고객회사명
from 고객
inner join 주문
on 고객.고객번호=주문.고객번호;


select avg(마일리지) as 도시별평마,도시
from 고객
group by 도시
having avg(마일리지)> 
(select avg(마일리지)
from 고객)
;

/* DML : 데이터 조작어 */
select *
from 부서;
/* 부서번호: A5,부서명: 마케팅부 추가 */
insert into 부서
values('A5','마케팅부');

select *
from 부서;

insert into 제품
values(999,'맛동산',1500,10); /*포장단위 누락 ->컬럼의 개수가 맞지않아 에러 발생*/


insert into 제품
values(999,'맛동산',null,1500,10); /*포장단위 누락 ->컬럼의 개수가 맞지않아 에러 발생*/

select * from 제품;
/*이런식으로 열을 명시해줘서 할 수 있음 기본키로 설정된 열은 null값이 있을 수 없음 실질적인 값이 들어있어야함*/
insert into 제품(제품번호,제품명,단가,재고)
values(998,'새우깡',2000,50); 

insert into 사원(사원번호, 이름, 직위, 성별, 입사일)
values('E20', '홍길동', '수습사원', '남', CURDATE());

select * from 사원;
insert into 사원(사원번호, 이름, 직위, 성별, 입사일)
values('E23', '임꺽정', '수습사원', '남', CURDATE()),
('E24', '신사임당', '수습사원', '여', CURDATE());

SELECT * FROM 사원;

/* update : 데이터를 변경 
update 테이블명
set 컬럼 = 값, 컬럼=값
where 조건 */

UPDATE 사원
SET 이름 = '김소미'
WHERE 사원번호='E01';


insert into 제품 (제품명,제품번호,단가,재고)
values('고래밥',111,2500,40);

update 제품
set 제품명='상어밥'
where 제품명=고래밥;
select * from 제품;

update 제품
set 단가=단가*1.1
where 제품명='새우깡';

update 제품
set 재고=재고+10
where 제품명='맛동산';

select * from 제품;

/*delete from 테이블명 where 조건 where 조건 안쓸 시 테이블 전체 삭제*/
delete from 제품 where 제품번호=999;
select * from 제품;

delete from 사원 order by 입사일 DESC limit 3;
select * from 사원 order by 입사일 DESC ;

/*데이터 추가시 이미 데이터가 있으면 값을 변경하고, 없으면 데이터를 추가 */
insert into 부서(부서번호, 부서명)
values('A1','총무부');  /*에러가 남 기본키가 중복되기 때문*/

insert into 부서(부서번호, 부서명)
values('A1','총무부')
on duplicate key update
부서명='총무부';
select * from 부서;

/* select 문 수행 결과를 다른 테이블에 추가 
insert in to 테이블명(컬럼1,컬럼2,--)
select 컬럼1,컬럼2,...
from 테이블명
where 조건;
예시
insert into 고객(고객번호,담당자명,주소,마일리지)
select 고객번호,담당자명,주소,마일리지
from 고객2
where 주소="서울특별시";
고객2 테이블에서 주소가 서울 특별시인 고객의 고객번호,담당자명,주소,마일리지를 각각 추출하여
고객테이블의 고객번호,담당자명,주소,마일리지열에 추가
*/

/*테이블 만들기 */
create table 고객2
(
고객번호 char(5) primary key,
담당자명 varchar(20),
주소 varchar(50),
마일리지 int);

select * from 고객2;
insert into 고객2(고객번호,담당자명,주소,마일리지)
values('aaaaa','홍길동','서울특별시',50000);
select * from 고객2;

insert into 고객(고객번호,담당자명,주소,마일리지)
select 고객번호,담당자명,주소,마일리지
from 고객2
where 주소="서울특별시";

select * from 고객;

insert into 고객2(고객번호,담당자명,주소,마일리지)
values('BBBBB','임꺽정','광주광역시',10000);

delete from 고객2 where 고객번호='aaaaa';

insert into 고객(고객번호,담당자명,주소,마일리지)
select 고객번호,담당자명,주소,마일리지
from 고객2;
select* from 고객;

delete from 고객 where 고객번호='aaaaa';

select * 
from 제품
where  제품번호 not in
 (select 주문세부.제품번호
from 주문세부 where 주문세부.제품번호=제품.제품번호)
;

insert into 제품(제품번호,제품명,포장단위,단가,재고)
values(95,'망고베리 아이스크림','400g',800,30);

select * from 주문;

select 고객.담당자명, 고객.고객회사명,count(*) as 주문건수,max(주문일) as 최종주문일, min(주문일) as 최초주문일
from 주문 inner join 고객 on 고객.고객번호=주문.고객번호
group by 주문.고객번호
;

insert into 제품(제품번호,제품명,단가)
values(96,"눈꽃빙수맛 아이스크림",2000)
;
update 제품 set 재고=30 where 제품번호=96 ;
select 사원.부서번호 from 사원 inner join 부서 on 부서.부서번호=사원.부서번호;

delete from 부서 where 부서.부서번호 not in (select distinct 사원.부서번호 from 사원 left outer join 부서 on 부서.부서번호=사원.부서번호);

DELETE FROM 부서
WHERE NOT EXISTS (
    SELECT 1
    FROM 사원
    LEFT OUTER JOIN 부서 ON 부서.부서번호 = 사원.부서번호
    WHERE 부서.부서번호 = 부서.부서번호
);
select * from 부서;