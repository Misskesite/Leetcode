# -*- coding: utf-8 -*-
"""
Created on Mon Jul 13 23:15:26 2020

@author: liuga
"""

SELECT 
       t.id
       t.company
       t.salary
   FROM
       (
        SELECT
            a.id,
            a.company,
            a.Salary,
        IF ( @com = a.company, @rn := @rn + 1, @rn := 1 ) AS rn,
            @com := a.company -- 必须放在后面
        FROM
            Employee a,
            ( SELECT @rn := 1, @com := NULL ) b 
        ORDER BY
            company,
            Salary 
        ) t 
        
    left join (SELECT company,count(*) as cnt from employee group by company) m
    on t.company = m.company
    where 
    t.rn in (FLOOR(m.cnt/2 + 1),CEIL(m.cnt/2))
    
       
       
       