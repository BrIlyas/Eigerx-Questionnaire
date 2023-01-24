SELECT D1.NAME,
       E1.EMP_COUNT
FROM   DEPARTMENT D1
       LEFT OUTER JOIN (SELECT DEPT_ID,
                               Count(*) AS emp_count
                        FROM   EMPLOYEE
                        GROUP  BY DEPT_ID) E1
                    ON D1.ID = E1.DEPT_ID
ORDER  BY E1.EMP_COUNT DESC,
          D1.NAME ASC;  