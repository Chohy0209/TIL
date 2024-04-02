INSERT INTO Person(id,name,Birthday) -- id는 기본키,not null
VALUES (1,"홍길동","1997-01-02");
INSERT INTO PERSON VALUES(2,"임꺽정","1999-01-01");

DELETE FROM Person;

UPDATE person set name="세종";

SELECT * From Person;

-- INSERT INTO Person(name,birthday) values ("김길동","1985-01-02"),("이길동", "1995-02-17")