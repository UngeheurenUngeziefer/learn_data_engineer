-- CTE vs SUB-QUERIES 

-- CTE

with _freight_sum as (
       select 
              sum(freight) as freight_sum, 
              orderid, 
              custid 
       from [TestSQL].[Sales].[Orders] 
       group by orderid, custid
), result as (
       select 
              row_number() over(partition by custid order by freight_sum desc) as  rn,
              freight_sum,
              orderid, 
              custid 
       from _freight_sum
)
select 
       * 
from result
where rn < 3
order by custid




-- sub-queries

select 
       * 
from (
       select 
            row_number() over(partition by custid order by freight_sum desc) as rn,
            freight_sum,
            orderid, 
            custid 
       from (
              select 
                     sum(freight) as freight_sum, 
                     orderid, 
                     custid 
              from [TestSQL].[Sales].[Orders] 
              group by orderid, custid
       )_freight_sum
) result
where rn < 3
order by custid
