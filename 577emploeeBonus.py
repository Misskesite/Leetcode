# -*- coding: utf-8 -*-
"""
Created on Wed Jul 15 16:30:03 2020

@author: liuga
"""

SELECT name, bonus 
FROM Employee LEFT JOIN Bonus USING (empId)
WHERE IFNULL(bonus, 0) < 1000