# -*- coding: utf-8 -*-
"""
Created on Wed Feb 12 12:54:01 2020

@author: liuga
"""

SELECT t.Request AS 'Day',
ROUND(SUM(IF(t.Status == 'completed',0,1))/COUNT(*)，2) AS 'cancellation Rate'
FROM Trips t INNER JOIN User u ON t.Clint_id == u.User_id
WHERE t.Reuqest_at BETWEEN '2013-10-01' and '2013-10-03'
AND u.Banned = 'No' and u.role == 'client'
GROUP BY t.Request_at ORDER BY t.Request_at
