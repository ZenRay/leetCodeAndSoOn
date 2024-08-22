
/* 描述你正在搭建一个用户活跃度的画像，其中一个与活跃度相关的特征是“最长连续登录天数”， 
请用SQL实现“2023年1月1日-2023年1月31日用户最长的连续登录天数”

drop table if exists tb_dau;
create table `tb_dau` (
    `fdate` date,
    `user_id` int
);
insert into tb_dau(fdate, user_id)
values 
('2023-01-01', 10000),
('2023-01-02', 10000),
('2023-01-04', 10000);
复制
输出：
user_id|max_consec_days
10000|2
*/


/*
===== 思路====
最大连续登录存在的几种情况
1. 连续登录存在间隔之后登录
2. 存在只登录一次
3. 最大的连续登录的位置可能在开始今天，可能在间隔的中间或者最后

解答:
1. 因此需要找到每次登录的第一天日期
2. 按照日期统计出第一天登录日期的次数
3. 找到最大次数
*/

SELECT
    t1.user_id
    ,MAX(days) AS max_consec_days
FROM(
    SELECT
        t1.user_id
        ,t1.start_date
        ,COUNT(t1.fdate) AS days
    FROM(
        SELECT
            t1.user_id
            ,t1.fdate
            ,DATE_SUB(t1.fdate, INTERVAL (ROW_NUMBER() OVER(PARTITION BY user_id ORDER BY fdate)) DAY)  AS start_date
        FROM tb_dau t1
        WHERE YEAR(t1.fdate) = 2023
    ) t1
    GROUP BY t1.user_id
        ,t1.start_date
) t1
GROUP BY t1.user_id
