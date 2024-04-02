INSERT into customer(c_id,c_name,c_addr,c_phone)
VALUES(1,"최길동","서울시","010-1234-5678");
INSERT INTO customer VALUES(2,"임꺽정","성남시","1999-01-01");

SELECT * FROM customer;
UPDATE customer SET c_name="김규동" WHERE c_id=2;

DELETE from customer WHERE c_id=2;