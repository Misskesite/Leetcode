# -*- coding: utf-8 -*-
"""
Created on Wed Jul 15 17:18:59 2020

@author: liuga
"""


select distinct e1.id, e1.month, 
sum(e1.salary) over(partition by e1.id order by e1.month)
from employee e1,
(select id, max(month) month from employee group by id) e2
where e1.id = e2.id and e1.month < e2.month
order by e1.ID;
