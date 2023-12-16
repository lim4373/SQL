use my_exam;
/* -------------- EXAM    ---*/ 
DROP TABLE My_REPORT;

create table  My_REPORT(
name varchar(10), 
color varchar(10), 
sales int);
 

insert into My_REPORT values ('shoes', 'Red', 5200);
insert into My_REPORT values ('Wallet', 'White', 3800);
insert into My_REPORT values ('shoes', 'Red', 5100);
insert into My_REPORT values ('shoes', 'Black', 4600);
insert into My_REPORT values ('Wallet', 'Black', 3900);
insert into My_REPORT values ('Wallet', 'White', 4000);
insert into My_REPORT values ('shoes', 'Red', 5200);

SELECT * FROM MY_REPORT;


-- Q3. 다음과 같이 그룹핑하자.
select name, sum(sales)
from My_REPORT group by name;
 
 -- Q4. 다음과 같이 그룹핑하자.
select name, color, sum(sales) 
from My_REPORT group by name, color;

-- Q5. 다음과 같이 출력 해보자.  
select name, sum(sales) 
from My_REPORT group by name with rollup;


-- Q6. 다음과 같이 출력 해보자.  
select name, color, sum(sales) 
from My_REPORT group by name, color;

-- Q7. 다음과 같이 출력 해보자
select name, color, sum(sales) 
from My_REPORT group by name, color with rollup;

-- 08. sales 값이 150 이상의 데이터만을 대상으로 그룹화하고, 그룹별로 sale  평균를 리턴하되  200 이상 만 출력하자. 
select NAME, avg(sales) as average 
from My_REPORT 
where sales >= 150 
group by NAME 
having average >= 200;