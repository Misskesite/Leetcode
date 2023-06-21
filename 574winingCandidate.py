# -*- coding: utf-8 -*-
"""
Created on Tue Jul 14 17:06:13 2020

@author: liuga
"""

select Name from candidate c join 
(
select top 1 CandidateId from Vote
group by CandidateId 
order by count(*) desc
) as w
on c.id = w.CandidateId