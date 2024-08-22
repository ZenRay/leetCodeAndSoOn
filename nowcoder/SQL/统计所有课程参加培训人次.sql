
/*
某公司员工培训信息数据如下：
员工培训信息表cultivate_tb(info_id-信息id,staff_id-员工id,course-培训课程)，如下所示：
注：该公司共开设了三门课程，员工可自愿原则性培训0-3项，每项课程每人可培训1次。


输入：
drop table if exists  `staff_tb` ; 
CREATE TABLE `staff_tb` (
`staff_id` int(11) NOT NULL,
`staff_name` varchar(16) NOT NULL,
`staff_gender` char(8) NOT NULL,
`post` varchar(11) NOT NULL,
`department` varchar(16) NOT NULL,
PRIMARY KEY (`staff_id`));
INSERT INTO staff_tb VALUES(1,'Angus','male','Financial','dep1'); 
INSERT INTO staff_tb VALUES(2,'Cathy','female','Director','dep1'); 
INSERT INTO staff_tb VALUES(3,'Aldis','female','Director','dep2'); 
INSERT INTO staff_tb VALUES(4,'Lawson','male','Engineer','dep1'); 
INSERT INTO staff_tb VALUES(5,'Carl','male','Engineer','dep2'); 
INSERT INTO staff_tb VALUES(6,'Ben','male','Engineer','dep1'); 
INSERT INTO staff_tb VALUES(7,'Rose','female','Financial','dep2'); 

drop table if exists  `cultivate_tb` ;   
CREATE TABLE `cultivate_tb` (
`info_id` int(11) NOT NULL,
`staff_id` int(11) NOT NULL,
`course` varchar(32) NULL,
PRIMARY KEY (`info_id`));
INSERT INTO cultivate_tb VALUES(101,1,'course1,course2');
INSERT INTO cultivate_tb VALUES(102,2,'course2');
INSERT INTO cultivate_tb VALUES(103,3,'course1,course3');
INSERT INTO cultivate_tb VALUES(104,4,'course1,course2,course3');
INSERT INTO cultivate_tb VALUES(105,5,'course3');
INSERT INTO cultivate_tb VALUES(106,6,NULL);
INSERT INTO cultivate_tb VALUES(107,7,'course1,course2');

解释：course1课程共有员工1、3、4、7共4名员工培训；
course2课程共有员工1、2、4、7共4名员工培训；
course3课程共有员工3、4、5共3名员工培训；

输出：
staff_nums
11

*/


/* === 解答思路==== 
从上面的结果来看，是按照课程和员工来统计次数，course 已经是合并课程信息了。因此结果
转换为统计course 内的信息即可。MySQL 没炸裂函数因此需要寻求其他方案，那么按照 course 内
逗号数量加 1 的思路进行统计
*/


SELECT
    SUM(LENGTH(t1.course) - LENGTH(REPLACE(t1.course, ",", "")) + 1) staff_nums
FROM cultivate_tb t1
