https://leetcode.com/problems/exchange-seats/

Mary is a teacher in a middle school and she has a table seat storing students' names and their corresponding seat ids.
The column id is continuous increment.
Mary wants to change seats for the adjacent students.
Can you write a SQL query to output the result for Mary?
+---------+---------+
|    id   | student |
+---------+---------+
|    1    | Abbot   |
|    2    | Doris   |
|    3    | Emerson |
|    4    | Green   |
|    5    | Jeames  |
+---------+---------+
For the sample input, the output is:
 

+---------+---------+
|    id   | student |
+---------+---------+
|    1    | Doris   |
|    2    | Abbot   |
|    3    | Green   |
|    4    | Emerson |
|    5    | Jeames  |
+---------+---------+
Note:
If the number of students is odd, there is no need to change the last one's seat


            
            
🐝 ------  🐝 ------  🐝 ------  🐝 ------  🐝 ------  🐝 ------  
# Write your MySQL query statement below
select
    case
        when id %2  = 0 then id-1
        when id %2 != 0 and id = (select max(id) 
                                  from seat) then id
        else id+1
    end as id
    , student
from seat
order by id;

            
🐝 ------  🐝 ------  🐝 ------  🐝 ------  🐝 ------  🐝 ------  
SELECT
	CASE
		WHEN seat.id % 2 <> 0 AND seat.id = (SELECT COUNT(*) FROM seat) THEN seat.id
		WHEN seat.id % 2 = 0 THEN seat.id - 1
		ELSE
			seat.id + 1
	END as id,
	student 
FROM seat
ORDER BY id

🐝 ------  🐝 ------  🐝 ------  🐝 ------  🐝 ------  🐝 ------  
这个理解起来太麻烦了：
# Write your MySQL query statement below
select
    if(id < (select count(*) from seat)
       , if(id mod 2 = 0, id-1, id+1)
       , if(id mod 2 = 0, id-1, id)) as id
   , student
from seat
order by id asc;
