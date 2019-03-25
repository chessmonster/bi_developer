-- ####### PART 1 QUERIES #######

-- get percentage per day all

select 'within 1 day' as leadtime ,count(id) as 'day' from exam_app_package where leadtime between 0.001 and 1
union all
select 'within 2 days' as leadtime ,count(id) as 'day' from exam_app_package where leadtime between 1.001 and 2
union all
select 'within 3 days' as leadtime ,count(id) as 'day' from exam_app_package where leadtime between 2.001 and 3
union all
select 'within 4 days' as leadtime ,count(id) as 'day' from exam_app_package where leadtime between 3.001 and 4
union all
select 'within 5 days' as leadtime ,count(id) as 'day' from exam_app_package where leadtime between 4.001 and 5
union all
select 'within 6 days' as leadtime ,count(id) as 'day' from exam_app_package where leadtime between 5.001 and 6
union all
select 'within 7 days' as leadtime ,count(id) as 'day' from exam_app_package where leadtime between 6.001 and 7

select count(id) from exam_app_package

-- get percentage per day GMA only

select 'within 1 day' as leadtime ,count(id) as 'day' from exam_app_package where leadtime between 0.001 and 1 and major_region = 'GMA'
union all
select 'within 2 days' as leadtime ,count(id) as 'day' from exam_app_package where leadtime between 1.001 and 2 and major_region = 'GMA'
union all
select 'within 3 days' as leadtime ,count(id) as 'day' from exam_app_package where leadtime between 2.001 and 3 and major_region = 'GMA'
union all
select 'within 4 days' as leadtime ,count(id) as 'day' from exam_app_package where leadtime between 3.001 and 4 and major_region = 'GMA'
union all
select 'within 5 days' as leadtime ,count(id) as 'day' from exam_app_package where leadtime between 4.001 and 5 and major_region = 'GMA'
union all
select 'within 6 days' as leadtime ,count(id) as 'day' from exam_app_package where leadtime between 5.001 and 6 and major_region = 'GMA'
union all
select 'within 7 days' as leadtime ,count(id) as 'day' from exam_app_package where leadtime between 6.001 and 7 and major_region = 'GMA'

select count(id) from exam_app_package where major_region = 'GMA'

-- count packages per major region

select major_region, count(id)
from exam_app_package
group by major_region

-- count packages per address in GMA

select address, count(id) as bilang
from exam_app_package
where major_region ='GMA'
group by address
order by bilang desc

-- ####### PART 2 QUERIES #######

-- QUESTION 1

select 
    unit_price, name, sku, shipping_type
from exam_app_ImsSalesOrderItem
where id_sales_order_item = 229884

-- QUESTION 2

select 
    item.id_sales_order_item
    , item.name
    , item.sku
    , status.status
from exam_app_imssalesorderitem item
left join exam_app_imssalesorderitemstatus status
on item.fk_sales_order_item_status_id = status.id_sales_order_item_status

-- QUESTION 3

select sum(unit_price)
from exam_app_imssalesorderitem
where shipping_type = 'cross_docking'

-- QUESTION 4

select id_sales_order_item, name, sku
from exam_app_ImsSalesOrderItem
where id_sales_order_item in (
    select fk_sales_order_item_id
    from exam_app_ImsSalesOrderItemstatushistory
    where fk_sales_order_item_status_id = (select id_sales_order_item_status from exam_app_ImsSalesOrderItemstatus where status = 'picklisted')
    and created_at like '%11/06/2013%'
)

-- QUESTION 5

select *
from exam_app_ImsSalesOrderItem
where shipping_type in (
    'marketplace', 'cross_docking', 'warehouse')
and unit_price between 50 and 100
and id_sales_order_item in (
    select fk_sales_order_item_id
    from exam_app_ImsSalesOrderItemstatushistory
    where fk_sales_order_item_status_id = (select id_sales_order_item_status from exam_app_ImsSalesOrderItemstatus where status = 'picklisted')
    and created_at like '%11/06/2013%')
