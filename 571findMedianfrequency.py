# -*- coding: utf-8 -*-
"""
Created on Tue Jul 14 10:30:38 2020

@author: liuga
"""

SELECT AVG(Number) AS median FROM (
  SELECT Number, Frequency, AccFreq, SumFreq FROM
  (SELECT    Number,
             Frequency, @curFreq := @curFreq + Frequency AS AccFreq
   FROM      Numbers n, (SELECT @curFreq := 0) r
   ORDER BY  Number) t1,
  (SELECT SUM(Frequency) SumFreq FROM Numbers) t2
) t
WHERE AccFreq BETWEEN SumFreq / 2 AND SumFreq / 2 + Frequency