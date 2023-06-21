# -*- coding: utf-8 -*-
"""
Created on Sun Jul 19 11:21:30 2020

@author: liuga
"""

SELECT customer_number FROM orders GROUP BY customer_number HAVING count(*) >= ALL (SELECT count(*) FROM orders GROUP BY customer_number)