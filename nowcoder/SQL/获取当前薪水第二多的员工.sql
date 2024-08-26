
/*
描述
有一个员工表employees简况


有一个薪水表salaries简况


drop table if exists  `employees` ; 
drop table if exists  `salaries` ; 
CREATE TABLE `employees` (
`emp_no` int(11) NOT NULL,
`birth_date` date NOT NULL,
`first_name` varchar(14) NOT NULL,
`last_name` varchar(16) NOT NULL,
`gender` char(1) NOT NULL,
`hire_date` date NOT NULL,
PRIMARY KEY (`emp_no`));
CREATE TABLE `salaries` (
`emp_no` int(11) NOT NULL,
`salary` int(11) NOT NULL,
`from_date` date NOT NULL,
`to_date` date NOT NULL,
PRIMARY KEY (`emp_no`,`from_date`));
INSERT INTO employees VALUES(10001,'1953-09-02','Georgi','Facello','M','1986-06-26');
INSERT INTO employees VALUES(10002,'1964-06-02','Bezalel','Simmel','F','1985-11-21');
INSERT INTO employees VALUES(10003,'1959-12-03','Parto','Bamford','M','1986-08-28');
INSERT INTO employees VALUES(10004,'1954-05-01','Chirstian','Koblick','M','1986-12-01');
INSERT INTO salaries VALUES(10001,88958,'2002-06-22','9999-01-01');
INSERT INTO salaries VALUES(10002,72527,'2001-08-02','9999-01-01');
INSERT INTO salaries VALUES(10003,43311,'2001-12-01','9999-01-01');
INSERT INTO salaries VALUES(10004,74057,'2001-11-27','9999-01-01');


请你查找薪水排名第二多的员工编号emp_no、薪水salary、last_name以及first_name，不能使用order by完成，以上例子输出为:
（温馨提示:sqlite通过的代码不一定能通过mysql，因为SQL语法规定，使用聚合函数时，select子句中一般只能存在以下三种元素：常数、聚合函数，group by 指定的列名。如果使用非group by的列名，sqlite的结果和mysql 可能不一样)
emp_no 
salary
last_name	first_name
10004	74057	Koblick	Chirstian



*/


/* === 解答思路 1==== 
在不进行排序情况下，获取第二高的 salary——那么比第二高的薪水只有一个。
解答的思路是薪水表自关联且关联条件为薪水比较，只要薪水高的员工数量只有一个的员工那么即是第二个
*/


SELECT
    t1.*

    ,t2.last_name
    ,t2.first_name
FROM (
    -- 获取比最高薪水高的员工只有一个的信息
    SELECT
        t1.emp_no
        ,t1.salary
    FROM salaries t1
    JOIN salaries t3
        ON t3.salary > t1.salary
    GROUP BY 1, 2

    HAVING COUNT(t3.emp_no) =1
) t1
LEFT JOIN employees t2
    ON t2.emp_no = t1.emp_no

;


/* === 解答思路 2=== 
在不进行排序情况下，获取第二高的 salary——那么比第二高的薪水只有一个。
排除掉最高薪水后的表中最高薪水即为第二高
*/


SELECT
    t1.emp_no
    ,t1.salary
    ,t2.last_name
    ,t2.first_name
FROM salaries t1
JOIN employees t2
    ON t2.emp_no = t1.emp_no
WHERE t1.salary = (
    -- 获取到具体的第二高薪水
    SELECT
        MAX(salary) salary
    FROM salaries
    WHERE salary < (
        SELECT
            MAX(salary) salary
        FROM salaries
    )
)
;