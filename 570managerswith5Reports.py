# -*- coding: utf-8 -*-
"""
Created on Tue Jul 14 10:05:58 2020

@author: liuga
"""

select * from employee
 
with cte as(
select ManagerId from employee
group by ManagerId
having count(Id)>=5
) select Name from employee e join cte c on e.Id=c.ManagerId