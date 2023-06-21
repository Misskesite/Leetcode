# -*- coding: utf-8 -*-
"""
Created on Wed Jul 15 17:01:58 2020

@author: liuga
"""

SELECT question_id as survey_log
FROM
(
	SELECT question_id,
		SUM(case when action = "answer" THEN 1 ELSE 0 END) as num_answers,
		SUM(case when action = "show" THEN 1 ELSE 0 END) as num_shows
	FROM survey_log
	GROUP BY question_id
) as tbl
ORDER BY (num_answers / num_shows) DESC
LIMIT 1;
