# -*- coding: utf-8 -*-
"""
Created on Fri Jul 17 17:18:49 2020

@author: liuga
"""

#mysql

SELECT name FROM customer WHERE referee_id <> 2 OR referee_id IS NULL;

SELECT name FROM customer WHERE referee_id != 2 OR referee_id IS NULL;