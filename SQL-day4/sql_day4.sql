use 한빛무역;
select char_length("hello"),
char_length("반갑습니다"),
length("hello"),
length("반갑습니다");

select concat("반갑습니다","안녕하세요", "잘가세요"),
concat_ws("-","반갑습니다","안녕하세요", "잘가세요");

select left("ai 서비스 개발", 5),
right("ai 서비스 개발", 5),
substr("ai 서비스 개발",2, 4),
substr("ai 서비스 개발",2);

/* 왼쪽에서 2번째 공백 이후를 모두 제거 */
select substring_index("서울특별시 강남구 역삼동"," ", 2);
select substring_index("강북구강남구영등포구","구", 2);

/* 오른쪽에서 2번째 공백 이전을 모두 제거 */
select substring_index("서울특별시 강남구 역삼동"," ", -2);

/* 특정 문자로 채우기 */
select lpad('sql', 5, "#");
select rpad('sql', 5, "#");

/* 공백 제거 */
select ltrim("   sql     ");
select rtrim("   sql     ");
select trim("   sql     ");

/* 양쪽, 왼쪽, 오른쪽 동일 문자열 제거 */
select trim(both "ab" from "ababcdab");
select trim(leading "ab" from "ababcdab");
select trim(trailing "ab" from "ababcdab");

/* field(찾고자하는문자열, 문자열1,...) */
select field("java", "sql", "java", "c");
select find_in_set("java", "sql,java,c");

/*instr(문자열, 찾고자하는문자열)
locate(찾고자하는문자열, 문자열)*/
select instr("네 인생을 살아라", "인생");
select locate("인생", "네 인생을 살아라");

/* elt(찾을문자열위치, "문자열1",...) */
select elt(2 , "sql", "java", "c");

/* 문자열 반복 함수 repeat(문자열, 횟수) */
select repeat("ㅋ",10);

/* 문자열 치환 함수 replace("문자열", "원래문자열", "바꿀문자열") */
select replace("010.1234.5678", ".", "-");

/* 문자열 뒤집기 reverse("문자열") */
select reverse("abcd");

/* 자릿수 지정 함수 */
select ceiling(123.36); /*올림*/
select floor(123.56); /*버림*/
select round(123.36); /*반올림*/
select round(123.356, 2); /*반올림*/
select truncate(123.56, 1); /* 버림 */

select abs(-3);
select abs(3);
select sign(-3);
select sign(3);

select mod(10, 4);
select 10 % 4;
select 10 mod 4;

select power(2,3);
select sqrt(9);
select rand();
select rand(20240405);/* seed */

select round(rand()*2); /* 0 <= rand() < 1 */

select now(); /*select sysdate();*/
select curdate();
select curtime();

select year(now()), 
month(now());
select quarter(now()); /*분기*/
select hour(now());
select minute(now());
select day(now());

select datediff('2024-05-01', '2024-04-05'); /*datediff(끝일자, 시작일자)*/
select datediff('2024-04-05','2024-05-01'); 
select timestampdiff(day,now(),'2024-04-30'); /* 단위, 시작, 끝*/
select timestampdiff(month,now(),'2024-12-31'); /* 단위, 시작, 끝*/
select timestampdiff(year,now(),'2025-12-31'); /* 단위, 시작, 끝*/

select adddate(now(), 20);
select adddate(now(), interval 20 day);
select adddate(now(), interval 20 month);
select adddate(now(), interval 20 hour);

select subdate(now(), interval 20 day); /*이전*/

select last_day(now()); /* 현재 월의 마지막 일자 */
select dayofyear(now()); /* 올해 며칠이 경과일 */
select weekday(now()); /* 요일 */

/* 데이터 형 변환 : cast(값 as 변환타입), convert() */
select cast('1' as unsigned); /* 문자 '1' -> 부호없는숫자 */
select cast('1' as signed); /* 문자 '1' -> 부호있는숫자 */
/*
1byte = 8bit => 1bit:부호(0 또는 1), 7bit:숫자
7bit = -128...0, ...127
1byte = 8bit =>8bit:숫자 = 0 ~ 255

4byte 공간 숫자를 저장
*/

select cast(1 as char(1)); /* 숫자 1 -> 문자 1 */
select convert(1, char(1)); /* 숫자 1 -> 문자 1 */

/* if(조건식, 참, 거짓) */
select if(1+2 > 0, '양수', '음수');

select ifnull(null, 0); /* 0 */
/* ifnull함수의 1번째 인수가 null이 아니면 1번째 인수가 리턴,
1번째 인수가 null이면 2번째 인수가 리턴 */
select ifnull(5, 10);
select ifnull(null, 10);

select nullif(3,5); /* 두 값이 같으면 null, 다르면 1번째 인수가 리턴*/
/* when 조건1 then 값1 when 조건2 then 값2 ... */
select case when 100*2 > 150 then "합격"
when 100*2 > 500 then "불합격"
else "재시험"
end;









