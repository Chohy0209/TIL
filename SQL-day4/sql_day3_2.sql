use 한빛무역;

select 고객번호, 담당자명, 마일리지, 도시 
from 고객 
where 도시 = '부산광역시' or 마일리지 < 1000 
order by 고객번호;

select 고객번호, 담당자명, 마일리지, 도시 
from 고객 
where 도시 = '부산광역시'
union
select 고객번호, 담당자명, 마일리지, 도시 
from 고객 
where 마일리지 < 1000;
/*도시 = '부산광역시' or 마일리지 < 1000 */

select 담당자명, 마일리지, 도시, 주소
from 고객 
where 도시 = '부산광역시'
union
select 담당자명, 마일리지, 도시, 주소
from 고객 
where 마일리지 < 1000
order by 마일리지;

select * from 고객;

select * from 고객 where 지역 = "";
select * from 고객 where 지역 IS NULL;
/*NULL은 알 수 없는 값, ""는 빈 문자열*/

/* CSV(비어있는 셀에는 "" 빈문자열이 저장) -> 테이블로 import 

n=null
바구니(변수)가 준비되어 있는 상태, 사과(값)가 들어있다
바구니=사과
바구니(변수)만 준비되어 있다
바구니=null
바구니(변수)가 준비되어 있으며, 아무것도 없다(먹어서 없는것인지, 원래 없던것인지는 모름)
바구니=""
그래서 바구니를 참조할때
바구니 IS NULL 문장과 바구니=""는 다르다.

/*고객 테이블에서 지역이 빈 문자열이면 모두 NULL로 변경하시오*/
/* 변경 : UPDATE 테이블명 SET 열 = 값 WHERE 조건식; */
UPDATE 고객
SET 지역 = NULL
WHERE 지역 = "";

select * 
from 고객
WHERE 지역 IS NULL;

select * from 고객 WHERE 지역="";
UPDATE 고객
SET 지역 = NULL
WHERE 지역 = "";

/*update시 에러 발생 -> safe mode 해제(edit->preferences->sql editor)
-> safe updates 항목 체크 해제! -> workbench 재 시작*/
use 한빛무역;

UPDATE 고객
SET 지역 = NULL
WHERE 지역 = "";

select * from 고객 WHERE 지역="";

/*담당자직위가 '영업 과장' 또는 '마케팅 과장'인 고객 자료 출력*/
select * from 고객 
where 담당자직위='영업 과장' or 담당자직위='마케팅 과장';

select * from 고객 
where 담당자직위 in ('영업 과장', '마케팅 과장');

/* 마일리지가 5만점 이상 20만점 이하인 고객을 추출하시오. */
select *
from 고객
where 마일리지 >= 50000 and 마일리지 <= 200000;

select *
from 고객
where 마일리지 between 50000 and 200000;

/* %:문자 여러개, _:문자 한개 */
select *
from 고객
where 도시 like "대전광역시";
/* like만 사용된 경우에는 =기호와 같은 의미
select *
from 고객
where 도시 = "대전광역시";

/* %:문자 여러개, _:문자 한개 */

select *
from 고객
where 도시 like "%광역시";

select *
from 고객
where 도시 like "%광역%";

select *
from 고객
where 도시 like "%천광%";

select *
from 고객
where 도시 like "%인천%";

select *
from 고객
where 도시 like "__특%";


select *
from 고객
where 도시 like "__광%";

/* 주소 중에서 '중구'에 해당되는 자료를 모두 추출하시오.*/
select * from 고객
where 주소 like '%중구%';

/* 도시가 '광역시'이면서 고객번호의 2번째 또는 3번째 글자가 'C'인 고객 정보 추출 */

select * from 고객
where 도시 like  '%광역시'
and (고객번호 like  '_C%' or 고객번호 like  '__C%');

/* 1번 */
select * from 고객
where 도시 like '서울%'
and 마일리지 between 15000 and 20000;

/* 2번 */
select distinct 지역, 도시 from 고객
order by 1,2;

/* 3번 */
select * from 고객
where 도시 in('춘천시', '과천시', '광명시')
and (담당자직위 like '%이사%' or 담당자직위 like '%사원%');

/* 4번 */
select * from 고객
where not(도시 like '%광역시' or 도시 like '%특별시')
order by 마일리지 desc
limit 3;

/* 5번 */
select * from 고객
where 지역 is not null
and 담당자직위 <> '대표 이사';












