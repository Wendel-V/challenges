-- Problem 1

select city
		from "alanparadise/cm"."offices"
order by city; 

--Problem 2

select employeenumber, lastname, firstname, extension  
		from "alanparadise/cm"."employees"
		where officecode = 4

--Problem 3

select ProductCode, ProductName, ProductVendor, quantityinstock, productline 
		from "alanparadise/cm"."products"  
		where quantityinstock between 200 and 1200;

--Problem 4

select Productcode, ProductName, productvendor, buyprice, MSRP   
		from "alanparadise/cm"."products"
		where MSRP = ( 
 		select min(msrp) from "alanparadise/cm"."products")

--Problem 5

select ProductName, (MSRP – BuyPrice) as PROFIT   
		from "alanparadise/cm"."products"
	order by profit desc limit 1;

--Problem 6

Select distinct country, count(*) as customers
		from "alanparadise/cm"."customers"
		group by country
			having count(*) = 2 
order by 1 asc; 

--Problem 7

Select p.productcode, productname, 
			count(ordernumber) as OrderCount  	
		from "alanparadise/cm"."products" p join "alanparadise/cm"."orderdetails" o 
        on p.productcode = o.productcode     
group by productcode, productname 
having OrderCount = 25;

--Problem 8

Select employeenumber, 
			concat(firstname," ",lastname) as name 
 	from "alanparadise/cm"."employees"
    where reportsto in ('1002', '1102');

--Problem 9

Select employeenumber, lastname, firstname 
		from "alanparadise/cm"."employees"
		where reportsto is null;

--Problem 10

Select productname, productline  
	      from "alanparadise/cm"."products"
	      where productline = "Classic Cars"  
	         and productname like "195%" 
order by productname;

--Problem 11

select count(ordernumber),  
			monthname(orderdate) as ordermonth  
		from  "alanparadise/cm"."orders"
		where extract(year from "alanparadise/cm"."orderdate") = '2004' group by ordermonth 
order by 1 desc limit 1;

--Problem 12

select lastname, firstname 
		from "alanparadise/cm"."employees" e left outer join "alanaparadise/cm"."customers" c 
        on e.employeenumber = c.salesrepemployeenumber 
where customername is null  
		and jobtitle = "Sales Rep";

--Problem 13

select customername , country 
		from "alanparadise/cm"."customers" c left outer join "alanparadise/cm"."orders" o 
        on c.customernumber = o.customernumber 
where o.customernumber is null    
	  and country = 'Switzerland';

--Problem 14

select customername, sum(quantityordered) as totalq 
		from "alanparadise/cm"."customers" c  
			join "alanparadise/cm"."orders" o on c.customernumber = o.customernumber 
          join "alanparadise/cm"."orderdetails" d on o.ordernumber = d.ordernumber 
group by customername  
having totalq > 1650;


---------------------------------------------------------------------------------------------------------------

--Problem 1

create table if not exists TopCustomers ( 
 	Customernumber int not null,  
	ContactDate    DATE not null, 
     OrderTotal 	decimal(9,2) not null default 0, 		constraint     PKTopCustomers primary key (CustomerNumber) 
 );

--Problem 2

insert into TopCustomers 
	select c.customernumber, CURRENT_date, 
			  SUM(priceEach * Quantityordered) 
 	   	from "Wendel-V/nw"."Customers" c, "Wendel-V/nw"."Orders" o,"Wendel-V/nw"."OrderDetails" d  	 	
			where c.Customernumber = o.Customernumber  
      	  and o.Ordernumber = d.Ordernumber 
 	group by c.Customernumber 
 	having SUM(priceEach * Quantityordered) > 140000;

--Problem 3

select * from "Wendel-V/nw"."topcustomers" order by 3 desc;

--Problem 4

alter table "Wendel-V/nw"."topcustomers" 
		add column OrderCount integer ;

--Problem 5

update "Wendel-V/nw"."topcustomers"
		set ordercount = floor((rand()*18));

--Problem 6

select * 
		from "Wendel-V/nw"."topcustomers"
		order by 4 desc;

--Problem 7

Drop table "Wendel-V/nw"."topcustomers"; 
