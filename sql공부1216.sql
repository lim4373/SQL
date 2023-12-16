SELECT productName, max(quantityinstock)
from products
group by productName;


select *
from products;


SELECT productName, max(quantityinstock)
from products
group by productName
HAVING max(quantityInStock) >= 6000;

SELECT productName, max(quantityinstock)
from products
group by productName with rollup;


select length("afsdfasdfsdafsdafasdf");

select concat("my","sql","en sourcre");

select locate("abc","abcabcabcabcabc");

select left("my sql easy",5);


select right("my sql easy",6);

select lower("afsdfasdfsdafsdafasdf");

select upper("afsdfasdfsdafsdafasdf");

select replace("mysql","my","ms");

-- trim() 문자열의 앞이나 뒤, 또는 양쪽 모두에 있는 특정 문자를 제거

select trim('                       mysql                      '),
trim(LEADING '#' from '###mysql##'),
trim(TRAiLING "#" FROM "###mysql##");

SELECT FORMAT(12345,6789,3);

SELECT sqrt(4),pow(2,3),exp(3),log(3);
-- abs(): 절대값, rand(): 무작위 값, floor: 내림, ceil():올림,round(): 반올림
select abs(-3),rand(),round(rand()*100,0),floor(11.01),ceil(11.01),round(-10.5);


