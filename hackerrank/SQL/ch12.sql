/*
Amber's conglomerate corporation just acquired some new companies. Each of the companies follows this hierarchy:

Given the table schemas below, write a query to print the company_code, founder name, total number of lead managers, total number of senior managers, total number of managers, and total number of employees. Order your output by ascending company_code.

Note:

    The tables may contain duplicate records.
    The company_code is string, so the sorting should not be numeric. For example, if the company_codes are C_1, C_2, and C_10, then the ascending company_codes will be C_1, C_10, and C_2.

*/

select C.company_code,
        C.founder,
        count(distinct L.lead_manager_code),
        count(distinct S.senior_manager_code),
        count(distinct M.manager_code),
        count(distinct E.employee_code)
from 
    Company C
INNER JOIN 
    Lead_Manager L 
on (C.company_code = L.company_code)
inner join
    Senior_Manager S
on (C.company_code = S.company_code)
inner join
    Manager M
on (C.company_code = M.company_code)
inner join
    Employee E
on (C.company_code = E.company_code)
group by C.company_code, C.founder
order by C.company_code asc;