use 한빛무역;

select *
from 사원;
/*ansi sql 형식 (미국 표준)  cross join 4 *10건 총 40건 */ 
 select  부서명,이름,부서.부서번호 from 부서 cross join 사원 where 이름='이소미';
 
 /*non-ansi sql */
  select  부서명,이름,부서.부서번호 
  from 부서,사원 
  where 이름='이소미';
  
  select *
  from 사원;  /*10건의 자료 */
  
  select *  /*부서번호 ,부서명 4건*/
  from 부서;
  /*ansi sql */
  select * 
  from 사원 
  inner join 부서
  on 사원.부서번호=부서.부서번호
  where 이름='이소미';
  
  /*non ansi sql */
  select * 
  from 사원,부서
  where 사원.부서번호=부서.부서번호 and 이름='이소미';
  
  select *
  from 고객
  inner join 주문
  on 고객.고객번호=주문.고객번호;
  
	select 고객.고객번호,담당자명,고객회사명,마일리지,count(*) as 주문건수
  from 고객
  inner join 주문
  on 고객.고객번호=주문.고객번호
  group by 고객.고객번호,담당자명,고객회사명,마일리지
  order by count(*) desc;
  
  select 고객.고객번호, 고객회사명,담당자명
  from 고객 
  inner join 주문
  on 고객.고객번호=주문.고객번호;
  
  /*고객과 주문 테이블을 먼저 이너조인 후 주문세부와 이너조인하여 세 테이블 연결*/
    select 고객.고객번호, 고객회사명,담당자명 ,sum(주문수량*단가) as 주문금액합계
  from 고객 
  inner join 주문
  on 고객.고객번호=주문.고객번호
  inner join 주문세부
  on 주문.주문번호=주문세부.주문번호
group by 고객.고객번호,고객회사명,담당자명;

select 고객번호,담당자명,마일리지,등급명,하한마일리지,상한마일리지
from 고객
cross join 마일리지등급;

/*위에것과 같은 의미 마일리지 등급의 모든 컬럼을 추출*/
select 고객번호,담당자명,마일리지,마일리지등급.*
from 고객
cross join 마일리지등급
where 담당자명="이은광";

select 고객번호,고객회사명,담당자명,마일리지,등급명
from 고객
inner join 마일리지등급
on 마일리지 between 하한마일리지 and 상한마일리지
where 담당자명='이은광';


/*LEFT, RIGHT,FULL(my sql에서는 full 지원x ->union사용해야함)*/
/*사원 테이블 (왼쪽)을 기준으로 부섵 테이블과 외부조인 */
select *
from 사원
left outer join 부서
on 사원.부서번호=부서.부서번호
where 성별="여";

select *
from 사원
right outer join 부서
on 사원.부서번호=부서.부서번호
;

select 부서명
from 사원
right outer join 부서
on 사원.부서번호=부서.부서번호 
where 사원.부서번호 is null;

select 이름,부서.부서번호,부서명
from 사원
left outer join 부서
on 사원.부서번호=부서.부서번호
where 부서.부서번호 is null;

/*셀프 조인 -사원번호,사원이름,상사의사원번호,상사의 이름 출력 */
select 사원.사원번호,사원.이름,상사.사원번호,상사.이름
from 사원
inner join 사원 AS 상사
on 사원.상사번호=상사.사원번호;


select 사원.이름, 사원.직위, 상사.이름 as '상사이름'
from 사원
left outer join 사원 as 상사
on 사원.상사번호 = 상사.사원번호
order by 상사.이름;

select 제품명,sum(주문세부.주문수량) as 주문수량합, 단가*주문수량합
from 제품
inner join 주문세부
on 제품.제품번호=주문세부.제품번호
group by 제품명;

select 제품명,sum(주문세부.주문수량) as 주문수량합 ,sum(주문세부.단가*주문세부.주문수량) as 주문금액합
 from 제품 
 inner join 주문세부 
 on 제품.제품번호=주문세부.제품번호 
group by 제품명;
