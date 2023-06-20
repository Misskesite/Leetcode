# -*- coding: utf-8 -*-
"""
Created on Wed Dec 18 19:29:19 2019

@author: liuga
"""

#sql
select FirstName, LastName, City, State from Person left join Address on Person.persionId = Adress.personId

select (select dictinct(salary) from Employee order by Salary Desc limit 1,1) as Secondhighest

select distinct(p.Email) from Person P, person P1
where p.id <>p1.id and p.email==p1.email
