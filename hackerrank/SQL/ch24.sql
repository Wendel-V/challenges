/*

A median is defined as a number separating the higher half of a data set from the lower half. Query the median of the Northern Latitudes (LAT_N) from STATION and round your answer to decimal places. 

*/

SELECT ROUND(LAT_N, 4)
FROM (select LAT_N
    from STATION
    order by LAT_N DESC
    LIMIT 250) AS S
ORDER BY LAT_N ASC
LIMIT 1;