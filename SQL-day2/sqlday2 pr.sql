INSERT into customer(c_id,c_name,c_addr,c_phone)
VALUES ("1","김수동","성남시 분당구", "010-1234-5934")
INSERT into customer(c_id,c_name,c_addr,c_phone)
VALUES("2","김길동","서울시 중랑구","010-4858-2945")

update customer set c_name="김지참" where c_id=2

select c_id,c_name,c_phone As "전화번호" from customer where c_id>1; 
delete from customer where c_id <2