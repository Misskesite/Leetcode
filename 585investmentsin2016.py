# -*- coding: utf-8 -*-
"""
Created on Fri Jul 17 17:48:26 2020

@author: liuga
"""

select sum(TIV_2016) as TIV_2016
from insurance
where tiv_2015 in (select TIV_2015  from insurance group by TIV_2015 having count(*)>1)
and CONCAT(LAT,CONCAT(',',LON)) in (select CONCAT(LAT,CONCAT(',',LON)) 
from insurance group by CONCAT(LAT,CONCAT(',',LON)) having count(*)=1)