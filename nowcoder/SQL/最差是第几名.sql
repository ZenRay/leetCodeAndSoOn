
/*
描述
班的每个人的综合成绩用A,B,C,D,E表示，90分以上都是A，80~90分都是B，70~80分为C，60~70为D，E为60分以下
假设每个名次最多1个人，比如有2个A，那么必定有1个A是第1名，有1个A是第2名(综合成绩同分也会按照某一门的成绩分先后)。
每次SQL考试完之后，老师会将班级成绩表展示给同学看。
现在有班级成绩表(class_grade)如下:

grade	number
A	2
C	4
B	4
D	2

第1行表示成绩为A的学生有2个
.......
最后1行表示成绩为D的学生有2个



老师想知道学生们综合成绩的中位数是什么档位，请你写SQL帮忙查询一下，如果只有1个中位数，输出1个，如果有2个中位数，按grade升序输出，以上例子查询结果如下:
grade
B
C

解析:
总体学生成绩排序如下:A, A, B, B, B, B, C, C, C, C, D, D，总共12个数，取中间的2个，取6，7为:B,C


drop table if exists class_grade;
CREATE TABLE class_grade (
grade varchar(32) NOT NULL,
number int(4) NOT NULL
);

INSERT INTO class_grade VALUES
('A',2),
('C',4),
('B',4),
('D',2);
*/



/* === 解答思路 ==== 
中位数的特点是大于上50%，小于下50%。该需求是需要进行定位。因此将总数据量的一半分别，和正向排序、逆向排序进行比较
*/

WITH temp AS(
SELECT
    grade
    ,number
    ,SUM(number) OVER(ORDER BY grade) AS t_rank_asc
    ,SUM(number) OVER(ORDER BY grade DESC) AS t_rank_desc
    ,SUM(number) OVER() AS total
FROM class_grade
)

SELECT
    grade
FROM temp
WHERE t_rank_asc >= total / 2
    AND t_rank_desc >= total / 2

ORDER BY 1