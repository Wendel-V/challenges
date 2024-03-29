/*
Query the list of CITY names from STATION that do not start with vowels. Your result cannot contain duplicates.
*/

select distinct(city) from station 
where substring(city, 1, 1) NOT IN ('a', 'e', 'i', 'o', 'u');